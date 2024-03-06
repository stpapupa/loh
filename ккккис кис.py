bagag = int(input("скока кг"))
if bagag<25 :
    print("проходите")
elif bagag>25:
    e=input("доплаивац 228р за кг ? да/нет")
    if e ==("да"):
        a=bagag-25
        print("с вас:", a*228)
        print("проходити")
    elif e ==("нет"):
        print("админы сюда кабанчиком")