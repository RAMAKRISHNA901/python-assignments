#accessing members of one class inside another class

class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    
    def display(self):
        print("eno : ",self.eno)
        print("ename ",self.ename)
        print("esal : ",self.esal)

class Test:
    def modify(emp):
        emp.eno=emp.eno+1000
        print("printing name inside test class modify method ",emp.ename)
        emp.display()

e=employee(23,"aman",2000)
Test.modify(e)


#accessing members of one class inside another class

class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    
    def display(self):
        print("eno : ",self.eno)
        print("ename ",self.ename)
        print("esal : ",self.esal)

class Test:
    def modify(emp):
        emp.eno=emp.eno+2000
        print("printing name inside test class modify method ",emp.ename)
        emp.display()

e=employee(23,"aman",4000)
Test.modify(e)


#accessing members of one class inside another class.
#1
class student:
    def __init__(self,stuno,stuname,stumarks):
        self.stuno=stuno
        self.stuname=stuname
        self.stumarks=stumarks

    def display(self):
        print("stuno : ",self.stuno)
        print("stuname ",self.stuname)
        print("stumarks : ",self.stumarks)

class Test:
    def modify(stu):
        stu.stuno=stu.stuno+200
        print("print name inside test class modify ",stu.stuname)
        stu.display()

a=student(23,"aman",23)
Test.modify(a)

#2
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

class bus:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def display_info(self):
        print(f"bus Model: {self.model}")
        print(f"Fuel Type: {self.engine.fuel_type}")

my_engine = Engine("Diesel")
my_bus = bus("tata", my_engine)

my_bus.display_info()



# inner class.
#1
class outer:
    def __init__(self):
        print("outer class object creations")

    class Inner:
        def __init__(self):
            print("inner class of creation")

        def m1(self):
            print("inner class method")

o=outer()
i=o.Inner()
i.m1()

#2
class OuterClass:
    def __init__(self):
        self.outer_var = "I am an developer"

    class InnerClass:
        def __init__(self):
            self.inner_var = "I am not  developer"

o = OuterClass()
i = o.InnerClass()

print(o.outer_var)
print(i.inner_var)

#3
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    class Item:
        def __init__(self, product, price):
            self.product = product
            self.price = price

cart = ShoppingCart("aman")
item1 = cart.Item("Earphones", 1300)
item2 = cart.Item("key board", 600)

cart.items.append(item1)
cart.items.append(item2)

for item in cart.items:
    print(f"{item.product}: accer{item.price}")








