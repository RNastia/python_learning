spisok=[]
print("Вводите по одной стране в которой вы были когда захотите пойти дальше напишите 'stop'")
while True:
    countries=input("Введите страну в которой вы были : ")

    if countries=="stop":
     break
    spisok.append(countries)

print(" ")
print("1. Просмотреть посещенные города ")
print("2. Удалить город из списка ")
print("3. Добавить в список новый посещенный город ")
print("4. Изменить имя посещенного города ")
print("5. Закончить действие ")
print(" ")

while True:
    cito=input("Теперь выберите цифру соотвецтвующую тому что вы хотите сделать : ")

    if cito=="1" or cito=="1.":
        for x in range(len(spisok)):
            print(f"{x+1}.", spisok[x])

    elif cito=="2" or cito=="2.":
        for x in range(len(spisok)):
            print(f"{x+1}.", spisok[x])
        change=input("Какую страну вы хотите удалить (введите ее номер) : ")   
        if change=="1" or change=="1.":
         del spisok[0]
        elif change=="2" or change=="2.":
         del spisok[1]
        elif change=="3" or change=="3.":
         del spisok[2]
        print(" ")
        print("Cтрана удалена")
        print("")
    
    elif cito=="3" or cito=="3.":
       new=input("Введите страну , которую вы хотите добавить в список : ")
       spisok.append(new)

       print("")
       print("Страна успешно добавлена")
       print("")


