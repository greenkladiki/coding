import re

def open_file():
    name = input('Введите название исходного файла с расширением: ')
    with open(name, "r", encoding="utf-8") as isl:
        text = isl.read()
    
    return text

def count(text):
    result = re.search(r'<teiHeader>(.*?)</teiHeader>', text, re.DOTALL)
    return len(result.group(1))

def create_file(a):
    result = input('Введите название результирующего файла с расширением: ')    
    with open(result, "w", encoding="utf-8") as res_file:
        res_file.write(str(a))

def create_predict(text):
    predict = re.match(r'.[w]', text)
    return str(predict)

def find_key(predict):
    keys = re.findall(r'type="([^"]*)"', predict)
    dicti = {}
    for word in keys:
        if word in dicti:
            dicti[word] += 1
        else:
            dicti[word] = 1
    return dicti

def create_dicti(dicti):
    result = input('Введите название словаря с расширением: ')    
    with open(result, "w", encoding="utf-8") as res_file:
        for key in sorted(dicti, key=dicti.get, reverse=True):
            res_file.write(str(dicti[key]) + '\t' + key + '\n')

def main():
    text = open_file()
    a = count(text)
    create_file(a)
    predict = create_predict(text)
    dicti = find_key(predict)
    create_dicti(dicti)
    
if __name__ == '__main__':
    main()
