import random

'''
2(adj) + 3(noun)
4(verb) + 1(dete) + 2(noun)
3(verb) + 2(adve)
'''
def adj(adj):
    with open('adj_2.txt', encoding='utf-8') as f:
        text = f.read()
        adj = text.split()
    return random.choice(adj)
def adv(adv):
    with open('adve_2.txt', encoding='utf-8') as f:
        text = f.read()
        adv = text.split()
    return random.choice(adv)
def noun_2(noun_2):
    with open('noun_2.txt', encoding='utf-8') as f:
        text = f.read()
        noun_2 = text.split()
    return random.choice(noun_2)
def noun_3(noun_3):
    with open('noun_3.txt', encoding='utf-8') as f:
        text = f.read()
        noun_3 = text.split()
    return random.choice(noun_3)
def art(art):
    with open('opr_art.txt', encoding='utf-8') as f:
        text = f.read()
        art = text.split()
    return random.choice(art)
def verb_3(verb_3):
    with open('verb_3.txt', encoding='utf-8') as f:
        text = f.read()
        verb_3 = text.split()
    return random.choice(verb_3)
def verb_4(verb_4):
    with open('verb_4.txt', encoding='utf-8') as f:
        text = f.read()
        verb_4 = text.split()
    return random.choice(verb_4)

def punctuation():
    marks = [".", "?", "!", "..."]
    return random.choice(marks)

def verse1():
    return adj(adj) + ' ' + noun_3(noun_3) + punctuation()
def verse2():
    return verb_4(verb_4) + ' ' + art(art) + ' ' + noun_2(noun_2) + punctuation()
def verse3():
    return verb_3(verb_3) + ' ' + noun_2(noun_2) + punctuation()

print(verse1())
print(verse2())
print(verse3())
