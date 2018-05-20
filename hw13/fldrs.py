import re
import os

def search():
    folders = {}
    for root, dirs, files in os.walk(os.getcwd()):
        garbage, rootname = os.path.split(root)
        letter = rootname[0]
        if letter in folders:
            folders[letter] += 1
        else:
            folders[letter] = 1
    return folders

def print_res(fldrs):
    for letter in sorted(fldrs, key=fldrs.get, reverse=True):
        print(letter, '\t', fldrs[letter])
        break
    
def main():
    fldrs = search()
    print_res(fldrs)

if __name__ == '__main__':
    main()
