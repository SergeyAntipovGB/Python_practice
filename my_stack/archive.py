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
dict_1 = {'AEIOULNSTRАВЕИНОРСТ': 1, 'DGДКЛМПУ': 2, 'BCMPБГЁЬЯ': 3, 'FHVWYЙЫ': 4, 'KЖЗХЦЧ': 5, 'JXШЭЮ': 8, 'QZФЩЪ': 10} 
word = list(input('Введите слово буквами верхнего регистра: '))
price = 0
for i in word:
    for key in dict_1:
        if i in key:
            price = price + dict_1.get(key)
print(f'Стоимость слова: {price}.')
'''


'''               #  Делает каждую букву отдельным ключем
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


'''~~~~~~~~~~~~~~~~~~~~ С е м и н а р  5 ~~~~~~~~~~~~~~~~~~~~'''


'''
Задача 31
Последовательностью Фибоначчи называется последовательность чисел a0, a1,
..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21

Задание необходимо решать через рекурсию
'''


# def fib(count):
#     if count == 0:
#         return 0
#     elif count == 1:
#         return 1
#     return fib(count-2) + fib(count-1)

# n = int(input('Введи натуральное число N = '))
# print(f'{n}-ое число Фибоначчи равно {fib(n)}')


'''
Задача 33
Хакер Василий получил доступ к классному журналу и хочет заменить
все свои минимальные оценки на максимальные. Напишите программу,
которая заменяет оценки Василия, но наоборот: все максимальные –
на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''


# def zamena(oneList):
#     maximal = max(oneList)
#     minimal = min(oneList)
#     for item in range(len(oneList)):
#         if oneList[item] == maximal:
#             oneList[item] = minimal
#     return oneList

# spisok = [1, 3, 3, 3, 4]
# print(zamena(spisok))


'''
Задача 35:
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

Input: 5
Output: yes
'''


# def simple(num):
#     for item in range(2, num // 2):
#         if num % item == 0: return False
#     return True

# n = int(input('введи целое число N = '))
# f = simple(n)
# if f: print('простое число')
# else: print('не простое число')


# def simple(num):           # решение с помощью рекурсии
#     if num == 1: return 'Простое'
#     elif n % (num) == 0: return 'Не простое'
#     return simple(num - 1)

# n = 11
# print(simple(n // 2))


'''
Задача 37:
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать
циклы (даже для ввода и вывода).

Input:    2 -> 3 4
Output: 4 3
'''


# def invert(count = 1):
# 	if count > n: return ''
# 	k = input(f'введи {count}-й элемент > ')
# 	return invert(count + 1) + ' ' + k

# n = 4
# print(invert())


'''
Проверка слова на палиндром
'''


# def pal(word):
#     if len(word) == 0: return ''
#     c = word.pop(0)
#     return pal(word) + c

# word = 'око'
# text = [item for item in word]
# if word == pal(text): print(f'слово {word} - палиндром')
# else: print(f'слово {word} - не палиндром')


# def pal(text):
#     if text == '': return ''
#     return text[-1] + pal(text[:-1])

# word = 'локон'
# if word == pal(word): print(f'слово {word} - палиндром')
# else: print(f'слово {word} - не палиндром')


# def is_palindrome(word):  
#     if word == word[::-1]:
#         return 'yes'
#     return 'no'
# print(is_palindrome("ollo"))


'''~~~~~~~~~~~~~~~~~~~~ С е м и н а р  6 ~~~~~~~~~~~~~~~~~~~~'''


'''
Дан массив, состоящий из целых чисел. Напишите программу, которая
в данном массиве определит количество элементов, у которых два соседних
и, при этом, оба соседних элемента меньше данного. Сначала вводится число
N — количество элементов в массиве Далее записаны N чисел — элементы массива.
Массив состоит из целых чисел.
Ввод: Ввод:
55
1 2 3 4 5 15151
Вывод: Вывод:
02
'''


# def fun(pos, count = 0):
#     if pos == 0: return count
#     if a[pos - 1] < a[pos] > a[pos + 1]: count += 1
#     return fun (pos - 1, count)

# a = [5, 12, 9, 8, 12, 9, 11, 3]
# n = len(a)
# print(fun(n - 2))


'''
Задача No45. Решение в группах
Два различных натуральных числа n и m называются дружественными,
если сумма делителей числа n (включая 1, но исключая само n) равна
числу m и наоборот. Например, 220 и 284 – дружественные числа. По
данному числу k выведите все пары дружественных чисел, каждое из
которых не превосходит k. Программа получает на вход одно натуральное
число k, не превосходящее 105. Программа должна вывести все пары
дружественных чисел, каждое из которых не превосходит k. Пары
необходимо выводить по одной в строке, разделяя пробелами. Каждая
пара должна быть выведена только один раз (перестановка чисел
новую пару не дает).
Ввод: Вывод:
300 220 284
10 минут
'''


# def div(max, count = 0, step = 1):
#     '''
#     Функция возвращает count - количество
#     делителей заданного числа max: [1, max)
#     '''
#     if step == max // 2 + 1: return count
#     if max % step == 0: count += step
#     return div(max, count, step + 1)

# def sum(step1, step2):
#     '''
#     Функция выбирает пары дружественных чисел
#     из заданного промежутка [1, k]
#     '''
#     if step1 == 1: return
#     if step2 == 0: sum(step1 - 1, step1 - 2)
#     else:
#         if div(step1) == div(step2): print(step1, step2)
#         sum(step1, step2 - 1)    
        
# k = 16
# sum(k, k - 1)

# def sum(friends):     # вариант решения вложенными циклами
#     for i in range(k, 1, -1):
#         first = div(i)
#         for j in range(i - 1, 0, -1):
#             second = div(j)
#             if first == second:
#                 print(i, j)
#                 break


# n = int(input())    # не работает !
# list_1 = list()
# for i in range(n):
#     sum = 0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:
#             sum += j
#     list_1.append((i, sum))
# for i in range(len(list_1)):
#     for j in range(i, len(list_1)):
#         if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
#             print(*list_1[i])

'''
1. Дано натуральное число *N* и последовательность из *N* элементов.
Требуется вывести эту последовательность в обратном порядке.

***Примечание.*** В программе запрещается объявлять массивы и
использовать циклы (даже для ввода и вывода).
'''


# def invert(count = 1):
# 	if count > n: return ''
# 	k = input(f'введи {count}-й элемент > ')
# 	return invert(count + 1) + ' ' + k

# n = 4
# print(invert())


'''
Даны два массива чисел. Требуется вывести те элементы первого массива
(в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел
- элементы массива. Затем число M - количество элементов во втором массиве.
Затем элементы второго массива
Ввод: 					Вывод:
7					3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1
'''


# n = [3, 1, 3, 4, 2, 4, 12]
# m = [4, 15, 43, 1, 15, 1]
# for item in range(len(n)):
#     if n[item] in m: n.pop(item)
# print(n)


'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных
друг другу. Считается, что любые два элемента, равные друг другу
образуют одну пару, которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных строках.
Ввод:			Вывод:
1 2 3 2 3			2
'''

# myList = [randint(-10, 11) for item in range(20)]
# print(myList)
# res = dict()
# for item in myList:
#     if item not in res: res[item] = 1
#     else: res[item] += 1
# for (k, v) in res:
#     print(k, v//2)
    

# n = int(input())
# list_1 = [int(i) for i in input().split()][:n]
# count = 0
# result = {}
# for i in list_1:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
# print(sum([i // 2 for i in result.values()]))


'''~~~~~~~~~~~~~~~~~~~~ С е м и н а р  7 ~~~~~~~~~~~~~~~~~~~~'''


'''
Задача 47
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
'''


# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(lambda val: val, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


'''
Задача 49
Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна
'''


# def find_farthest_orbit(orbits):
#     elliptic_orbits = list(filter(lambda item: item[0] != item[1], orbits))
#     areas = list(map(lambda item: item[0] * item[1], elliptic_orbits))
#     return elliptic_orbits[areas.index(max(areas))]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(max(orbits, key=lambda x: (x[0] != x[1])* x[0] * x[1]))


# def maxSquare(orbits, count = 0, max = 0):
#     if count == len(orbits): return tuple(maxr[-1])
#     if orbits[count][0] != orbits[count][1]:
#         s = orbits[count][0] * orbits[count][1]
#         if max < s:
#             max = s
#             maxr.append(orbits[count])
#     return maxSquare(orbits, count + 1, max)

# maxr = list()
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(maxSquare(orbits))


# def find_farthest_orbit(orbits):
#     list_of_elliptical_orbits = [i for i in orbits if i[0] != i[1]]
#     list_of_areas = [i[0] * i[1] for i in list_of_elliptical_orbits]
#     # max_area_index = list_of_areas.index(max(list_of_areas))
#     max_area_index = [i for i in range(len(list_of_areas)) if list_of_areas[i] == max(list_of_areas)]
#     return list_of_elliptical_orbits[max_area_index[0]]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))


'''
Задача 51
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод:							Вывод:
values = [0, 2, 10, 6]				same
if same_by(lambda x: x % 2, values):
	print('same')
else:
	print('different')
'''

# def same_by(characteristic, objects):
#     return len(list(filter(characteristic, objects))) == 0

# values = [0, 2, 10, 6]
# print(same_by(lambda x: x % 2, values))
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


# def same_by(characteristic, objects):
#     return sum(list(map(characteristic, objects))) == 0

# values = [0, 2, 3, 11, 6, 9]
# print(same_by(lambda x: x % 3, values))
# if same_by(lambda x: x % 3, values):
#     print('same')
# else:
#     print('different')


'''
Доп. задача 1.
Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.

 пример  - 8 11 0 -23 140 1 => 11 -23
'''


# list1 = '-8 11 0 -23 140 1'.split()
# print(*list(filter(lambda i: len(str(abs(int(i)))) == 2, list1)))


'''
Доп. задача 2. 
Дан список, вывести отдельно буквы и цифры.

a = ( "a", 'b', '2', '3' ,'c')
b = ( 'a' , 'b' , 'c')
c = ( '1', '2', '3')
'''


# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')
# print(list(filter(lambda x: x in b, a)))
# print(list(filter(lambda x: x in c, a)))


'''
Доп. задача 3.
Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
При решении задачи используйте комбинацию функций filter, map, sum.

Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.
'''


# numbers = [i for i in range(10, 100)]
# print(sum(map(lambda x: x ** 2, filter(lambda x: x % 9 == 0, numbers))))


'''
Задача 36:
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*
**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     print('	'.join([str(i) for i in range(1, num_columns + 1)]))
#     for i in range(2, num_rows + 1):
#         print(i, end=' \t')
#         for j in range(2, num_columns + 1):
#             print(operation(i, j), end=' \t')
#         print()

# print_operation_table(lambda x, y: x * y)


# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for x in range(1, num_rows + 1):
#         print(*list(map(operation, [1] * x, range(1, num_columns + 1))))

# print_operation_table(lambda x, y: x * y)


'''~~~~~~~~~~~~~~~~~~~~ C е м и н а р  8 ~~~~~~~~~~~~~~~'''


'''
Задача No49.
Решение в группах Создать телефонный справочник с возможностью импорта и
экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона -
данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''


# def show_menu():
#     os.system('clear')
#     print("\nВыберите необходимое действие:\n"
#           "1. Вывести справочник на экран\n"
#           "2. Сохранить справочник в текстовом файле\n"
#           "3. Найти абонента по фамилии\n"
#           "4. Найти абонента по имени\n"
#           "5. Завершить работу программы\n")
#     choice = int(input('> '))
#     return choice

# def go_to_function(variant):
#     while (variant != 5):
#         if variant == 1:         # Вывести справочник на экран
#             for line in read_from_txt(filename):
#                 print(*line, end='')
#                 pause()
#         elif variant == 2:       # Сохранить справочник в текстовом файле
#             write_to_txt(filename, abon_list)
#             print('\nфайл сохранён !', end='')
#             pause()
#         elif variant == 3:       # Найти абонента по фамилии
#             finder = input_finder('введите фамилию абонента')
#             find_abonent(filename, finder)
#             pause()              
#         elif variant == 4:       # Найти абонента по имени
#             finder = input_finder('введите имя абонента')
#             find_abonent(filename, finder)
#             pause()
#         variant = show_menu()

# def read_from_txt(filename):         # Чтение файла txt в список
#     phone_list = [fields]
#     with open(filename, 'r', encoding='utf-8') as file:
#         # phone_list.append(fields)
#         for line in file:
#             phone_list.append(line.split(','))
#     return phone_list

# def write_to_txt(filename, phone_dict):        # Запись списка в файл txt
#     with open(filename, 'w', encoding='utf-8') as file:
#         for line in phone_dict:
#             word = ''
#             for w in line:
#                 word += str(w) + ','
#             file.write(f'{word[:-1]}\n')

# def input_finder(message):              # Запрос параметра для поиска
#     answer = input(f'\n{message} > ').title()
#     print('\n')
#     return answer

# def pause():
#     input('\nнажмите Enter для продолжения...')

# def find_abonent(filename, find_param):
#     phone_list = read_from_txt(filename)
#     find_list = []
#     for line in phone_list:
#         if find_param in line:
#             find_list.append(line)
#     if len(find_list) == 0: print('нет данных!')
#     else: 
#         find_list.insert(0, fields)
#         for line in find_list:
#             print(*line, end='')

# filename = './my_stack/phone.txt'
# fields = ["Фамилия", "Имя", "Отчество", "Телефон\n\n"]
# abon_list = [
#     ['Пушкин','Александр','Сергеевич',999],
#     ['Есенин','Сергей','Александрович',123]
# ]
# go_to_function(show_menu())



