import pyautogui
bagag = open('bagaj.txt', 'r', encoding="utf-8")
ves= bagag.readline().strip()
ves=int(ves)
if ves<10 :
    pyautogui.alert(text="вес проходит стандарт проходите на борт", title="сервис", button="класс")
else:
    pyautogui.alert(text="вес багажа слишком высокий", title="сервис", button="тогда выложу труп от туда")
print("самолёт вылетает через 1 час")
bagag.close()