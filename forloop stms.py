#for loop statements.
# for each element in seqyence and do actions.
s="rama krishna"
count=0
for i in s:
    count+=1
    print(i)
    print("the number of character present",count)
#
n=input("enter the word:")
count=0
for i in n:
    print("character present in ",count,"index is ",i)
    count+=2
    count+=3

#for loop
#syntax: 
# for variable name in iterable object
#stmt1:
#stmt2:
#.....
#stmt n
print("enter a name ")
x='aman'
print(x)
for p in x:
    print(p*3)
    print("end")
#range:
# range objects represents group of non decimal point numiracal values
#range is immutable
#syntax: (begin,end,step)
x=range(10)
print(x)
print(x[2])
print(x[-2])
for p in x:
    print(p)

#
x=list()
print(x)
print(type(x))
print(len(x))
y=[]
print(y)
print(type(y))
print(len(y))
z=[10,40,30,60,50]
print(z)
p=[100,3+4j,123.123,'lokesh']
print(p)
v=[100,200,100,200,300]
print(v)
# sum of even numbers
x=[10,20,30,40,50,60]
print(x)
s=0
for p in x:
    s=s+p
    print(s)
    i=0
    eis=0
    while i<len(x):
        eis=eis+x[i]
        i=i+2
        print(eis)
#nested list:
x=[10,20,30],[40,50,60,],[70,80,90]
print(x)
for p in x:
    for v in p:
        print(v,end="")
        print()
    
    #
n=5
for i in range(0,n):
    print (i)
    
#
n=134
for i in range(0,n):
    print(i)
# string itration
s="aman"
for i in s:
    print(i)
    
# 
x=range(10)
print(x)
print(x[2])
for p in x:
    print(p)
#
x= "raju"
print(x)
for p in x:
    print(p*5)

#
x="aman ,raju ,ram"
print(x)
for p in x:
    print(p*2)
 #
x=["ram aman raju ranmana"] 
for i in x:
    print(i)
    if i=='aman':
        print("aman hi")
    else:
        print("aman hi ")
#
a=[20, 30,40,50]
for i in a:
    if i<=250:
        print(i,"grater then 35 ")
    else:
        print(i,"less than 35 ")
#
k=["kajal is a good girl"]
for i in k:
    print(i)
#
num=[1,2,3,4,5]
names=["aman","ram","raju","ramana","nani"]
for i in num:
    for y in names:
        print(i,y)
#
b=[2,6,8,9,]
for i in x:
    print(b)
# sum of even num altenate.
x=[10,20,30,40,50]
print(x)
s=0
for p in x:
    s=s+p
print(s)
i=0
eis=0
while i<len(x):
    eis=eis+x[i]
    i=i+2
    print(eis)
#
x=range(10,20,30)
print(x)


    

    
    
    




    
        









