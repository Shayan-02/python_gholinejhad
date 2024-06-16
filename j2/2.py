def sums(a, op, b):
    if op == "+":
        print(a+ b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)

num1 = int(input("enter a: "))
op = input("enter op: ")
num2 = int(input("enter b: "))

sums(num1, op, num2)