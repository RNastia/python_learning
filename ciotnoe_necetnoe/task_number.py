print("Мы рады видеть вас , данная программа проверяет число которое вы введете на четность или же нечетность\n")

name=input("Введите пожалуйста ваше имя что бы далее мы могли обращаться к вам по нему : ")
while len(name)<=2:
    name=input("Ваше имя содержит слишком мало символов , введите его еще раз пожалуйста : ")

number=input(f"{name} пожалуйста введите число которое вы хотите проверить : ")
while not number.isdigit():
    print(f"Упс {name}, вы ввели не число, а то что вы ввели это '{number}'")
    number=input("Введите еще раз ваше число :")

# сдесь смотрится четное число или нет исходя из остатка если его нет (= 0) то число четное а если он =1 число нечетное

while True:
 number=int(number)
 if number % 2 == 1:
    print(f"Ваше число {number} нечетное (Odd number)")
 else:
    print(f"Ваше число {number} четное (Even number)")
 number=input("Может вы хотите проверить еще какое либо число если да то введите его если нет то введите 'нет' : ")

 if number=="нет":
    break

 while not number.isdigit():
    print(f"Упс {name}, вы ввели не число, а то что вы ввели это '{number}'")
    number=input("Введите еще раз ваше число :")