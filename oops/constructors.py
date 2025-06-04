# Class: class is a blueprint or a template. Eg. Form for an Exam that contains name,age, electives, father's name etc

# Object: Specific instanse created from the tmplate (class.) Eg. Form which contains the data for john doe

class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instance attribute of name salary and assign it wiht salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the emplyee is {self.name}. Salary is {self.salary}. THe bond is for {self.bond} years")

e1 = Employee(3400,"john doe", 4)
print(e1.get_salary())
print(e1.get_info())