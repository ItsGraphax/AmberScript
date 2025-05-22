from os import listdir
from os.path import isfile, join

import re

PROJECT_PATH = 'project/'
OUTPUT_PATH = 'output/'

def list_files(path:str, ending:str) -> list[str]:
    """Lists all files in the directory that end on ending"""
    return [file for file in [f for f in listdir(path) if isfile(join(path, f))] if file.endswith(ending)]

def to_func(text:str) -> str:
    text = re.sub(r'(\n(#.+)?)+', r'\\n', text)
    return text

files = list_files(PROJECT_PATH, '.as')

with open('output/file.txt','w') as file:
    for filepath in files:
        print(f'[Log] Parsing {filepath}')
        text = contents = open(PROJECT_PATH + filepath).read()
        text = to_func(text)
        file.write(f'{filepath[:-3]} -> {text}\n')

