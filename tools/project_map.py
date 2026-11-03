#!/usr/bin/env python3
"""Index project files and search human-reviewed annotations. Standard library only."""
import argparse
import hashlib
import json
import os
from pathlib import Path

FIELDS = {'summary', 'tags', 'category', 'review_status', 'public_use', 'selected_for', 'location_notes'}


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    temporary.replace(path)


def index(source, output, annotations):
    source, output = source.resolve(), output.resolve()
    if not source.is_dir():
        raise ValueError('Source must be an existing project directory')
    if output == source or source in output.parents:
        raise ValueError('Keep map output outside the original project folder')
    if output in source.parents:
        raise ValueError('Map output must not contain the source directory')
    notes = read_json(annotations) if annotations else {}
    if not isinstance(notes, dict):
        raise ValueError('Annotations must be a JSON object keyed by source-relative path')
    records, skipped, seen = [], [], {}
    for directory, dirs, files in os.walk(source, followlinks=False):
        dirs.sort()
        for name in list(dirs):
            path = Path(directory) / name
            if path.is_symlink():
                skipped.append({'path': path.relative_to(source).as_posix(), 'reason': 'symlink directory'})
                dirs.remove(name)
        for name in sorted(files):
            path = Path(directory) / name
            relative = path.relative_to(source).as_posix()
            if path.is_symlink() or not path.is_file():
                skipped.append({'path': relative, 'reason': 'symlink or non-regular file'})
                continue
            try:
                before = path.stat()
                digest = hashlib.sha256()
                with path.open('rb') as stream:
                    for block in iter(lambda: stream.read(1024 * 1024), b''):
                        digest.update(block)
                after = path.stat()
                if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                    raise ValueError('file changed during indexing; rerun')
                checksum = digest.hexdigest()
                note = notes.get(relative, {})
                if not isinstance(note, dict) or set(note) - FIELDS:
                    raise ValueError('annotation has unsupported fields or is not an object')
                record = {
                    'id': 'F-' + hashlib.sha256(relative.encode()).hexdigest()[:16],
                    'path': relative,
                    'extension': path.suffix.lower(),
                    'size_bytes': after.st_size,
                    'sha256': checksum,
                    'duplicate_of': seen.get(checksum),
                    'summary': '', 'tags': [], 'category': 'unclassified',
                    'review_status': 'unreviewed', 'public_use': 'unknown',
                    'selected_for': [], 'location_notes': '',
                    **note,
                }
                for key in ('tags', 'selected_for'):
                    if not isinstance(record[key], list) or not all(isinstance(x, str) for x in record[key]):
                        raise ValueError(key + ' must be a list of strings')
                for key in FIELDS - {'tags', 'selected_for'}:
                    if not isinstance(record[key], str):
                        raise ValueError(key + ' must be text')
                records.append(record)
                seen.setdefault(checksum, record['id'])
            except (OSError, ValueError) as error:
                skipped.append({'path': relative, 'reason': str(error)})
    result = {'schema_version': 1, 'source_root': str(source),
              'annotation_file': str(Path(annotations).resolve()) if annotations else None,
              'files': records, 'skipped': skipped,
              'unused_annotation_paths': sorted(set(notes) - {x['path'] for x in records})}
    write_json(output / 'project-map.json', result)
    print(json.dumps({'map': str(output / 'project-map.json'), 'indexed': len(records),
                      'skipped': len(skipped), 'unused_annotations': result['unused_annotation_paths']}))
    return 1 if skipped else 0


def find(map_path, query, public_only, selected_for):
    catalog = read_json(map_path)
    terms = query.casefold().split()
    matches = []
    for record in catalog['files']:
        haystack = json.dumps({k: record.get(k) for k in
            ('path', 'summary', 'tags', 'category', 'selected_for', 'location_notes')}, ensure_ascii=False).casefold()
        if not all(term in haystack for term in terms):
            continue
        if public_only and record.get('public_use') != 'approved':
            continue
        if selected_for and selected_for not in record.get('selected_for', []):
            continue
        matches.append(record)
    print(json.dumps({'source_root': catalog['source_root'], 'matches': matches}, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    build = commands.add_parser('index', help='Read originals; write a separate JSON file map')
    build.add_argument('--source', type=Path, required=True)
    build.add_argument('--output', type=Path, required=True)
    build.add_argument('--annotations', type=Path)
    search = commands.add_parser('find', help='Search paths and reviewed notes; does not search file contents')
    search.add_argument('--map', type=Path, required=True)
    search.add_argument('--query', default='')
    search.add_argument('--public-only', action='store_true')
    search.add_argument('--selected-for')
    args = parser.parse_args()
    try:
        if args.command == 'index':
            return index(args.source, args.output, args.annotations)
        find(args.map, args.query, args.public_only, args.selected_for)
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, str(error) + '\n')


if __name__ == '__main__':
    raise SystemExit(main())
