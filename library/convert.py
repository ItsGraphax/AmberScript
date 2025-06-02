import os
import re

PROJECT_PATH = 'project/'
OUTPUT_PATH = 'output/'

def to_func(text: str) -> str:
    # Remove comments (lines starting with # or inline #) and blank lines, then
    # replace newlines with literal "\n"
    text = re.sub(r'(?m)^\s*#.*\n?|(?<!\S)#.*|^\s*\n', '', text)
    return text.replace('\n', '\\n')

with open(os.path.join(OUTPUT_PATH, 'file.txt'), 'w', encoding='utf-8') as out_file:
    # Walk through PROJECT_PATH recursively
    for dirpath, dirnames, filenames in os.walk(PROJECT_PATH):
        for fname in filenames:
            if not fname.endswith('.as'):
                continue

            full_path = os.path.join(dirpath, fname)
            # Compute the relative path from PROJECT_PATH, e.g. 'foo/bar/B.as'
            rel_path = os.path.relpath(full_path, PROJECT_PATH)

            # Build a key by removing ".as" and replacing os.sep with "."
            key_without_ext = os.path.splitext(rel_path)[0]
            key = key_without_ext.replace(os.sep, '.')

            print(f'[Log] Parsing {rel_path}')
            with open(full_path, 'r', encoding='utf-8') as f:
                contents = f.read()

            processed = to_func(contents)
            out_file.write(f'{key} -> {processed}\n')
