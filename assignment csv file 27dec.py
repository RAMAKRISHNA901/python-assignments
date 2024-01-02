#csv==> comma separated values. 
# as the part of programming ,it is very common requerment to write and read data/to from csv files. 

#python provides csv modules to handle csv files. 
# program


import csv 
with open("emp.csv",'w')as f: # returns object write data
    w=csv.writer(f)
    #print(type(w))
w.writerow(["ENAME","EMP NO","ESALYRY","EADDAR"])
while True:
    ename=int(input("enter employee name: "))
    enum=int(input("enter employee no: "))
    esal=float(input("enter employee salary: "))
    eaddr=int(input("enter employee adress: "))
    w.writerow([ename,enum,esal,eaddr])
    option=input("do you want to insert one more record[yes|no]:")
    if option.lower()=="no":
        break 
print("total Employees written to csv file sussfully")
    