a = input("Введите команду +, -, *, /")
b = float(input("Введите первое число"))
c = float(input("Введите второе число"))
if a == "+":
    print(b + c)
elif a == "-":
        print(b - c)
elif a == "*":
        print(b * c)
elif a == "/":
    print( b / c)
else:
    print("Ошибка: деление на ноль")