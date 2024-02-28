import os
idea=input("идея")
cmd=input("куда идею")
if cmd ==("покупки"):
    pok= open("pok.txt","w", encoding ="utf-8")
    pok.write("- "+idea)
    pok.close()
elif cmd ==("задачи"):
    zad= open("zad.txt","w", encoding ="utf-8")
    zad.write("- "+idea)
    zad.close()
elif cmd ==("идеи"):
    idei= open("idei.txt","w", encoding ="utf-8")
    idei.write("- "+idea)
    idei.close()