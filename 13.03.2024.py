
number = int(input("Введите количество участников: "))

if number == 0:
    print("Встреча отменяется")
elif 0 < number and number <10:
    print("Встреча состоится, как запланировано")
else:
    print("Нам нужно помещение побольше")