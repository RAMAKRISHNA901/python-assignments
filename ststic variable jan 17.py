import sys
class customer:
    bankname="SBI"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("the balance after the deposit is :",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient amount, please withdraw with in the balance amount")
            sys.exit()
        self.balance=self.balance-amount
        print("the balance after the withdraw is ",self.balance)

print("welcome to ",customer.bankname)
name=input("Enter your name :ram ")
c=customer(name)
while True:
    print("d-deposit \n w- withdraw \n e- exit")
    option =input(" choose your option ") 
    if option=="d":
        amount=int(input("enter the amount to deposit : "))#1000
        c.deposit(amount)
    elif option=="w":
        amount=int(input(" enter the withdraw amount :"))
        c.withdraw(amount)
    elif option=="e":
        print("thank you for banking with us ")
        sys.exit()
    else:
        print("invaild option, please select correct option ")
    
        
 # delete of static variable
class student:
    a=10
    @classmethod
    def m2(cls):
        del cls.a

student.m2()
print(student.__dict__)




class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=40
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=588
        del Test.c
    @staticmethod
    def m3():
        Test.r=70

t=Test()
t.m1()
t.m3()
print(Test.__dict__)

class Test:
    a=10
    def __init__(self):
        Test.b=30
        del Test.a
    def m1(self):
        Test.c=40
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=588
        del Test.c
    @staticmethod
    def m3():
        Test.r=50

t=Test()
t.m1()
t.m2()
t.m3()
print(Test.__dict__)








Comment
       
        
        
        
        
        
