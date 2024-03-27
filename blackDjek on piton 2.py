import random

print("Это что-то похожее на игру блек джек.Правила: набрал больше 20 баллов- проиграл. И так,\n ваш баланс:")
bal1=random.randint(1,8)
balans1=5
bal2=random.randint(1,8)
balans2=5
print("ход первого игрока,его счёт:",balans1)
vr=input("первый игрок,выберите действие:взять,перестать")
if vr=="взять" or vr=="Взять" or vr=="dpznm" or vr=="Dpznm":
    balans1=bal1 + balans1
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку его счёт:",balans2)
vr2=input("второй игрок,выберите действие:взять,перестать")
if vr2=="взять" or vr2=="Взять" or vr2=="dpznm" or vr2=="Dpznm":
    balans2=bal2 + balans2
    print("ваш кольчество баллов :",balans2)
if vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans2)
    
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm" and vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    if balans1>balans2 or balans2 > 20 :
        print("победу одержал первый игрок,поздравляем!")
    if balans1<balans2 or balans1 > 20 :
        print("победу одержал второй игрок,поздравляем!))")
    if balans1==balans2 or balans1 > 20 and balans2 > 20 :
        print("ничья.... Хах,ну переиграйте если хотите))))")
        exit()
print("ход первого игрока,его счёт:",balans1)
vr=input("первый игрок,выберите действие:взять,перестать")
if vr=="взять" or vr=="Взять" or vr=="dpznm" or vr=="Dpznm":
    balans1=bal1 + balans1
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку его счёт:",balans2)
vr2=input("второй игрок,выберите действие:взять,перестать")
if vr2=="взять" or vr2=="Взять" or vr2=="dpznm" or vr2=="Dpznm":
    balans2=bal2 + balans2
    print("ваш кольчество баллов :",balans2)
if vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans2)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm" and vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    if balans1>balans2 or balans2 > 20 :
        print("победу одержал первый игрок,поздравляем!")
    if balans1<balans2 or balans1 > 20 :
        print("победу одержал второй игрок,поздравляем!))")
    if balans1==balans2 or balans1 > 20 and balans2 > 20 :
        print("ничья.... Хах,ну переиграйте если хотите))))")
        exit()
print("ход первого игрока,его счёт:",balans1)
vr=input("первый игрок,выберите действие:взять,перестать")
if vr=="взять" or vr=="Взять" or vr=="dpznm" or vr=="Dpznm":
    balans1=bal1 + balans1
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку его счёт:",balans2)
vr2=input("второй игрок,выберите действие:взять,перестать")
if vr2=="взять" or vr2=="Взять" or vr2=="dpznm" or vr2=="Dpznm":
    balans2=bal2 + balans2
    print("ваш кольчество баллов :",balans2)
if vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans2)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm" and vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    if balans1>balans2 or balans2 > 20 :
        print("победу одержал первый игрок,поздравляем!")
    if balans1<balans2 or balans1 > 20 :
        print("победу одержал второй игрок,поздравляем!))")
    if balans1==balans2 or balans1 > 20 and balans2 > 20 :
        print("ничья.... Хах,ну переиграйте если хотите))))")
        exit()
print("ход первого игрока,его счёт:",balans1)
vr=input("первый игрок,выберите действие:взять,перестать")
if vr=="взять" or vr=="Взять" or vr=="dpznm" or vr=="Dpznm":
    balans1=bal1 + balans1
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку его счёт:",balans2)
vr2=input("второй игрок,выберите действие:взять,перестать")
if vr2=="взять" or vr2=="Взять" or vr2=="dpznm" or vr2=="Dpznm":
    balans2=bal2 + balans2
    print("ваш кольчество баллов :",balans2)
if vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans2)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm" and vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    if balans1>balans2 or balans2 > 20 :
        print("победу одержал первый игрок,поздравляем!")
    if balans1<balans2 or balans1 > 20 :
        print("победу одержал второй игрок,поздравляем!))")
    if balans1==balans2 or balans1 > 20 and balans2 > 20 :
        print("ничья.... Хах,ну переиграйте если хотите))))")
        exit()
print("ход первого игрока,его счёт:",balans1)
vr=input("первый игрок,выберите действие:взять,перестать")
if vr=="взять" or vr=="Взять" or vr=="dpznm" or vr=="Dpznm":
    balans1=bal1 + balans1
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку его счёт:",balans2)
vr2=input("второй игрок,выберите действие:взять,перестать")
if vr2=="взять" or vr2=="Взять" or vr2=="dpznm" or vr2=="Dpznm":
    balans2=bal2 + balans2
    print("ваш кольчество баллов :",balans2)
if vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans2)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm" and vr2=="перестать" or vr2=="Перестать" or vr2=="gthtcnfnm" or vr2=="Gthtcnfnm":
    if balans1>balans2 or balans2 > 20 :
        print("победу одержал первый игрок,поздравляем!")
    if balans1<balans2 or balans1 > 20 :
        print("победу одержал второй игрок,поздравляем!))")
    if balans1==balans2 or balans1 > 20 and balans2 > 20 :
        print("ничья.... Хах,ну переиграйте если хотите))))")
        exit()
    
    
    


 