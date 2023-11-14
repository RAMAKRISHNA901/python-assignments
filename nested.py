#
for i in range(4):
    for j in range(4):
        print("i={}andj={}".format(i,j))
#
for i in range(4):
    for i in range(5):
        for z in range(3):
            print("i={}amdj={}andz={}".format(i,j,z))
#
for i in range(4):
    for i in range(4):
        print("hello")
        for z in range(3):
            print("i={}andj={}andz={}".format(i,j,z))
#
for i in range(3):
    for j in range(3):
        print("aman")
        print()
#
for i in range(3):
    print("hii")
    for j in range(3):
        print("aman")
# pattern:
for i in range(5):
    for j in range(5):
        print("*",end=" ")
#
for i in range(4):
    for j in range(4):
        print("*",end="  ")
    print()
#
for i in range(3):
    for j in range(4):
        print("*")
        print()
#
n=int(input("enter n value:"))
for i in range(n):
    print("*",end="  ")
    print()
#

for i in range(4):
    for j in range(9):
        print(i,end="   ")
        print()
#
n=int(input("enter num of rows:"))
for i in range(n):
   print("* "*n)
   
   
   
#

n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end="    ")
    print()
#
n=int(input("enter a number:"))
for i in range(1,n+1):
    for k in range(i):
        print("*",end="")
    print()

#
row=5
b=0 
for i in range(row,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end="")    
        
#
n=int(input("enter the number of rows:"))
for i in range(6):
    print(""*(n-i-1)+(str(i+1)+"")*(i+1))
    
#   
n=int(input("enter a number of rows:"))
for i in range(5):
    print(""*(n-i-2)+(str(i+2)+" "))
# pattern numbers:

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    