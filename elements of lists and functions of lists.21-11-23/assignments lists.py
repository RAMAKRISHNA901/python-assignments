#write a program to display uniqe vowels present in the words.
#ch=input("enter a character:")
#for i in ch:
#    if(ch=="a"or ch=="e"or ch=="i"or ch=="o" or ch=="u"):
#       print(i,"it is a vowels")
#    else:
#        print(i,"it is not vowls")

# square root of range from 1 to 20.
list=[x*x for x in range(1,21)]
print(list)

# copy ()
x=[10,20,30,40,50,60,70]
x.copy()
print(x)

#reverse short ()
list=[10,22,32,40,44,55,60]
list.sort(reverse=True)
print(list)

#
list=["ram","aman","raju","ramana","AMAN RAJ"]
list.sort(reverse=False)
print(list)

# write a program to take tuple of numbers from key board print sum average.
x=(10,20,30,40,50,60,70,80,90)
print(x)
i=1
ois=0
while i<len(x):
    ois=ois+x[i]
    i=i+1
print(ois)

























