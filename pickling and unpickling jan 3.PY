class Student:
    sname="marvel"
    def __init__(self,person_name,person_section,person_rollno):
        self.name=person_name
        self.section=person_section
        self.rollno=person_rollno
    def display(self):
        print(self.sname,"----",self.name,"----",self.section,"----",self.rollno)

    

s=Student("aman","c",21)
b=Student("raju","a",45)
c=Student("sairam","B",98)

s.display()
b.display()
c.display()




#pickling and unpickling

import pickle

class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eno,"/t",self.ename,"/t",self.esal)

with open("emp.data","wb") as f:
    c=Employee(123,"rama krisna",20000)  
    d=Employee(456,"aman",10000)
    e=Employee(789,"varun",25000)
    pickle.dump(b,f) 
    pickle.dump(e,f)
    pickle.dump(c,f)
    
    print("pickle of emp object is done ")

#unpickle

with open("emp.data","rb") as h:
    self=pickle.load(h)
    self=pickle.load(h)
    self=pickle.load(h)
    self.display()
    self.display()
    self.display()



class Studentdata():
    def __init__(self,stuname,sturollno,stuage,stucourse,stuaddress):
        self.stuname=stuname
        self.sturollno=sturollno
        self.stuage=stuage
        self.stucourse=stucourse
        self.stuaddress=stuaddress
    print("Each student data:")
    def progress(self):
        print(self.stuname,"---",self.sturollno,"---",self.stuage,"---",self.stucourse,"---",self.stuaddress)

self=Studentdata("ram",100,12,"python","madhapur") 
self.progress()      
self=Studentdata("aman",101,34,"developer","vizag")
self.progress()


import pickle
class Studentdata():
    def __init__(self,stuname,sturollno,stuage,stucourse,stuaddress):
        self.stuname=stuname
        self.sturollno=sturollno
        self.stuage=stuage
        self.stucourse=stucourse
        self.stuaddress=stuaddress
    print("student data:")
    def progress(self):
        print(self.stuname,"---",self.sturollno,"---",self.stuage,"---",self.stucourse,"---",self.stuaddress)



#pickling


import pickle
# python object 
sample_list=[23,"aman","developer"]



#pickling and unpickling
#some times we have to write total state of object and we 
# have to read the state of the object from the file
# class --> blue print of model
#object --> each AC (each instance is a one object )
#reference var --> is remote to operat object 
import pickle

class student:
    def __init__(self,srollno,sname,smark):
        self.srollno=srollno
        self.sname=sname
        self.smark=smark
    def display(self):
        print(self.srollno,"/t",self.sname,"/t",self.smark)

with open("student.data","wb") as p:
    e=student(233,"aman",200)
    b=student(244,"ram",400)   
    pickle.dump(e,p)
    pickle.dump(b,p)
    print("pickle of student object is done ")

#unpickle

with open("student.data","rb") as f:
    obj=pickle.load(f)
    print("student information after the unpickling")
    obj.display()







