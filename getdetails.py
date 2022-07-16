import time
import json
class Base:
    def __init__(self):
        self.employee={}

class EmpDetails:
    def __init__(self):
        self.name=input("Enter your First name : ").title()+" "+input("Enter your Last name : ").title()
        self.age=int(input("Enter your age : "))
        self.gender=input("Enter your gender (M/F/NA) : ").upper()
        self.hobby=input("Enter your hobby : ").title()
        self.salary=float(input("Enter your salary (in numbers) : "))
    def getDict(self):
        return({self.name:{"Age":self.age,"Sex":self.gender,"Hobby":self.hobby,"Salary":self.salary}})

class Employee(Base):

    def getEmpCount(self):
        self.x=int(input("Enter the number of Employees : "))
    def getDetails(self):
        try:
            for i in range(self.x):
                time.sleep(0.5)
                print("Hi There!!")
                time.sleep(1)
                print("Please fill in your details!")
                time.sleep(1)
                e=EmpDetails()
                self.employee.update(e.getDict())
                time.sleep(0.5)
                print("Thank you for filling the form ♥ \n")
                time.sleep(1)
                if (i<self.x-1):
                    print("Enter details for the next Employee! \n")
                time.sleep(1)
            return self.employee
        except:
            time.sleep(1)
            print("For more number of employees...")
            time.sleep(2)
            print("Get number of Employees from obj.getEmpCount()")
            time.sleep(1.5)
    def toJSON(self,data):
        self.data=data
        json.dump(self.data,open("employeeDetails.json",'w'))



e=Employee()
e.getEmpCount()
d=e.getDetails()
e.toJSON(d)