import re

def remake_file():
    title = input('Hазвание без .txt: ') + '.txt'
    with open(title, 'r', encoding='utf-8') as txt:
        text = txt.read()
    text = re.sub(r'[!?]', '\.', text)
    text = re.sub('\.\.\.', '\.', text)
    sentences = text.split('.')
    sentences2 = [re.sub(r'[«\n,:;"—\\»]', '', phrase) for phrase in sentences]
    sentences = [re.sub(r'^(\s)*(\S)', r'\2', phrase) for phrase in sentences2]
    rf = [phrase for phrase in sentences if phrase]
    return rf

def lots_of_dicts(text):
    my_dict = {}
    for phrase in text:
        sentdict = {word: len(word) for word in phrase.split(' ')}
        my_dict[phrase] = sentdict
    return my_dict

def formatirovanie(my_dict):
    for key in my_dict:
        print('sntnc :) {kl} :)\ndict :) {zn}'.format(zn = my_dict[key], kl = key))
        
def main():
    text = remake_file()
    my_dict = lots_of_dicts(text)
    formatirovanie(my_dict)

if __name__ == '__main__':
    main()
