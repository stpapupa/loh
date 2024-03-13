import random
num = random.randint(1, 6)
hp = 50
volkHp = 20
if num == 1:
    hp = hp - 10
    print("Вам нанесли 10 урона, ваше здоровье", hp, "хп.")
elif num == 2:
    hp == hp - 5
    print("Вам нанесли 5 урона, ваше здоровье", hp, "хп.")
elif num == 3:
    hp = hp - 2
    print("Вам нанесли 2 урона, ваше здоровье", hp, "хп.")
elif num == 4 or num == 5:
    volkHp = volkHp - 5
    print("Вы нанесли волку 5 урона, его здоровье", volkHp, "хп.")
elif num == 6:
    volkHp = volkHp - 10
    print("Вы нанесли волку 10 урона, его здоровье", volkHp, "хп.")