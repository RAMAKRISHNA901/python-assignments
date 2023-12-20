# try exception:
try:
    print(2/0)
except ZeroDivisionError:
    print("cannot divided zero")
    

#control flow in try except block
try :
    a=3
    b=6
    print(a+b)
    print("aman")
    print(20/5)
except TypeError :
    print("typeerror is occured")
print(a*b)
print("ramya")

#case-2
#nt
try :
    print("rahul")
    a=3
    b="arjun"
    print(a+b)
    print(20/5)
except TypeError :
     print("typeerror  occured")
print("prabha")

#case -3
try :
    print("prthu")
    a=3
    b="rahul"
    print(a+b)
    print(20/5)
except ValueError :
    print("valueerror is occured")
    
    
#case-4    
#at
    
try :
    print("rahul")
    a=3
    b="ravi"
    print(a+b)
    print(20/5)
except TypeError :
    a=3
    b="ram"
    print(a+b)
    print("typeerror occured")  
    
      
#
try:
    a=int(input("enter  num: "))
    b=int(input("enter num: "))
    print(a+b)
    print(a/b)
except (ZeroDivisionError):
    print("please give value")
   
   
#   
try:
    a=int(input("enter num: "))
    b=int(input("enter num: "))
    print(a+b)
    print(a/b)
except (ValueError,) as m:
    print(m)
    
    

        
    
    
    
          
    
    
