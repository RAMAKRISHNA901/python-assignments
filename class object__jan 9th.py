
class Student:

    def _init_(self,sname,smarks) :
         self.sname=sname
         self.smarks=smarks

    def message(self):
         print(self.sname,"percentage is=",self.smarks,"%") 
        
    @classmethod
    def display(cls,sname,smarks):
        return cls(sname,str((int(smarks)/500*200)))
    

s2=Student.display("rama krishna","80")  
s2.message()

s3=Student.display("aman","40")
s3.message()



class Student:
     count=0
     def _init_(self,sname,smarks) :
         self.sname=sname
         self.smarks=smarks
         Student.count=Student.count+1

     def message(self):
         print(self.sname,"___________________",self.smarks)  
     @classmethod    
     def total_count(cls):
         return cls.count
    
s1=Student("rama krishnakrishna",90)  
s2=Student("aman",88)
print("total count is=",Student.total_count())  # print("total count is=",s1.total_count())
print("total count is=",s2.total_count())



class MyClass:
    def _init_(self,fname,lname) :
        self.fname=fname
        self.lname=lname
    def msg(self):
        print("fname=",self.fname,"lname=",self.lname) 
    @classmethod    
    def getSalary(cls,salary):
         cls.salary=salary

    def s(self):
        print("total salary is=",self.salary)   
       

m=MyClass("rama krishna","aman")
m.getSalary(15000)
m.msg()
m.s()