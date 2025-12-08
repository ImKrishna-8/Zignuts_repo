num = int(input("Enter number: "))
flag=True

for i in range(2,(num//2)+1):
    if((num%i)==0):
        flag=False

if(flag):
    print("prime")
else:
    print("not prime")