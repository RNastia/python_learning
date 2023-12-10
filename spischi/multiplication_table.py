number=input("Введите пожалуйста ваше число : ")

while not number.isdigit():
     print(f"Упс , вы ввели не число, а то что вы ввели это '{number}'")
     number=input("Введите еще раз ваше число : ")

while True:

    until=input("Введите пожалуйста дo какого числа будет идти таблица умножения : ")

    while not until.isdigit():
     print(f"Упс , вы ввели не число, а то что вы ввели это '{until}' ")
     until=input("Введите еще раз до какого числа будет идти ваша таблица умножения : ")

    # Цикл фор

    for x in range(int(until)):
        print(f"{number} * {x+1} = ",int(number)*(x+1))
    number=input("Если вы хотите можете ввести данные еще раз но для других чисел , если да то введите пожалуйста ваше число , если нет наберите нет : ")
    
    if number=="нет":
        break

    while not number.isdigit():
     print(f"Упс , вы ввели не число, а то что вы ввели это '{number}' ")
     number=input("Введите еще раз ваше число : ")

