# split(): it is divided the sting into multiple words.
x="lokesh aman python django"
print(x)
words=x.split()
print(len(words))
for w in words:
    print(w,len(w),w.upper())

#
s="python is very thogh and python is logical "
l=s.split()
print(s)

#
s="python is simple language and very easy language"
l=s.split()
for x in l:
    print(x,end=" ")
#count()
s="aman is a my trianner"
print(s.count("is"))
print(s)

# replace ().(old string to new string)
s="python is very is language "
s=s.replace("python","java")
print(s)

# program to display the all position of sub string in the given string.
s=input("enter the string:")
subs=input("enter the sub string:")
flag=False
position=-1
n=len(s)
while True:
    position=s.find(subs,position+1,n)
    if position==-1:
        break
    print("found at index:",position)
    flag=True
if flag==False:
    print("NOT found")
    

#assignments write
#1)
# beast is a rangerover:out put
s="rengerover is a beast"
a=s.split()
for i in a[::-1]:
    print(i,end=" ")
    

#
s1="rangerover is a beast"
print(s1[::-1])
print() 

#upper()  
# string.isupper: syntax
a="WELOCOME TO MY WORLD"
b="python language"
c="PYTHON IS A GOOD LANGUAGE"
d="aman is a developer"
print(a.upper())
print(b.upper())
print(c.upper())
print(d.upper())
print()
#lower
# syntax: string.islower.
a="HELLO AMAN"
b="hello ram"
c="my name is aman"
print(a.lower())
print(b.lower())
print(c.lower())

#titile()
text="welocome to my 2world"
x=text.title()
print(x)

# swape case()
a="Hii aman "
b="Hi ram"
print(a.swapcase())
print(b.swapcase())

# capitialize ()
a="hello aman welocome to python"
b="hii aman"
print(a.capitalize())
print(b.capitalize())






    
  






















