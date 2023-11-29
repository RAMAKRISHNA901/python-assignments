# pop()
s={10,20,30,40,50,}
print(s.pop())
print(s)

#
s={10,20,30,40,50}
s.pop()
print(s)

#
s.remove(40)
s.pop()
print(s)

#
s={10,20,30,40,50,60,70,80,90,100}
s.pop()
print(s)

#
s={50,84,49,89.90}
s.pop()
print(s)

#remove ()
l={10,20,30,40,50}
l.remove(20)
print(l)

#
l={100,200,300,400,500,600}
l.remove(200)
print(l)

#
l={1020,303,405,503,603}
l.remove(1020)
print(l)
#
l={100,200,300,400,500,600,700,800,900}
l.remove(400)
print(l)

#
l={101,202,303,404,505}
l.remove(303)
print(l)

# discard()
l={10,20,30,40,50,60,}
l.discard(100)
print(l)

#
l={100,200,300,400,500,600,700}
l.discard(500)
print(l)

#
l={201,401,201,501,601}
l.discard(700)
print(l)

#
l={1001,2001,3001,4001,5001,60011,7001}
l.discard(5001)
print(l)
#
x={10,20,30,40,50,60,}
x.add(80)
print(x)

#
x={100,200,300,400,500}
x.add(50)
print(x)

#
x={200,300,400,500,600,}
x.add(700)
print(x)

#
x={101001,199191,939993,39993,48484}
x.add(1373)
print(x)


# set comprenchions.
# this concepect are generating elementsinto the set by writing logic in the set is known as a set compreanchions
x={p for p in range(10)}
print(x)

y={v**2 for v in range(10,20) if v%2==0}
print(y)

z={r*r for r in range(20,30)if r%2!=0}
print(z)




















