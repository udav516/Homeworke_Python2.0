# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3]
print(f'{my_list} -> {(sum(my_list[1::2]))}')

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

N = int(input("Enter array size:"))
numbers = []
result = []
for i in range(N):
    numbers.append(random.randint(-N, N))
for i in range((len(numbers) + 1)//2):
    result.append(numbers[i] * numbers[N - 1 - i])
print(f'{numbers} => {result}')

# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

array = [1.1, 1.2, 3.1, 5, 10.01]
newArray = [round(i % 1, 2) for i in array if i % 1 != 0]
print(f'{array} => {max(newArray) - min(newArray)}')

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Enter number:'))
print(f'{number} -> {bin(number)[2:]}')

# Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input("Inset k: "))

fibonacciList = [0]*(k*2+1)
fibonacciList[k] = 0
fibonacciList[k+1] = 1

for i in range(k+2, len(fibonacciList)):
    fibonacciList[i] = fibonacciList[i-2]+fibonacciList[i-1]
for i in range(k, -1, -1):
    fibonacciList[i] = fibonacciList[i+2]-fibonacciList[i+1]
print(fibonacciList)
