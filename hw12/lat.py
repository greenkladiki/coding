import os
import re

def read_names():
    name_list = os.listdir()
    with open ('spisok.txt', 'w', encoding='utf-8') as f:
        spisok = f.write(str(name_list))
    return spisok

def open_res(spisok):
    with open('spisok.txt', 'r', encoding='utf-8') as f:
        names = f.read()
    return names

def find_count_res(names):
    res = re.findall(r'[A-Z][a-z]*\.\w*', names)
    num = len(res)
    return num, res

def main():
    spisok = read_names()
    names = open_res(spisok)
    num = find_count_res(names)
    res = find_count_res(names)
    print(num)

if __name__ == '__main__':
    main()
