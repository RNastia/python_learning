name=input("Введите свое имя :")
#name1=list(name)
surname=input("Введите фамилию :")
otcestvo=input("Введите отчество : ")
#otcestvo1=list(otcestvo)

name3=f"{name[0]}.{otcestvo[0]}.{surname}"

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

cito=input(f"{name3} теперь выберите цифру соотвецтвующую тому что вы хотите сделать : ")
while not cito.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{cito}' ")
    cito=input("Введите пожалуйста еще раз цифру : ")

while True:
    
    if cito=="1" or cito=="1.":
        for x in range(len(spisok)):
            print(f"{x+1}.", spisok[x])

    elif cito=="2" or cito=="2.":

        for x in range(len(spisok)):
            print(f"{x+1}.", spisok[x])
        change=input(f"{name3} какую страну вы хотите удалить (введите ее номер) : ")   
        spisok.pop(int(change)-1)

        print(" ")
        print("Cтрана удалена")
        print("")
    
    elif cito=="3" or cito=="3.":
       new=input(f"{name3} тогда введите страну , которую вы хотите добавить в список : ")
       spisok.append(new)
       print("")
       print("Страна успешно добавлена")
       print("")

    elif cito=="4" or cito=="4.":
        for x in range(len(spisok)):
            print(f"{x+1}.", spisok[x])
        change=input(f"{name3} какое название страны вы хотите изменить (введите ее номер) : ")
        new2=input("Введите новое название страны : ")
        spisok.pop(int(change)-1)
        spisok.insert(int(change)-1,new2)
        #spisok[int(change)-1]=new2

    elif cito=="5" or cito=="5.":
        ex=input(f"{name3} вы точно хотите покинуть программу ? (да / нет) : ")
        if ex=="да":
            exit(0)
        
    cito=input("Если вы хотите произвести еще какие-либо манипуляции то введите цифру соотвецтвубщую действию которое вы хотите выполнить (если нет то введите 'нет') : ")
    if cito=="нет":
        break






