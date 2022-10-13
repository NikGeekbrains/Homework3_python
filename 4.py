def SpisokFibonacci():
    k = int(input('Введите число: '))
    fibonacci = 0
    spisok = list(range(k * 2 + 1))
    spisok[k] = 0
    for i in range(0, k):
	    fibonacci += i + 1
        elem_1 = k + i
        elem_2 = k - i
	    spisok.pop(elem_1)
	    spisok.insert(k + i, fibonacci)
	    spisok.pop(elem_2)
	    spisok.insert(k - i, -fibonacci)
    print(spisok)