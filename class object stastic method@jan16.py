
class Test:
    a=10
    def __init__(self):
        self.b=999
    
    def m1(self):
        Test.a=800
    @classmethod
    def m2(cls):
        cls.a=600
    @staticmethod
    def m3():
        Test.a=200
    
t=Test()
t.m1()
t.m2()
t.m3()
t.a=489
print(t.a)
print(Test.a)


class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=30
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=677
        del Test.c
    @staticmethod
    def m3():
        Test.r=60
        

t=Test()
t.m1()
t.m3()
print(Test.__dict__)



class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=40
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=677
        del Test.c
    @staticmethod
    def m3():
        Test.r=50
        
t=Test()
t.m1()
t.m2()
print(Test.__dict__)



class Test:
    a=10
    def __init__(self):
        self.b=1000
    
    def m1(self):
        Test.a=800
    @classmethod
    def m2(cls):
        cls.a=600
    @staticmethod
    def m3():
        Test.a=300
    
t=Test()
t.m1()
t.m2()
t.m3()
t.a=568
print(t.a)
print(Test.a)



