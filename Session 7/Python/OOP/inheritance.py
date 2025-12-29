class Employee: 
    company = "Zignuts"
    def __init__(self):
        print("im 1")
        

    def showdet(self):
        print(f"i am Employee")

    
class coder: 
    def __init__(self):
        print("im 2")

    language = "python"

    def showdet2(self):
        print(f"i am Coderrrrrrrr")


class programmer(coder,Employee):
    company = "ITC"


a = programmer()
a.showdet()
a.showdet2()
print(a.company)



