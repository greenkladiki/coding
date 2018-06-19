'''
1 (5 баллов). Создайте csv-таблицу с полями "doc_id", "title", "author",
"created", "topic", "tagging" с информацией о всех статьях (см. тег meta).
'''
import re

def open_file():
    with open ('new.zip', 'r', encoding='windows-1251') as file:
        text = file.read()
        splited_text = text.split('\n')
    return splited_text

def doc_id(splited_text):
    for line in splited_text:
        if re.findall('docid', line):
            a = re.search('content="(\S*)"\s', line)
            res1 = a.group(1)
    return res1

def title(splited_text):
    for line in splited_text:
        if re.findall('title', line):
            a = re.search('content="(\S*)"\s', line)
            res2 = a.group(1)
    return res2

def author(splited_text):
    for line in splited_text:
        if re.findall('author', line):
            a = re.search('content="(\S*)"\s', line)
            res3 = a.group(1)
    return res3

def created(splited_text):
    for line in splited_text:
        if re.findall('created', line):
            a = re.search('content="(\S*)"\s', line)
            res4 = a.group(1)
    return res4

def topic(splited_text):
    for line in splited_text:
        if re.findall('topic', line):
            a = re.search('content="(\S*)"\s', line)
            res5 = a.group(1)
    return res5

def tagging(splited_text):
    for line in splited_text:
        if re.findall('tagging', line):
            a = re.search('content="(\S*)"\s', line)
            res6 = a.group(1)
    return res6

def create_file(res1, res2, res3, res4, res5, res6):
    with open('h.csv', 'w', encoding='windows-1251') as w:
            w.write('docid' + '\t' + str(res1) + '\n' 'docid' + '\t' + str(res1) + '\n' + 'title' + '\t' + str(res2) + '\n' + 'author' + '\t' + str(res3) + '\n' + 'created' + '\t' + str(res4) + '\n' + 'topic' + '\t' + str(res5) + '\n' + 'tagging' + '\t' + str(res6) + '\n')

def main():
    splited = open_file()
    res1 = doc_id(splited_text)
    res2 = title(splited_text)
    res3 = author(splited_text)
    res4 = created(splited_text)
    res5 = topic(splited_text)
    res6 = tagging(splited_text)
    create_file(res1, res2, res3, res4, res5, res6)
    
if __name__ == '__main__':
    main()
