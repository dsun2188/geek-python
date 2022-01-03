# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

words = input("Введите строку из нескольких слов >>> ").split()

for idx, value in enumerate(words, start=1):
    print(f"{idx}. {value[:10]}")
