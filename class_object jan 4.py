class Employee:
      name="aman" 
      def __init__(self,ename,esal,eid,epack,edomain,name):
            name="aman"
            self.ename=ename
            self.esal=esal
            self.eid=eid
            self.epack=epack
            self.edomain=edomain
            self.name=name
      def employeeDetails(self) :
            print("Employee Details:")   
            print(self.name,"________",self.ename,"________",self.esal,"_______",self.eid,"________",self.epack,"___________",self.edomain) 
  
e=Employee("aman",30000,407,2.9,"python","ramu")
e.employeeDetails()
print(e.name)
print(Employee.name)
  
e=Employee("ram",100,0,4.68,"java","ramam")
e.employeeDetails()
print(e.name)
print(Employee.name)


class student:
  def __init__(a,b,c,d,e) :
    a.snm=b
    a.srno=c
    a.sper=d
    a.sclg=e

  def display(a):
      print("display method....")
      print(a.snm)
      print(a.srno)
      print(a.sper)
      print(a.sclg)
s=student("aman",123,77,"vamsi")
s.display()


class Employee:
    def __init__(emp) :
        emp.ename="aman"
        emp.esal=20000
        emp.eid=307
        emp.epack=4.0
    def employeeDetails(emp):   
        print("Employee Details:") 
        print(emp.ename)
        print(emp.esal)
        print(emp.eid) 
        print(emp.epack)
Employee().employeeDetails() 



# using object reference
class studentdata():
    clg="rama krishna"
    def __init__(self,name,rollno,age,section):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.section=section
    def progress(self):
        print(self.clg,self.name,self.rollno,self.age,self.section)
a=studentdata("aman",30,15,"B")
a.progress()
studentdata("aman",30,15,"B").progress()
print()



#static variable  outside the method
class studentdata():
    clg="rama krishna"
    def record(self):
        name="aman"
        age=25
        rollno=35
        section="B"
        print("hlo")
    print(studentdata.clg)
a=studentdata()
a.record()
print() 
#by using method
class Student:
    def studentRecords(self,sname,srno,sper):
        self.sname=sname
        self.srno=srno
        self.sper=sper
        print("student records")
s=Student()
s.studentRecords("aman",44,98)     
#by  using constructor

class Student:
    def __init__(self,sname,srno,sper):
        self.sname=sname
        self.srno=srno
        self.sper=sper
        print("student records")
s=Student("aman",44,98)

 #by using constructor and method
class Student:
    def __init__(self,sname,srno,sper):
        self.sname=sname
        self.srno=srno
        self.sper=sper
    
    def studentRecords(self,sname,srno,sper):
        self.sname=sname
        self.srno=srno
        self.sper=sper
        print("student records")
Student("aman",55,65)  .studentRecords("aman",55,65) 

 










     


    

 