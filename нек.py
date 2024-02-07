import pyautogui

a=input("логин")
b=input("пароль")

if a=="123" and b=="777":
    pyautogui.alert(text="!!!секретные файлы!!!", title="секрет кавасаки", button="")
else:
    print("логин или пароль не верный")
print("Спасибо, что пользуетесь технологиями Umbrella Corporation!")