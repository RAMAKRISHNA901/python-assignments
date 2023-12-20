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
    
    #try exception 

# try:
#     #risky code
# except BaseException :
#     #handling code

# print("statement1")
# try:
#     print(10/0)
# except ZeroDivisionError as m:
#     print(10/2,"message - ",m)
# print("stat 3")

#control flow in try except block

# try:
#     statement-1
#     statement-2
#     statement-3
# except:
#     statment-4
# statment-5

#case-1
#if there is no error in try block statement-1,2,3,5 -Normal termination

#case-2
#if an excep raised at stat-2 and corresponding except block is matched -stat -1,4,5
#normal termination

#case -3
#if an excep raised at stat-2 and corresponding except block is not matched

# try:
#     print("hi")
#     print(10/0)
#     print("hello")
# except ZeroDivisionError:
#     print("stat -4")
# print("stat -5",10/0)


# try:
#     statement-1
#     statement-2
#     statement-3
# except:
#     statment-4
# statment-5


# try:
#     a=int(input("enter the first number : "))
#     b=int(input("enter the sec number : "))
#     print(a/b)
# except (ZeroDivisionError,ValueError) as m:
#     print(m)


#4
try:
    print(100+50)
    print(10/0)
    print("hello")
except ZeroDivisionError:
   print(10/2,"hiii")
print(10/0,"hlooo")  



#5
try:
    print(100-50)
    print(10/0)
    print("hello")
except ZeroDivisionError as m:
   print(10/2,"hiii",m)
print(10/0,"hlooo")  




try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divided by zero") 



try:
    a=int(input("enter the first number"))
    for i in range(0,10):
       if i%2==0:
           
           print(i,"is even")
       elif i%2!=0:

           print(i,"is odd numbers")
except :
    print("invalid")
    

try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot division of number") 
except ValueError:
    print("please provide a value not string")    



try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except (ZeroDivisionError,ValueError )as m:
    print(m) 


 

        
    
    
    
          
    
    
