import os
os.system('clear')


one = ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R',
       'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т', 'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r')
two = ('Д', 'К', 'Л', 'М', 'П', 'У', 'D', 'G', 'д', 'к', 'л', 'м', 'п', 'у', 'd', 'g')
three = ('Б', 'Г', 'Ё', 'Ь', 'Я', 'B', 'C', 'M', 'P', 'б', 'г', 'ё', 'ь', 'я', 'b', 'c', 'm', 'p')
four = ('Й', 'Ы', 'F', 'H', 'V', 'W', 'Y', 'й', 'ы', 'f', 'h', 'v', 'w', 'y')
five = ('Ж', 'З', 'Х', 'Ц', 'Ч', 'K', 'ж', 'з', 'х', 'ц', 'ч', 'k')
eight = ('Ш', 'Э', 'Ю', 'J', 'X', 'ш', 'э', 'ю', 'j', 'x')
ten = ('Ф', 'Щ', 'Ъ', 'Q', 'Z', 'ф', 'щ', 'ъ', 'q', 'z')
myList = [one, two, three, four, five, eight, ten]
dic = {one: 1, two: 2, three: 3, four: 4, five: 5, eight: 8, ten: 10}

def whereChar (stringChar, collections, dictionary):  #~~~ поиск кортежа с заданной буквой ~~~~
    if stringChar in collections:
        return dictionary[collections]
    else: return 0

count = 0   #~~~ подсчет баллов за буквы ~~~~
word = [i for i in input('введи слово или фразу: ')]
for myChar in word:
    for i in myList:
        count += whereChar(myChar, i, dic)
print(f'получаете {count} балла (ов)')