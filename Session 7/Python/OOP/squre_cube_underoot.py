class calculation:
    
    @staticmethod
    def square(n):
        return n*n
    
    @staticmethod
    def cube(n):
        return n*n*n
    
    def underoot(n):
        return n**0.5
    
n = int(input("Enter Number: "))
print(calculation.square(n))
print(calculation.cube(n))
print(calculation.underoot(n))
