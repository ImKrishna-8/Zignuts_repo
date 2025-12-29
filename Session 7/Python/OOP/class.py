class Employee:
    def __init__(self):
        print("Im making a object right now")
    
    language="Python"
    salary=10000

    def getinfo(self):
        print(self.name , self.language)

harry = Employee()
harry.name = "haryy bhai "
harry.getinfo()
Employee.getinfo(harry)
