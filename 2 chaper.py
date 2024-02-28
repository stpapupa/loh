import pyautogui
import os
spisok = open("hleb.txt","r")
str1 = spisok.readline().strip()
spisok.close()
if str1==("тревога"):
    os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("nomer durki")