spisok=[]
item=""
while item !="stop":
    item=input("Введите , пожалуйста , вещь которую вы хотите купить (наберите 'stop' , когда захотите завершить покупки): ")
    if item=="stop":
        break
    spisok.append(item)

spisok=sorted(spisok)

for x in range(len(spisok)):
    print(f"{x+1}.", spisok[x])


