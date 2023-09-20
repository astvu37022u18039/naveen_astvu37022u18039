class Bank_Account:
    __balance=0.0
    __acntno=0
    __acnthldnm=""
    def __init__(self):
        print("Hello!\nWelcome to the Deposit & Withdrawal Machine")
        self.__acntno=int(input("\nEnter ur Account No: "))
        self.__acnthldnm=input("Enter ur Name: ")
 
    def deposit(self):
        amount=float(input("\nEnter amount to be Deposited: "))
        self.__balance += amount
        print("Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("\nEnter Amount to be Withdrawn: "))
        print("\nWithdral Report:")
        if self.__balance>=amount:
            self.__balance-=amount
            print("Acco`unt No: ",self.__acntno,"\nAccount Holder Name: ",self.__acnthldnm,"\nYour Withdrew: ", amount)
        else:
            print("\n Insufficient __balance  ")
 
    def display(self):
        print("\nBalance Report:","\nAcco`unt No: ",self.__acntno,"\nAccount Holder Name: ",self.__acnthldnm,"\nNet Available Balance=",self.__balance)
 
s = Bank_Account()
s.deposit()
s.withdraw()
s.display()
input()
