# numbers pattern:
n=int(input("enter the number :"))
for i in range(1,n+1):
        for j in range(i):
            print(j+1,end="")
        print()

#4,0,1,2,3
n=int(input("enter a number:"))
for i in range(2,n+1):
    for j in range(i):
        print(i+1,end="")
    print()
#
n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
#
n=int(input("enter a number:"))
for i in range(2,n+1):
    for j in range(i):
        print("*",end="")
    print()
#
rows=5
for j in range (1, rows+1):
    print("* " * j)
    
#
n=int(input("enter a number:"))
for i in range(1,n-2):
    for j in range(i,):
        print("*",end=" ")
    print()
    
#
n=int(input("enter a number:"))
for i in range(5):
    for i in range(4):
        print("*",end="  ")
    print()
#
for i in range(1,n-1):
    for i in range(i):
        print("*",end=" ")
    print()
    
#
for i in range(rows):
    for j in range(i):
        print("*",end=" ")
    print()
    
#
rows=5
n=int(input("enter a number of rows"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()

#
for i in range(rows+1,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print()
#
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
    
# full parymid of stars:
for i in range(5):
    for s in range(-6,-i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
# left triangle pattern
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
# right triangle pattern
for i in range(1,n+1,):
    for j in range(i):
        print("*",end="")
    print()

#square pattern
for i in range(0,5):
    for j in range(0,5):
        print("*",end="")
    print()
# left down word pattern
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
#dimand star
n=5
for i in range(n):
    for j in range(n-i-1):
        print("*",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
#paramid pattern
for i in range(5):
    for s in range(-6-i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
# inverted half parymid
for i in range(5):
    for j in range(i,5):
        print("*",end="")
    print()
# stright line *
for i in range(4):
    for j in range(4):
        print("*")
    print()
# enter number of rows.
n=5
for i in range(1,n+1):
    for j in range(i):
        print("*",end="") 
    print()
# pattern
n=int(input("enter a number of rows"))
for i in range(0,n):
    for j in range(0,i):
        print("")
for j in range(0,i+1):
    print("*",end="")
print("")
    
#
for i in range(5):
    for j in range(i):
        print("*",end="") 
    print() 
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()
 #
for i in range(8):
     for j in range(i-7+1):
         for k in range(i+7):
             print("*",end=" ")
             print()
#
for i in range(14):
    for j in range(i):
        print("*",end="") 
    print() 
for i in range(14):
    for j in range(14-i):
        print("*",end="")
    print()
#              
n=13             
for i in range(13):
    for j in range(j):
        print("*",end=" ") 
    print() 
for i in range(13):
    for j in range(13-j):
        print("*",end=" ")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    