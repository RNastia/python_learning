spisok1=input("Ведите , пожалуйст , числа через пробел : ")
spisok2=input("Отлично , теперь еще какие-то числа через пробел : ")
array=spisok1.split()
array2=spisok2.split()

spisocek=array+array2
print(sorted(spisocek))

