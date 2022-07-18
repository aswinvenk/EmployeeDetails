import getEmployeeForm as g
"""the getEmployeeForm module is used to get Employee details and store them as JSON"""

e=g.Employee()
"""Creating an object(e) for the class Employee()
Once the object is created, it will ask for number of employees"""

d=e.getDetails()
"""obj.getDetails() will ask you for inputs and returns the data as a dict"""

#e.toJSON(d)
"""obj.toJSON is a method used to save the employee data as JSON in employeeDetails.json"""


e.toYourJSON(d)
"""e.toYourJSON is a method used to save the employee data as JSON as a separate file
after giving your preferrred 'filename', the JSON is saved as 'filename'.json"""


#d=["I have written this list for a sample code",1,2,3,4,5,"Its just a sample","@#$%!"]
#e.toYourJSON(d)