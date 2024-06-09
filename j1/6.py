a = float(input("enter a number: "))

if a < 0:
    print("enter a possetive number")
elif a > 0:
    print(int(a))
    if int(a) % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print(int(a))
    print("zero")