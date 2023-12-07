numbers=input("Введите пожалуйста числа для нахождения их среднего арифметического (через пробел) : ")

array=numbers.split()
print(array)

summa=0
for eliment in array:
    summa=summa + int(eliment)

col=len(array)
srednee=summa/col
print(srednee)


