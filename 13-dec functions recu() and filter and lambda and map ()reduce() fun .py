# anonymous and lambda function:
a=lambda n:n*n
print(a(3))
print(a(12))

#
a=lambda n:n+n
print(a(4))
print(a(1234))

#
a=lambda n:n-n
print(a(3))
print(a(1234))

#
a=lambda n:n%n
print(a(-23))
print(12)

#
a=lambda n:n+n
print(a(2+1+23))
print(a(2+4))

#filter function:
x=[10,11,12,13,14,15]
print(x)
res=list(filter(lambda p:p%2==0,x))
print(res)

#
a=[1,3,56,7,9,00,0,34,567]
print(a)
res=list(filter(lambda p:p%2==0,x))
print(res)

#
y=["ram","aman","achari","abhinay"]
print(y)
res=list(filter(lambda v:len(v)==7,y))
print(res)

a=["blue","green","yellowo","red"]
print(a)
res=list(filter(lambda v:len(v)==5,y))
print(res)


#map()
x=[1,2,3,4,5]
print(x)
res=list(map(lambda p:p*2,x))
print(res)
y=["python","django","oddo","restpai"]
print(y)
res1=list(map(lambda v:len(v),y))
print(res1)
res2=list(map(lambda r:len(r)==6,y))
print(res2)

#
x=[1,2,3,4,5,6,7,]
res=list(map(lambda p:p*4,x))
print(res)

#
x=[11,22,33,44,55,66,77,]
res=list(map(lambda p:p*4,x))
print(res)

# dec function:

def mul(func):
    def inner(a):
        x=func(a)
        return x*x
    return inner
def multwo(func):
    def inner(a):
        x=func(a)
        return 2*x
    return inner
@multwo
@mul
def num(a):
    return a
print(num(10))

#
def divi(func):
    def inner(a,b):
         if b==0:
             print("it cannot divided by zero")
         else: func(a,b)
    return inner
@divi   
def d(a,b):
    print(a/b)
d(10,2)

# nested funtion:
def outer():
    print("this is my outer function")
    def inner():
        print("this is my inner function")
    inner()
outer()



# function alising:
def f(name):
    print("good morning",name)
a=f
f("aman")
a("raju")
