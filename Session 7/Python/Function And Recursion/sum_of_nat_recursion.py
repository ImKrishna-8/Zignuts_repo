def sum_of_natural(n):
    if(n==0):
        return 0
    else: 
       return n+sum_of_natural(n-1)
    
n= int(input("Enter number: "))
print(sum_of_natural(n))