#!/usr/bin/env python3
from collections import defaultdict

def file_extensions(filename):
    file_dict = defaultdict(list)
    file_list = []
    with open(filename, 'r') as file:
        file_reader = file.read().splitlines()
        try:
            for line in file_reader:
                index = line.index('.')
                file_dict[line.split('.')[-1]].append(line)
        
        except:
            file_list.append(line)

    file_dict = dict(file_dict)
    return (file_list, file_dict)

def main():
    file_list, file_dict = file_extensions('filenames.txt')
    print('{} files with no extension'.format(len(file_list)))
    for extension, file_name in sorted(file_dict.items()):
        print(extension, len(file_name))

if __name__ == "__main__":
    main()
