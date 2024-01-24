file = open('negr.txt', 'r')
balance = int(file.readline().strip())
file.close()
print("Ваш боланс:", balance)

deystwee = input("Что вы хотите сделать? закрыть или прибавить или отнять: ")

if deystwee == "закрыть":
    print("Файл закрыт")
elif deystwee == "прибавить":
    tsifra = int(input("Введите сумму для добавления: "))
    balance += tsifra
    file = open('negr.txt', 'w')
    file.write(str(balance))
    file.close()
    print("Баланс обновлен")
elif deystwee == "отнять":
    tsifra = int(input("Введите сумму для вычитания: "))
    balance -= amount
    file = open('negr.txt', 'w')
    file.write(str(balance))
    file.close()
    print("Баланс обновлен")
else:
    print("Некорректный ввод")