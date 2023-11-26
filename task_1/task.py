# books #
books =input("Здравствуйте сколько книг вы прочли?\n")

while not books.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{books}' \n")
    books =input("Введите еще раз сколько книг вы прочли?\n")

# years Books #
yearsBooks = input("За сколько лет вы прочли все эти книги?\n")

while not yearsBooks.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{yearsBooks}' \n")
    yearsBooks =input("Введите еще раз за сколько лет вы прочли эти книги?\n")

# movies #
movies = input("А сколько фильмов вы посмотрели?\n")

while not movies.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{movies}' \n")
    movies =input("Введите еще раз за сколько фильмов вы посмотрели?\n")

# yearsMovies #
yearsMovies = input("За сколько лет вы просмотрели все эти фильмы?\n")
while not yearsMovies.isdigit():
    print(f"Упс , вы ввели не число, а то что вы ввели это '{yearsMovies}' \n")
    yearsMovies =input("Введите еще раз за сколько лет вы просмотрели эти фильмы?\n")

# resultYear #
print("Значит в год вы читаете", int(books)//int(yearsBooks), "книг")
print("Значит в год вы смотрите", int(movies)//int(yearsMovies), "фильмов")
