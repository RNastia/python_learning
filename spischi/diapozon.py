number1=input("Введите пожалуйста число которое будет началом диапазона : ")
while not number1.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{number1}' ")
    number1=input("Введите еще раз которое будет началом диапазона : ")


number2=input("Введите число которое будет концом диапазона : ")
while not number2.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{number2}' ")
    number2=input("Введите еще раз число которое будет концом диапазона : ")

number1=int(number1)
number2=int(number2)

# Тут два способа один с вводом новой переменной , другой без нее

if number1>number2:

    #temp=number1
    #number1=number2
    #number2=temp

    number1=number1+number2
    number2=number1-number2
    number1=number1-number2

for x in range(int(number1),int(number2)+1):
    if x % 2 == 1:
        print(x)
