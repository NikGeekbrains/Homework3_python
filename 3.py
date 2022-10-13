# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def SummaNaNechetnychPoz():
    spisok_1 = [1, 5, 6, -9, 0, 12, 16, 3]  
    summa = 0
    for i in range(len(spisok_1)):
        if i % 2 == 1:
            summa += spisok_1[i]      
    print(f'Сумма элементов на нечетных позициях: {summa}')
                
# SummaNaNechetnychPoz()

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def ProizvedeniePar():
    spisok_1 = [1, 5, 6, -9, 0, 12, 16, 3]  
    spisok_2 = []
    for i in range(int(len(spisok_1) / 2)):
        spisok_2.append(spisok_1[i] * spisok_1[len(spisok_1) - 1 - i])
    print(f'Произведение пар чисел списка: {spisok_2}')

# ProizvedeniePar()

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def MaxMinDrobnoiChasti():
    spisok_1 = [1.3, 5, 6.04, -9.12, 0.56, 12.2, 16.03, 3]  
    spisok_2 = []
    for i in range(int(len(spisok_1))):
        if spisok_1[i] % 1 != 0:
            spisok_2.append(abs(spisok_1[i]) % 1)
    max(spisok_2) % 1
    min(spisok_2) % 1
    Raznitsa = max(spisok_2) % 1 - min(spisok_2) % 1
    print(f'Разница между максимальным и минимальным значением дробной части элементов: {Raznitsa}')

# MaxMinDrobnoiChasti()

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def Perevod10In2():
    desyatichnoe = int(input('Введите число: '))
    ostatok = []
    while desyatichnoe > 2:
        ostatok.append(int(desyatichnoe % 2))
        desyatichnoe /= 2   
    else:
        ostatok.append(int(desyatichnoe))
    for i in reversed(ostatok):
        print(i, end=' ')

# Perevod10In2()

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def SpisokFibonacci():
    k = int(input('Введите число: '))
    spisok = list(range(k * 2 + 1))
    spisok[k] = 0
    spisok[k - 1] = -1
    spisok[k + 1] = 1
    for i in range(2, k + 1):
	    spisok[k + i] = spisok[k + i - 1] + spisok[k + i - 2]
    for n in range(2, k + 1):
        spisok[k - n] = -spisok[k + n]
    print(spisok)

# SpisokFibonacci()