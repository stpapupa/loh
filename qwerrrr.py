import pyautogui

a=input("логин")
b=input("пароль")
if a=="12345":
    print("логин верный")
elif b=="55555":
    print("пароль верный")
elif a!="12345":
    print("логин neверный")
elif b!="55555":
    print("пароль neверный")
else:
    print("я гусь")
if a=="12345" and b=="55555":
    pyautogui.alert(text="!!!секретные файлы!!!", title="секрет кавасаки", button="смотреть")