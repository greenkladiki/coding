import re

def open_file():
    name = input('Введите название исходного файла с расширением: ')
    with open(name, "r", encoding="utf-8") as phil:
        text = phil.read()
    return text

def exchange(text):
    text = re.sub(r'(\W|^)филосо.?фи([яиюей][йюмх]?и?)', r'\1астрологи\2',text)
    text = re.sub(r'(\W|^)Филосо.?фи([яиюей][йюмх]?и?)', r'\1Астрологи\2',text)
    return text

def create_file(text):
    result = input('Введите название результирующего файла с расширением: ')    
    with open(result, "w", encoding="utf-8") as res:
        res.write(text)

def main():
    text = open_file()
    text = exchange(text)
    create_file(text)

if __name__ == '__main__':
    main()
