# Class: class is a blueprint or a template. Eg. Form for an Exam that contains name,age, electives, father's name etc

# Object: Specific instanse created from the tmplate (class.) Eg. Form which contains the data for john doe

class Employee:
    company ="pelupa"

    def get_salary(self): # self is important here because self is a way to reference the object of the class which is being created
        # print(self)
        return 3000
    

e = Employee() # An object of class Employee is created here
print(e.get_salary()) # Emplyee get salary method is called

e2 = Employee()
print(e.get_salary())
print(e2.company)