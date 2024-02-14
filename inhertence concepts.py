#single level inheritance #inheriting properities from one class to another class
#
class P:
    def m1(self):
        print("this is parent class")

class C(P):
     def m2(self):
        print("this is child class")

c=C()
c.m2()
c.m1()


#multi level inheritance # grand father->father->child
#
class gf:
    def m1(self):
        print("grand father")
class f(gf):
    def m3(self):
        print("father")
class c(f):
    def m2(self):
        print("child")

c=c()
c.m1()


#hierarchical ->single parent but mutiple childs

class r:
     def m1(self):
         print("parent")

class c1(r):
     def m2(self):
         print("child 1")

class c2(r):
     def m3(self):
         print("child 2")

c1=c1()
c1.m2()
c1.m1()

# c2=c2()
# c2.m1()
# c2.m3()


#multiple #if parent class is multiple but one child class

class r1:
    def m3(self):
         print("parent 1")

class r2:
    def m1(self):
        print("parent 2")

class c(r1,r2):
    def m2(self):
        print("child")


c=c()
c.m1()
#single level inheritance
class p:
    def m1(self):
        print("this is parent class")
class c(p):
    def m2(self):
        print("this is child class")
c=c()
c.m2()
c.m1()


class p():
    def first(self):
        print("this first function")
class c(p):
    def second(self):
        print("this  second function")
c=c()
c.first()
c.second()

class p():
    def a(self):
        print("this first section")
class c(p):
    def b(self):
        print("this  second section")
c=c()
c.a()
c.b()

#multi level inheritance
class gp:
    def m1(self):
        print("grand father")
class p(gp):
    def m2(self):
        print("parent")
class c(p):
    def m3(self):
        print("child")
c=c()
c.m1()
c.m2()
c.m3()


class gp:
    def m1(self):
        print("grand father")
class p(gp):
    def m1(self):
        print("parent")
class c(p):
    def m1(self):
        print("child")
c=c()
c.m1()

class gp:
    def m1(self):
        print("grand father")
class p(gp):
    def m1(self):
        print("parent")
class c(p):
    def m3(self):
        print("child")
c=c()
c.m1()


#hierarchical 
# -> single parent but multiple child class

class mobile:
    def a(self):
        print("phone")

class c1(mobile):
    def b(self):
        print("one plus")

class c2(mobile):
    def c(self):
        print("redmi")

c1=c1()
c1.b()
c1.a()

c2=c2()
c2.a()
c2.c()

class p:
    def m1(self):
        print("parent")

class c1(p):
    def m2(self):
        print("child 1")

class c2(p):
    def m3(self):
        print("child 2")

c1=c1()
c1.m2()
c1.m1()

c2=c2()
c2.m1()
c2.m3()


class human:
    def a(self):
        print("human")

class c1(human):
    def b(self):
        print("rama krishna")

class c2(human):
    def c(self):
        print("rahithya")

c1=c1()
c1.a()
c1.b()

c2=c2()
c2.a()
c2.c()


class p:
    def a(self):
        print("parent")

class c1(p):
    def b(self):
        print("rama krishna")

class c2(p):
    def c(self):
        print("rahiyatha")

c1=c1()
c1.a()
c1.b()

c2=c2()
c2.a()
c2.c()


#multiple
# #if parent class is multiple but one child class



class p1:
    def m1(self):
        print("parent")
class p2:
    def m2(self):
        print("parent 2")
class c(p1,p2):
    def m3(self):
        print("child")
c=c()
c.m2()
c.m1()
c.m3()


class p1:
    def a(self):
        print("parent")
class p2:
    def a(self):
        print("parent 2")
class c(p1,p2):
    def a(self):
        print("child")
c=c()
c.a()




class p1:
    def c(self):
        print("parent")
class p2:
    def a(self):
        print("parent 2")
class c(p1,p2):
    def b(self):
        print("child")
c=c()
c.a()
c.b()
c.c()


