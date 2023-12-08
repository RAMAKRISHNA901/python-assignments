# nested dictionary:
x={"aman":{"ram":10,"aman":20,"raju":30},"colours":{"red":10,"orange":20,"blue":30}}
print(x)

for keys in x:
    print(keys,x[keys])
    for p in x [keys]:
        print(p,x[keys][p])
    
               
for i,j in x.items():
    print(i,j)
    for a,b in j.items():
        print(a,b)




# searching elements for dictionary
#x={"python":"django","java":"spring","hadoop":"bive"} #members ship operaters work on dictionary keys.
#print(x)
#print=input("enter a element:")
#if print in x:
#    print("element is found")
#else:
#    print("element is not found")

# output :
# enter a element :java
#element is found
#enter search element:spring
#elemen is not found

# dictionary compranchions:
# this concept of generating items into the dictionary by writing some logic in the dictionary. 
# example program:
x={p:p*p for p in range(5)}
print(x)

y={r**3:r for r in range(12,20)if r%2!=0}
print(y)

# split dictionary:
names="aman ram jaya madhu python"
words=names.split()







        