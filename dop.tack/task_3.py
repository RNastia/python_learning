name=input("Напишите пожалуйста ваше имя ,а так же отчество : ")

# summa
summa=input(f"Здравствуйте {name}, введите пожалуйста сумму которую вы хотите положить в банк : ")
while not summa.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{summa}' \n")
    summa =input("Введите еще раз сумму которую вы хотите положить в банк\n")

#time in months
time=input(f"{name} а сейчас введите на какой период вы хотите сделать вклад (в месяцах): ")
while not time.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{time}' \n")
    time =input("Введите еще раз на какой период вы хотите сделать вклад (в месяцах)?\n")


summa=int(summa)
procent = 5.5
summaProcent = summa * procent / 100

summaMonth = summa
for month in range(int(time)):
    summaMonth += summaProcent
    print(f"В {month+1} месяце сумма: ",summaMonth)

print("------------------------------")
print("Итоговая сумма :", summaMonth)




   
