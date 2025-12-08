
def sum_of_number(n):
    sum=0
    for i in range (n+1):
        sum+=i
    return sum 

n = int(input("Enter Natural Number:"))
print(sum_of_number(n))
