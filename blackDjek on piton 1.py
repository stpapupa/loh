import random
import pyautogui

print("привет,это мой первый серьёзный проект.Это что-то похожее на игру блек джек.Правила: набрал больше 20 баллов- проиграл")
bal1=random.randint(1,8)
balans1=random.randint(4,12)
bal2=random.randint(1,8)
balans2=random.randint(4,12)



pyautogui.confirm(text='выберите действие', title='окно выбора действия', buttons=['взять', 'перестать'])
if button == "взять":
    print(bal1 + balans1)