

#create a class with instance attributies.

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("Hii, my name is:{} and my age is:{}".format(self.name,self.age))

student1=student("aman",26)
student2=student("ram",22)

student1.details()
student2.details()

#creating vehicle class with out any variables and methods......

class vehicle:
    pass
v=vehicle()



#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class


class Vehicle:

 def __init__(self, name, speed, mileage):
    self.name = name
    self.speed = speed
    self.mileage = mileage
class car(Vehicle):
 pass

vehical = car("mahindra", 150, 30)
print("Vehicle Name:", vehicle.name, "Speed:", vehicle.speed, "Mileage:", vehicle.mileage)

