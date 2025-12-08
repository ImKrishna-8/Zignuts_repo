num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
operator = input("Enter operator(only +,-,*,/):")


if(operator == "+"):
    print(f"addtion of {num1} + {num2} = {num1+num2}")
elif(operator == "-"):
    print(f"substraction of {num1} - {num2} = {num1-num2}")
elif(operator == "*"):
    print(f"multiplication of {num1} x {num2} = {num1*num2}")
elif(operator == "/"):
    print(f"division of {num1} / {num2} = {num1/num2}")
else:
    print("you entred wrong operator!")