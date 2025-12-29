import mysql.connector as connector

mydb=connector.connect(host="localhost",user="root",password="1234",database="bank")
db_cursor = mydb.cursor();

class Account:
    def __init__(self,name):
        self.name=name
        self.account_no = None

    def find_account(self,account_no):
        db_cursor.execute("SELECT * FROM account WHERE acc_no=%s",(account_no,))
        data = db_cursor.fetchall()
        if(len(data)==0 or data[0][3]==0):
            print("No Account Found! please Check the account No:")
            return 0
        else:
            self.name = data[0][1]
            self.account_no = data[0][0]
            return 1

    def create(self):
        db_cursor.execute("INSERT INTO account(name) VALUES(%s)",(self.name,))
        print("your account Number: ",db_cursor.lastrowid) 
        mydb.commit();
        self.account_no = db_cursor.lastrowid
    
    def withdraw(self,amount):
        db_cursor.execute("UPDATE account SET balance=balance-%s WHERE acc_no=%s",(amount,self.account_no))
        print("Amount Deducted From Your account! New balance:")
        self.check_balance()
    
    def deposite(self,amount):
        db_cursor.execute("UPDATE account SET balance=balance+%s WHERE acc_no=%s",(amount,self.account_no))
        print("Amount added to your account! New balance:")
        self.check_balance()

    def check_balance(self):
        db_cursor.execute("SELECT * FROM account WHERE acc_no = %s",(self.account_no,))
        data=db_cursor.fetchall()
        print("  ------------------------------")
        print(f" |Your balanace :{data[0][2]}  |");
        print("  ------------------------------")

    def deactivate(self,account_no):
        db_cursor.execute("SELECT * FROM account WHERE acc_no=%s",(account_no,))
        data = db_cursor.fetchall()
        if(len(data)==0 or data[0][3]==0):
            print("No Account Found! Or Account Already Deactivated")
        else:
            db_cursor.execute("UPDATE account SET is_active=false WHERE acc_no=%s",(account_no,))
            print("Deactivated Succesfully")

    

def general_menu(acc):
    cc = 0
    while(cc!=4):
        print("-----------------------")
        print("|    ACCOUNT MENU      |")
        print("-----------------------")
        print("|  1.Check balance     |")
        print("|  2.deposite amount   |")
        print("|  3.withdraw amount   |")
        print("|  4.back to Main menu |")
        print("| ---------------------")

        while True:
            try:
                cc = int(input("enter your choice:"))
                break;
            except:
                print("Try Again Wrong Input")
        if(cc==1):
            acc.check_balance()
        elif(cc==2):
            amount=int(input("Enter Amount:"))
            acc.deposite(amount)
        elif(cc==3):
            amount=int(input("Enter Amount:"))
            acc.withdraw(amount)
        elif(cc==4):
            print("going to main menu")
            break
        else:
            print("wrong Input Try Again")


c=0
while(c!=4):
    print("--------------------------------")
    print("           MAIN MENU            ")
    print("--------------------------------")
    print("1.Create Account")
    print("2.Already Have account")
    print("3.deactivate account")
    print("4.exit")
    print("--------------------------------")
    while True:
            try:
                c = int(input("enter your choice:"))
                break
            except:
                print("Try Again Wrong Input")

    if(c==1):
        name = input("Enter Your name:")
        acc = Account(name)
        acc.create()
        general_menu(acc)

    elif(c==2):
        acc = Account("temp")
        account_no = input("Enter your Account No: ")
        res=acc.find_account(account_no)
        if(res==1):
            general_menu(acc)
    elif(c==3):
        acc = Account("temp")
        account_no = input("Enter your Account No: ")
        acc.deactivate(account_no)
    else:
        print("WRONG Choice!!! Please Try Again")




