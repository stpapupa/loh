import os
cmd=input("введите команду")
if cmd ==("помощь"):
    print("анекдот(рассказывает анекдот), сказка,новость,дела,заметка(спросить небольшой текст и заменить в файле с заметками),контакт(ФИО + номер телефона) в файл с контактами,браузер,блокнот, показать весёлое фото")
elif cmd ==("анекдот"):
    print("негр увидел чёрный свет в конце тонеля")

elif cmd ==("сказка"):
    print("жили были взяли сдохли")
elif cmd ==("новость"):
    print("сегодня был устроен массовый генацыд в школе")
elif cmd ==("дела"):
    os.startfile("dela.txt")
elif cmd ==("заметка"):
    izmzam=input("текст для изменения файла")
    zam= open("zam.txt","w", encoding ="utf-8")
    zam.write(izmzam)
    zam.close()
elif cmd ==("контакт"):
    izmcont=input("текст для изменения файла")
    cont= open("cont.txt","w", encoding ="utf-8")
    cont.write(izmcont)
    cont.close()
elif cmd ==("браузер"):
    os.startfile("google")
elif cmd ==("блокнот"):
    os.startfile("bloknot.txt")
elif cmd ==("фото"):
    os.startfile("kkk.jpg")