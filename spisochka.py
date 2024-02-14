spisok = open("kot.txt","r", encoding ="utf-8")
spisok1 = open("kot2.txt","r", encoding ="utf-8")
itog = open("itog.txt","r", encoding ="utf-8")
str1 = spisok.readline().strip()
print(str1)
str2 = spisok.readline().strip()
print(str2)
str3 = spisok.readline().strip()
print(str3)
str4 = spisok.readline().strip()
print(str4)
spisok.close()



spisok1 = open("kot.txt","r", encoding ="utf-8")
str5 = spisok1.readline().strip()
str6 = spisok1.readline().strip()

str7 = spisok1.readline().strip()

str8 = spisok1.readline().strip()

spisok1.close()



spisok2 = open("kot2.txt","r", encoding ="utf-8")
str1 = spisok2.readline().strip()

str2 = spisok2.readline().strip()

str3 = spisok2.readline().strip()

str4 = spisok2.readline().strip()

spisok2.close()
spisok2 = open("itogi.txt","w", encoding ="utf-8")
spisok2.write(str5 + str1+ "\n")
spisok2.write(str6 + str2+ "\n")
spisok2.write(str7 + str3+ "\n")
spisok2.write(str8 + str4+ "\n")
spisok2.close()