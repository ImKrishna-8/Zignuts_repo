n = int(input("Enter a number: "))

print("USING FOR LOOP ")
for i in range(1,11):
    print(f"{n} x {i} = {n*i}");

print("USING FOR WHILE")
i=1
while(i<11):
    print(f"{n} x {i} = {n*i}");
    i+=1


