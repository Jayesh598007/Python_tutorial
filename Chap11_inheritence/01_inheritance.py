# Inheritance is a way for making a new class from an existing class 
'''
class Employee:       -----> Base class
    #code

class Programmer(Employee):   -------> Derived/child class
    #code
'''
# we can use the methods and atributes of base class in a derived class object
# we can alos overwrite or add new metohds and attrubutes in derived class



class Employee:
    company = "Google"     #attribute of base  class
    def showdetails(self):   #func of base class
        print(f"This is an employee of {self.company}")

class Programmer(Employee):
    company = "microsoft"    #attribute of child class
    lang ="Python"
    def getlang(self):      #func of child class
        print(f"The language is {self.lang}")  
    
    def showdetails(self):        
        print(f"This is a Programmer of {self.company}")   


# if the details are not provided for the child class, then it will write them of the base class
# if the details are provided , then it will overwrite them of the base class, and wrie of their own


e = Employee()
p = Programmer()

e.showdetails()    # it will show details of base class
p.showdetails()     # it will show details of child class, if not, then of base class

print(e.company)      # it will show company of base class
print(p.company)     # it will show company 9of child class, if not, then of base clas

p.getlang()     # it will print the lang of child class


