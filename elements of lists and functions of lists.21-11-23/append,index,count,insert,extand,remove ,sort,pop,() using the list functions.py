# accesing the elements of lists.
# functions of lists
# append() : add an elements to the end of the list.
l=["red","blue","yellow"]
l.append("gray")
print(l)

#
l=["aman is a developer"]
l.append("aman is a writer")
print(l)

#
l=[10,20,30,40,50,60,70]
l.append(80)
print(l)

# add a numbers
#l=[]
#for i in range(21):
#    if i%2==0:
#        l.append(i)
#
l=[10,30,40,50,]
l.append(999)
print(l)

# insert():insert an item as the defined item.
l=["aman","ram","raju","rameh"]
l.insert(2,"ahmed")
print(l)

#
l=["ram is a good boy","aman is a developer"]
l.insert(2,"raju is a writer")
print(l)

#
l=[10,20,30,40,50,60]
l.insert(4,"45")
print(l)

#
l=[10,20,30,40,]
l.insert(1,"0")
print(l)

#
l=["ram is a boy"]
l.insert(1,"good")
print(l)

#extand():add all elements of a list to another list.
l1=["aman","karthik","raju"]
l2=["10,20,30",]
l2.extend("l1")
print(l1)
print(l2)

#
l1=["aman","karthik","raju"]
l2=["10,20,30,"]
l2.extend("ram")
print(l2)
print(l2)


#
l=["aman is a developer"]
l1=["10,20,30,40"]
l.extend("ram")
print(l)
print(l1)

#
l=["10,20,30,40,50"]
l.extend("60")
print(l)

#
l=["red","blue","pink","orange"]
l.extend("blue")
print(l)

# remove(): this method the first occerence of the element with the specified value.
l1=[10,20,30,40,50,60]
l1.remove(60)
print(l1)

l1=["ram","aman","madhu","balu"]
l1.remove("balu")
print(l1)

#
l1=[10,20,30,40,50,60]
l2=["ram","aman","rakesh","laddu"]
l1.remove(20)
l2.remove("ram")
print(l1,l2)

#
l=[10,20,30,40,50,60,70,80,90,10]
l.remove(70)
print(l)

#
numbers=[10,20,30,40,50,60,70,80,90,100]
for num in numbers:
    if num % 2==0:
        numbers.remove(num)
print(numbers)

# revrse(): sorting order of the element.
# syntax: l.reverse()
l=[10,20,30,40,50,60,70]
l.reverse()
print(l)

#
l=["ram","aman","raju","ramana"]
l.reverse()
print(l)

#
l1=[10,20,30,40,50,60]
l2=[20,30,40,50,60]
l1.reverse()
l2.reverse()
print(l1)
print(l2)

#
fruits=["apple","banana","mango"]
l.reverse()
print(fruits)

#'
list=["a","b","c","d","e"]
l.reverse()
print(list)

# sort():this method are accending by default.
l=["ram","AMAN","volo"]
l.sort()
print(l)

#
l=[11,3,7,5,2,1]
l.sort()
print(l)

#
v=["e","a","u","o","i"]
l.sort()
print(v)

#
l=[111,222,33,44,556,777]
l.sort()
print(l)

#
x=[10,20,30,40,50,70,80]
l.sort()
print(x)

#pop():
l=[10,20,30,40,50,60,70]
l.pop(6)#to remove indexing
print(l)

#
l=[1,2,3,4,"ram","aman",8,9,0,]
l.pop(4)
print(l)

#
l=[10,20,30,40,50,60,70,80,90]
print(l.pop())
l.pop(1)
print(l)


 


































