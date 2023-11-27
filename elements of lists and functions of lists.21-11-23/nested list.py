# nested list:we can store list with the another list.
x=[[10,20,30,],[40,50,60],[70,80,90]]
print(x)
print(x[0])
print(x[0][0])
print(x[0][1])
print(x[0][2])
print(x[1])
print(x[1][0])
print(x[1][1])
print(x[1][2])
print(x[2])
print(x[2][0])
print(x[2][1])
print(x[2][2])

# nested lit. program : while . matrix
#
x=[[10,20,30,],[40,50,60],[70,80,90]]
print(x)
i=0
while i<len(x):
    print(x[i])
    j=0
    while j<len(x[i]):
        print(x[i][j])
        j=j+1
    i=i+1
#  nested list -for
x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
for p in x:
    for v in p:
        print(v,end=" ")
    print()
    
#nested list : while
x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
i=0
while i<len(x):
    j=0
    while j<len(x[i]):
        print(x[i][j],end=" ")
        j=j+1
    print()
    i=i+1
# un packed for :nested     
x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
for p,v,r in x:
    print(p,v,r)
    
#
# list comprehensions:
#* the concepts of generating elements into the list object by writing some logic in the list
#is known as a list comprehensions .

# program
x=[p for p in range(10)]
print(x)
y=[r**2 for v in range(10,20)if v%2==0]
print(y)
z=[r*r for r in range (20,30) if r%2!=0]
print(z)


# list objects:
# list object represent group of objects.
# the object which are present inside the list objects are known as elements of lists .
#list object can be created by using list function.
#by using [] brackets
#lists objects are suppourt both positive and negetive indixing.
#dupliate elements are allowed.
#list object are mutable objects'
#elements of the list can be mutable (or) immutable
#
# program.
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
p=[100,True,3+4j,"aman"]
print(p)
print(len(p))
v=[100,200,100,300,200]
print(v)

# sum of even numbes ,ultarnate.

x=[10,20,30,40,50,60,70,80,90]     
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
        














