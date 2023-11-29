# number #
number=input("Введите число\n")

while not number.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{number}' \n")
    number =input("Введите еще раз ваше число?\n")

# procent #
procent=input("Введите процент который вы хотите вычислить от числа \n")

valid=False
while not valid:   
    if(not procent.isdigit()):
        print(f"Упс , вы ввели не число, а то что вы ввели это '{procent}' \n")
        procent =input("Введите еще раз ваш процент\n")

    elif (int(procent)>100):
        print("Упс , ваш процент больше 100 \n")
        procent =input("Введите еще раз ваш процент\n")

    else:
        valid = True

# result #      
resultChislo = int(number)*int(procent)/100
print("Процент от вашего числа равен ", resultChislo)
