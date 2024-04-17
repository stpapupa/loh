import random
import time
print("Это что-то похожее на игру блек джек.Правила: набрал больше 20 баллов- проиграл. И так,\n ваш баланс:")
bal1=random.randint(3,6)
balans1=5
karta=" "
bal2=random.randint(3,6)
balans2=5
print("ход первого игрока,его счёт:",balans1)
vr=input("первый игрок,выберите действие:взять,перестать")
if vr=="взять" or vr=="Взять" or vr=="dpznm" or vr=="Dpznm":
    if bal1 == 3 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки волета")
    if bal1 == 4 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки даму :)")
    if bal1 == 5 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки короля -_-")
    if bal1 == 6 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки туз!")
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку то есть боту,подождите немного пожалуйста")
time.sleep(3)
balans2=bal2 + balans2    
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    if balans1>balans2 or balans2 > 20 :
        print("победу одержал первый игрок,поздравляем!")
    if balans1<balans2 or balans1 > 20 :
        print("победу одержал второй игрок,поздравляем!))")
    if balans1==balans2 or balans1 > 20 and balans2 > 20 :
        print("ничья.... Хах,ну переиграйте если хотите))))")
    if balans1>20 and balans2>20:
        print("у игроков количество балов больше 20 и оба игрока(игрока с ботом) проиграли")
    exit()
print("ход первого игрока,его счёт:",balans1)
vr=input("первый игрок,выберите действие:взять,перестать")
if vr=="взять" or vr=="Взять" or vr=="dpznm" or vr=="Dpznm":
    if bal1 == 3 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки волета")
    if bal1 == 4 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки даму :)")
    if bal1 == 5 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки короля -_-")
    if bal1 == 6 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки туз!")
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку то есть боту,подождите немного пожалуйста")
time.sleep(3)
balans2=bal2 + balans2    
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
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
    if bal1 == 3 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки волета")
    if bal1 == 4 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки даму :)")
    if bal1 == 5 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки короля -_-")
    if bal1 == 6 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки туз!")
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку то есть боту,подождите немного пожалуйста")
time.sleep(3)
balans2=bal2 + balans2    
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
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
    if bal1 == 3 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки волета")
    if bal1 == 4 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки даму :)")
    if bal1 == 5 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки короля -_-")
    if bal1 == 6 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки туз!")
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку то есть боту,подождите немного пожалуйста")
time.sleep(3)
balans2=bal2 + balans2    
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
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
    if bal1 == 3 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки волета")
    if bal1 == 4 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки даму :)")
    if bal1 == 5 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки короля -_-")
    if bal1 == 6 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки туз!")
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку то есть боту,подождите немного пожалуйста")
time.sleep(3)
balans2=bal2 + balans2    
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
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
    if bal1 == 3 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки волета")
    if bal1 == 4 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки даму :)")
    if bal1 == 5 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки короля -_-")
    if bal1 == 6 :
        balans1=bal1 + balans1
        print("ваш кольчество баллов :",balans1 , "вы получили на руки туз!")
    print("ваш кольчество баллов :",balans1)
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    print("вы перестали набирать карты ваш баланс:",balans1)
print("ход перешел ко второму игроку то есть боту,подождите немного пожалуйста")
time.sleep(3)
balans2=bal2 + balans2    
if vr=="перестать" or vr=="Перестать" or vr=="gthtcnfnm" or vr=="Gthtcnfnm":
    if balans1>balans2 or balans2 > 20 :
        print("победу одержал первый игрок,поздравляем!")
    if balans1<balans2 or balans1 > 20 :
        print("победу одержал второй игрок,поздравляем!))")
    if balans1==balans2 or balans1 > 20 and balans2 > 20 :
        print("ничья.... Хах,ну переиграйте если хотите))))")
    exit()