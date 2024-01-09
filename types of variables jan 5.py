class Employee:
    def __init__(self,eno,ename,esal) :
        self.eno=eno
        self.ename=ename
        self.esal=esal
        
    def employeeDetails(self):
        print("eno=",self.eno)
        print("ename=",self.ename)
        print("esal=",self.esal)


Employee(11,"rama krishna",25555).employeeDetails()

e=Employee(22,"aman",767889)
e.__init__
e.employeeDetails()

#constructor overloading
class ram:
    def __init__(self):
        print("this is first constructor method_____________________")
    def __init__(self):
        print("this is second constructor method_____________________")    
    def __init__(self):
        print("this is third constructor method")   
    def __init__(self):
        print("this is fourth constructor method")    
d=ram()       





class Student:
    def __init__(self,sname,srno,sage,sper,sclg):
        self.sname=sname
        self.srno=srno
        self.sage=sage
        self.sper=sper
        self.sclg=sclg

    def StudentDetails(self):
        print("sname=",self.sname)    
        print("srno=",self.srno)
        print("sage=",self.sage) 
        print("sper=",self.sper)
        print("sclg=",self.sclg)

s=Student("rama krishna",27,34,55,"aman")
s.StudentDetails()

Student=[Student("rama krishna",55,97,69,"sai")]
for i in Student:
    i.StudentDetails()

#1).instance variables(object level variable)
    
#1).inside the constructor you can declare  the variable
#2).inside the instance  method using self variables
#3).outside the class by using object refercence variable

class Employee:
    def __init__(self): #1
        self.ename="rama krishna"
        self.esal=5000000
        self.eid=2995
    def employeeDetails(self):#2
              self.phno=9014
              self.edomain="python developer"

e=Employee() 
print(e.__dict__)

e.employeeDetails()
print(e.__dict__)
#outside the class by using object refercence variable
e.ecnm="mphasis"#3
print(e.__dict__)
print(e.ecnm)
print(e.phno)
print(e.edomain)

class Student:
    def __init__(self):
        self.sname="rama krishna"
        self.srno=34
        self.sage=28
        self.sper=79
        self.sclg="atp"
    def details(self):
        self.sbranch="bsc"
s=Student()
s1=Student()
s.details()
s1.details()
s1.d=800

print(s.__dict__)       
print(s1.__dict__)  
print(s.sname)  
print(s1.sbranch)


#2).static variable(class level variable)

#how to acces static variable
#should be acced either by classname or by object reference
class Employee:

    enm=" rama krishna"#sta var

    def __init__(self):#inst var
        self.eid=356
        self.esal=8888
    def display(self):
        print("eid=",self.eid)
        print("esalary=",self.esal)    
e=Employee()
print(e.enm) 
print(e.__dict__)

print(Employee.enm)
e.display() 

print(e.eid)
print(e.esal)


class Employee:

    enm="aman"#sta var

    def __init__(self):#inst var
        self.eid=123
print("_______")
e=Employee()
e.eid=33

Employee.enm=" rama krishna"
e1=Employee()
print(e.enm,e.eid)
print(e1.enm,e1.eid)


      



              


      