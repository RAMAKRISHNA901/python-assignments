
# assignments
#input:aman is good.
#out put:good is aman.
s="aman is good"
a=s.split()
for i in a[::-1]:
    print(i,end=" ")
    
#input:AABBCCCDDEEFGGHHIJJKKLLLAABBC
#output:ABCDEFGHIJKL
list="AABBBCCDDEFGGHHIJJKKLAB"
X=[]
y=[]
for i in list:
    if i not in X:
        X.append(i)
for i in X:
    if list.count(i) > 1:
        y.append(i)
print(y)

#LIST FIND ONLY 30 AND 40
list=[10,20,30,[40,50,60],70,80,90]
print(list[2],list[3],[0])
#      
        
        
        
        
        
        
        
