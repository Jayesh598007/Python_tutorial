class Employee:  
    company = "Google" 
    salary = 100
'''
    # 'company' is a class attribute, it is directly related to the class
    # Class Atribute will apply on every instance(Employee) of the class
'''

harry = Employee()   #adding the employees
rajni = Employee()
harry.salary = 300
rajni.salary = 400
'''
    # 'salary' is a instance attribute, it belongs with only the employee, not the whole class
    # Instance attribute belongs to only the instance(Employee) of the class
'''
print(harry.company)   # printing the empolyee company
print(rajni.company)

Employee.company = "Youtube"   # changing the company name
print(harry.company)     # printing the empolyee company again
print(rajni.company)

print(harry.salary)
print(rajni.salary)

