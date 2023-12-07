numbers=input("Введите пожалуйста числа для нахождения их среднего арифметического (через пробел) : ")

num=numbers.split()
print(num)

summa=0
for eliment in num:
    summa=summa + int(eliment)

col=len(num)
srednee=summa/col
print(srednee)


