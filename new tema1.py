a = input("прочитать или изменить?")
if a == "изменить":
    file = open('dota2.txt', 'w', encoding="utf-8")
    zamena = input("Введите новый текст файла: ")
    file.write(zamena)
    file.close()
elif a == "прочитать":
    file=open('dota2.txt', 'r', encoding="utf-8")
    stroka1 = file.readline().strip()
    print("Сейчас текст в файле такой:", stroka1)
    file.close()
else:
    print("Некорректный ввод")