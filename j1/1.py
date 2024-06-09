num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))


# if num1 > num2:
#     if num2 > num3:
#         print("the biggest number is num1")
# elif num2  >num1:
#     if num2 > num3:
#         print("the biggest number is num2")
# elif num3 > num1:
#     if num3 > num2:
#         print("the biggest number is num3")

if num1 < num2 and num2 < num3:
    print(f"the smallest number is {num1}")
elif num2 < num1 and num2 < num3:
    print(f"the smallest number is {num2}")
elif num3 < num1 and num3 < num2:
    print(f"the smallest number is {num3}")



if num1 > num2 and num1 > num3:
    print("the biggest number is num1")
elif num2 > num1 and num2 > num3:
    print("the biggest number is num2")
elif num3 > num1 and num3 > num2:
    print("the biggest number is num3")