from random import randint
import os
os.system('clear') 


'''
§§§§§§§§§§§§§§§§§§§§§§§§§  S e m i n a r  1  §§§§§§§§§§§§§§§§§§§§§§§§§
'''
'''
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
if a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    print('a = b')
'''


# Задача No1. Решение в группах
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать
# маршрут длиной m километров? При решении этой задачи нельзя пользоваться
# условной инструкцией if и циклами.

# Input: n = 700 m = 750
# Output: 2


'''
n = int(input('введите расстояние, проезжаемое за день > '))
m = int(input('введите расстояние, которое необходимо проехать > '))
print(f'n = {n} m = {m} Output: {(m + n - 1) // n}')
'''


# Задача No3. Решение в группах
# В некоторой школе решили набрать три новых математических класса и
# оборудовать кабинеты для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся в каждом из трех
# классов. Выведите наименьшее число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32


'''
a1 = int(input('количество учеников в первом кабинете > '))
a2 = int(input('количество учеников во втором кабинете > '))
a3 = int(input('количество учеников в третьем кабинете > '))
print(f'необходимо {(a1 + 1) // 2 + (a2 + 1) // 2 + (a3 + 1) // 2} парт')
'''


# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве


'''
x1 = int(input('введите х координату первой точки > '))
y1 = int(input('введите у координату первой точки > '))
x2 = int(input('введите х координату второй точки > '))
y2 = int(input('введите у координату второй точки > '))
print(f'расстояние между точками в 2D пространстве {((x2-x1)**2+(y2-y1)**2)**0.5}')
'''


# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.

# Input: 3 4(ввод на разных строках)
# Output: 6


'''
i = int(input('введите требуемый номер вагона > '))
j = int(input('введите действительный номер вагона > '))
if i == j:
    print('нельзя определить количество вагонов')
else:
    print(f'{i + j - 1} вагонов')
'''


# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

# Input: 2016
# Output: YES


'''
year = int(input('введите год > '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')
'''


'''
§§§§§§§§§§§§§§§§§§§§§§§§§§  S e m i n a r  2  §§§§§§§§§§§§§§§§§§§§§§§§§§§§§
'''


# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# Input: 5
# Output: 120


'''
x = 0
while x == 0:
    n = int(input('Введите целое неотрицательное число > '))
    if n > 0 and n % 1 == 0:
        x = 1
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(f"факториал введенного числа равен {fact}")
'''


# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6


'''
a = int(input('Введите натуральное число больше 1 > '))  # это мой незаконченный код
n = -1
fib = 1
while True:
    if a == fib:
        n = fib + 3
    elif a > fib:

    
a = int(input("Введите натуральное число больше 1 > "))
status = True
num1 = 0
num2 = 1
i = 2
while status:
    result = num1 + num2
    num1 = num2
    num2 = result
    i = i + 1

    if a == result:
        print(i)
        status = False
    elif result > a:
        print(-1)
        status = False
'''


# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


'''
days = int(input('Введи количество отслеживаемых дней > '))
maxDays = count = 0
for i in range(days):
    dayTemp = randint(-50, 50)
    print(dayTemp)
    if dayTemp > 0:
        count += 1
        if maxDays < count:
            maxDays = count
    else:
        count = 0
print()
print(f"наибольшая продолжительность теплых дней {maxDays}")
'''


#         Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9


'''
size = int(input('Введите количество арбузов > '))
n = randint(1, 10)
print(n)
max = min = n
for i in range(size - 1):
    n = randint(1, 10)
    if max < n:
        max = n
    if min > n:
        min = n
    print(n)
print()
print(f'{min} {max}')
'''


'''
§§§§§§§§§§§§§§§§§§§§§§§§§  S e m i n a r  3  §§§§§§§§§§§§§§§§§§§§§§§§§§§§
'''


# Задача №17:
# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.


'''
n = [1, 1, 2, 0, -1, 3, 4, 4]
n = set(n)
print(len(n))
'''


# Задача №19:
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# Примечание: Пользователь может вводить значения списка или список задан изначально.


'''
n = [1, 2, 3, 4, 5, 6, 7]#   Моё решение
print(n)
k = int(input('введи количество сдвигов > '))
for i in range(k):
    n.insert(0, n.pop(len(n) - 1))
print(n)


list_1 = [int(i) for i in input('введите числа: ').split()]
step = int(input("Введите кол-во сдвигов: "))
result_list = [list_1[i - step] for i in range(len(list_1))]
print(result_list)


list_1 = [int(i) for i in input('введите числа: ').split()]
step = int(input("Введите кол-во сдвигов: "))
result_list = list()
for i in range(len(list_1)):
    result_list.append(list_1[i - step])
print(result_list)


list_1 = [int(i) for i in input("Введите числа: ").split()]
step = int(input("Введите кол-во сдвигов: "))
step = step % len(list_1)
print(step)
result_list = list()
for i in range(len(list_1)):
    result_list.append(list_1[i - step])
print(result_list)
'''


# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов.

# K – может быть как положительным так и отрицательным числом.


'''
n = [1, 2, 3, 4, 5, 6, 7]
print(n)
step = int(input('введи количество сдвигов > '))
for i in range(abs(step)):
    if step > 0:
        n.insert(0, n.pop(len(n) - 1))
        message = "вправо"
    elif step < 0:
        n.insert(len(n) - 1, n.pop(0))
        message = "влево"
print(f'смещение {message} на {abs(step)} знаков\n{n}')
'''


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#         {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит


'''
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
mas = set()
print(data)
for i in range(len(data)):
	for k in data[i]:
		mas.add(data[i][k])
print(mas)


l = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
     {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
startValues = list()
unicueValues = set()
for i in l:
    for (k, m) in i.items():
        startValues.append(m)
        unicueValues.add(m)
print(f'исходные значения словаря:\n{startValues}\n')
print(f'уникальные значения словаря:\n{unicueValues}\n')


data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
        {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
values = set()
for i in data:
    for key in i:
        values.add(i[key])
print(values)


data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
        {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
values = set()
for i in data:
    values.add(list(i.values())[0])
print(values)
'''


# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших
# предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.


'''
from random import randint

# massive = [int(i) for i in input("Введите числа: ").split()]
length = 15
massive = [randint(-10, 10) for i in range(length)]
print(massive)
count = 0
for i in range(1, length):
    if massive[i - 1] < massive[i]:
        count += 1
print(count)
'''

# Домашняя задача 3го семинара
'''
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
'''

'''

k = int(input())
m = abs(k - list_1[0])  # модуль разности
numbers = []  # список для хранения чисел

for i in range(len(list_1)):
    if abs(list_1[i] - k) <= m:
        if abs(list_1[i] - k) < m:
            numbers = []  # очищаем список, если нашли число ближайшее, чем предыдущее
            m = abs(list_1[i] - k)
        numbers.append(list_1[i])
'''


'''
dict_1 = {'AEIOULNSTRАВЕИНОРСТ': 1, 'DGДКЛМПУ': 2, 'BCMPБГЁЬЯ': 3, 'FHVWYЙЫ': 4, 'KЖЗХЦЧ': 5, 'JXШЭЮ': 8, 'QZФЩЪ': 10} 
word = list(input('Введите слово буквами верхнего регистра: '))
price = 0
for i in word:
    for key in dict_1:
        if i in key:
            price = price + dict_1.get(key)
print(f'Стоимость слова: {price}.')
'''

'''
onePoints = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
twoPoints = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
threePoints = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я' ], 3)
fourPoints = dict.fromkeys(['Й', 'Ы'], 4)
fivePoints = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
eightPoints = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
tenPoints = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
mergedDict = onePoints | twoPoints | threePoints | fourPoints | fivePoints | eightPoints | tenPoints 

userText = list(input("Введите одно слово ").upper())
sum = 0
for i in userText:
    sum += mergedDict[i]
print(sum)
'''


# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


'''
myList = 'a a a b c a a d c d d'.split()
# myList = [i for i in input('> ').split()]
resultList = list()
for item in myList:
    count = 1
    flag = True
    while flag:
        if item not in resultList:
            resultList.append(item)
            flag = False
        else:
            item = item[0] + '_' + str(count)
            count += 1 
    print(item, end=', ')


word = input("Введите строку: ").split()
result = {}
for i in word:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
        result[i] += 1
    else:
        print(i, end=' ')
        result[i] = 1
'''


'''
s = input()  # читаем строку с входа
count = {}  # создаем пустой словарь для подсчета количества повторов символов
for c in s:
    if c in count:
        count[c] += 1  # увеличиваем количество повторов для уже встреченного символа
        s = s.replace(c, c + '_' + str(count[c]), 1)  # добавляем постфикс к символу
    else:
        count[c] = 1  # начинаем счёт для символа
print(s)  # выводим измененную строку с постфиксами
'''


'''
stroka = input().split()
result = {}
for i in stroka:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
    result[i] = result.get(i, 0) + 1
'''


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

'''
text1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure."
text2 = " So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
text = text1 + text2
res = {item.lower() for item in text.split(' ')}
print(len(res))
'''


# На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень",
# "ножницы", "бумага", "ящерица" или "Спок". На первой строке записан выбор Тимура, на второй –
# выбор Руслана.

# Формат выходных данных
# Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

# Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень.
# Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает ножницы, которые,
# в свою очередь, отрезают голову ящерице, которая ест бумагу, на которой улики против Спока.
# Спок испаряет камень, а камень, разумеется, затупляет ножницы.

# a=input()
# b=input()
# m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
#         'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
#         'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
#         'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
#         'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
#         'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
#         'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
#         'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
#         'Спок-ящерица': 'Руслан'}
'''
a=input()
b=input()
m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
        'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
        'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
        'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
        'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
        'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
        'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
        'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
        'Спок-ящерица': 'Руслан'}
key = a + "-" + b
print(key)
print(m[key])
'''


