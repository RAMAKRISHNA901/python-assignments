# break statements:
# based on some condition if we want to break execution.
#
for i in range(10):
    if i==8:
        print("hii")
    print(i)
#
for i in range(20):
    if i==9:
        print("hello")
        break
    print(i)
#
for i in range(3):
    for j in range(2):
        if i==j:
            break
        print(i,j)

#
for i in range(20):
    if i==0:
        continue
    print(i)
#
for i in range(25):
    for j in range(25):
        if i==2:
            continue
        print(i,j)
cart=[20,60,400,500,900]
for item in cart:
    if item<500:
       print("product price exceed the limited",item)
       break
print("procesing itemsucess",item)

#pass statement:
for i in range(50):
    if i%20==0:
        print(i)
    else:
        pass
#
for i in range(15):
    for j in range(20):
        for a in range(22):
            if i%10==0:
                print(i,j,a)
            else:
                pass
#
i=["a","b","c","d",]   
for i in i:
    if(i=="a"):
        pass
    else:
        print(i)
#
for name in "rama krishna":
    pass
print("name:","rama krishna")

#
for name in "aman":
    pass
print("name:","aman",)
print("subject:","trinar")

#
i=["ram","aman","raj","ramana"]
for i in i:
    if(i=="a"):
        pass
    else:
        print(i)
#
print("enter a number") 
i=0
while i<5:
    i=i+1
    if i==3:
        continue
    print("hii aman")
#
print("enter the number")
i=0
while i<6:
    i=i+1
    if i==4:
        continue
    print("hii how are you")   
        
        
            
        
 
    













