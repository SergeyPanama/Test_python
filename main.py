kol = 0
vsego = 10

otv = input("Какая версия языка сейчас актуальна? ")
if otv.lower() == "Python3".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")

otv = input("Какая кодировка используется в строках? ")
if otv.lower() == "UTF8".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")

otv = input("Сколько значений есть у bool ")
if otv.lower() == "2".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")

otv = input("Можно ли складывать строки? ")
if otv.lower() == "Да".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")

otv = input("Какая функция определяет длину строки? ")
if otv.lower() == "Len".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")

otv = input("Какой метод делает все буквы маленькими? ")
if otv.lower() == ".lower".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")
otv = input("Какой метод делвет все буквы большими? ")
if otv.lower() == ".upper".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")

otv = input("Какой метод делает все слова с большой буквы? ")
if otv.lower() == ".title".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")

otv = input("Будут ли значения (1+1) и ('1'+'1') равны? ")
if otv.lower() == "Нет".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")

otv = input("Можно ли выполнить сложение 1+'1'?")
if otv.lower() == "Нет".lower():
    print(f"Ответ {otv} верен")
    kol = kol + 1
else:
    print("Неверный ответ")
print(kol, " верных ответов из ", vsego)
