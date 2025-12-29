def take_user_input():
    global number_1,  number_2
    while True:
        try:
             number_1 = float(input("Enter First Value : ")) 
             number_2 = float(input("Enter Second Value : "))
             break;
        except:
            print("Invalid Input Try again")



print("WELCOME TO CLI BASED CALCULATOR")

try:
    take_user_input()
except:
    print("invalid input")
    take_user_input()


c=0
while(c!=7):
    print("WHAT YOU WANT TO PERFORM")
    print("-------------------------------")
    print("| 1. Addition                 |")
    print("| 2. Substraction             |")
    print("| 3. Multiplication           |")
    print("| 4. division                 |")
    print("| 5. Power(base,power)        |")
    print("| 6. new Values               |")
    print("| 7. Exit                     |")
    print("-------------------------------")
    c = int(input("Enter Your choice: "))
    if(c==6):
        take_user_input()
        continue

    if(c==1):
        print(f"{number_1} + {number_2} = {number_1+number_2}")
    elif(c==2):
        print(f"{number_1} - {number_2} = {number_1-number_2}")
    elif(c==3):
        print(f"{number_1} * {number_2} = {number_1*number_2}")
    elif(c==4):
        print(f"{number_1} / {number_2} = {number_1/number_2}")
    elif(c==5):
        print(f"{number_1}^{number_2} = {number_1 ** number_2}")
    elif(c==7): 
        print("Thank you")
    else:
        print("Wrong input please Try again!! ")



