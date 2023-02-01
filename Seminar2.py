# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2
import random

counts = int(input('Введите количество монеток: '))
print(counts, end=' -> ')
tails = 0
eagle = 0
for _ in range(counts):
    side = int(random.randint(0, 1))
    print(side, end=' ')
    if side == 0:
        tails += 1
    else:
        eagle += 1
print()
if tails < eagle:
    print(tails)
else:
    print(eagle)

# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

summa = int(input("Введите сумму чисел: "))
product = int(input("Введите произведение чисел: "))
x = (summa-int((summa**2-4*product)**0.5))//2
y = (summa+int((summa**2-4*product)**0.5))//2
print(f'{summa} {product} -> {x} {y}')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input('Введите число: '))
degree = 1
print(number, end=' -> ')
for _ in range(number):
    if degree < number / 2:
        degree = 2**_
        print(degree,  end=' ')

# пользователь будет вводить каждое число на новой строке для задач 10, 12.
