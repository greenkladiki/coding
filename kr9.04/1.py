'''
Для работы программы понадобится файл с разметкой из исландского корпуса.
Размеченные тексты выстроены таким образом, что на одной строке
располагается одна словоформа в следующем виде:
<w lemma="til" type="ae">Til</w>. Морфологическая разметка даётся
как последовательность символов внутри type="",
где каждый символ кодирует определённый грамматический показатель.
Что значат эти показатели, написано в отдельном pdf-файле .

1. (5 баллов) Открыть файл с корпусом, подсчитать в нём число строк
заголовка XML (то есть от начала файла до строки, которая содержит
"</teiHeader>"), открыть другой файл для записи,
записать туда число подсчитанных строк.

2. (8 баллов) Создать словарь,
в котором ключами являются строки с морфологическим разбором слов
(то есть значения атрибута type для строк, в которых имеется "<w lemma="),
а значениями - количество их вхождений в файле.
Распечатать пары ключ-значение из словаря в открытый для записи файл
таким образом, чтобы каждая пара располагалась на одной строке.
'''
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
