# dictionary: dictionary objects represented are group of items.
# key values are pair is known as item. 
#dictionary objects can be created by calling dict function (or) by using "{}".
# dictionary objects are mutable objects. 
#values can be mutable. 
#duplicate keys are not allowed . 
#values are allowed. 

# some methods in dictionary.
# 
x=dict()
print(x)

# 
x=dict()
print(type(x))

#
x=dict()
print(len(x))

#
z={"aman":99,"ram":89,"raju":78,"ramana":56}
print(z)
#

x={10:"python",20:"java",30:"hadoop"}
print(x)

#
x={"aman":200,"ram":300,"rekha":400,"latha":500}
print(id(x))
y={20:"aman",25:"ramana",35:"balaji"}
print(id(y))

#
x={"python":200,"ram":400,"aman":500}
print(x["ram"])
print(x["python"])
#
x={"red":20,"yellow":40,"green":50}
print(x["red"])
print(x["yellow"])


# 
x={"aman":21,"raju":22,"red":33,"green":45}
for k in x:
    print(k,x[k])
    
#
x={"red":21,"green":22,"yellow":33,"orange":45}
for k in x:
    print(k,x[k]) 
#  copy
#
x={"aman":10,"ram":20,"madhu":30,"mahesh":40}
print(x)
y=x.copy()
print(y)

#
x={"kajal":10,"samantha":20,"rasmika":30,"thamanna":40}
print(x)
y=x.copy()
print(y)

#
x={20:"aman",25:"ramana",35:"balaji","ram":43,"roja":78}
print(x)
y=x.copy()
print(y)

#
x={2000:"mahesh",25000:"varun",3005:"vasu","sam":4003,"aman":7998}
print(x)
y=x.copy()
print(y)

#
x={20:"brown",25:"blue",30:"orange","yellow":40,"red":7}
print(x)
y=x.copy()
print(x)

# delete
d={10:"raju",20:"ramana",40:"aman",50:"varun"}
del d[40]
print(d)
#
d={1022:"d",2034:"c",40444:"b",540:"a"}
del d[2034]
print(d)


# clear()
x={"ram":2022,"aman":7898,"raju":7879}
x.clear()
x.clear()
print(x)
# 
d=dict([(500,"ram"),(600,"aman"),(700,"ashok"),(800,"ahmed"),(900,"madhu")])
print(d.get(500))
print(d)
#
d=dict([(10000,"red"),(20000,"yellow"),(30000,"orange"),(40000,"green"),(50000,"gray")])
print(d.pop(10000))
print(d)
#
d=dict([(1,"aman"),(2,"ram"),(3,"achiri"),(4,"mahi"),(5,"raju")])
print(d.popitem())
print(d)




# keys
x={"aman":10,"ram":20,"raju":30,}
k=x.keys()
print(k)
#
x={"colours":600,"digrams":500,"writing":400,}
k=x.keys()
print(k)

#
x={"aman":2000,"balu":3000,"charan":4000,"dj ram":5000}
k=x.keys()
print(k)
for p in k:
    print(p)
# values
x={"aman":10,"ram":20,"raju":30,}
v=x.values()
print(v)
for v in v:
    print(v)



# items
x={"aman":2000,"balu":3000,"charan":4000,"dj ram":5000}
x=x.items()
print(x)

for i in x:
    print(i)
    for j in i:
        print(j)

d=dict([(1,"aman"),(2,"ram"),(3,"achiri"),(4,"mahi"),(5,"raju")])
print(d.keys())
print(d.values())
l=d.items()
for k,v in l:
    print(k,v)

