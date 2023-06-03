import os
os.system('clear')

def pal(text):
    if text == '': return ''
    return text[-1] + pal(text[:-1])

word = 'локон'
if word == pal(word): print(f'слово {word} - палиндром')
else: print(f'слово {word} - не палиндром')