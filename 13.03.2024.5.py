f = open("data.txt","r")
mode = f.readline().strip()
f.close()
print("Режим сейчас:", mode)
action = input("Переключить тумблер?: ")
if action == "да" or action == "Да": 
    if mode == "обогрев":
        mode = "охлаждение"
        print("Включён режим «охлаждение»")
    if  mode == "охлаждение":
        mode = "обогрев"
        print("Включён режим «обогрев»")
        
    f = open("data.txt","w")
    f.write(action)
    f.close()