a=int(input("введите сумму"))
if a < 1000:
    print(a)
elif a >= 1000 and a < 5000:
    print(a-a*5/100)
elif a >= 5001 and a < 10000:
    print(a-a*10/100)
