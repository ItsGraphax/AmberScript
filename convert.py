from os import listdir
from os.path import isfile, join

import re

def list_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

files = list_files('.')
files = [file for file in files if file.endswith('.as')]

data = {}

def to_func(text, name):
    text = re.sub(r'(\n(#.+)?)+', r'\\\\c', text)
    text = f'function.register {name} "{text}"'
    return text
    

def convert(filepath):
    contents = open(filepath).read()

    contents = contents.replace('\\', '\\\\')
    contents = re.sub(r'(?<!\\)\$', r'\$', contents)

    with open(f'output/{filepath}', 'w') as file:
        file.write(contents)

    data[filepath] = contents

for path in files:
    convert(path)

with open('output/main.as', 'w') as main:
    with open('output/file.txt','w') as file:
        for name, commands in zip(data.keys(), data.values()):
            func = to_func(commands, name[:-3])
            main.write(func + '\n')
            file.write(func + '\\n')
