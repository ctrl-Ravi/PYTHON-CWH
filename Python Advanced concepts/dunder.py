class Employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
    # for user
    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    # for developer
    def __repr__(self):
        return f"name: {self.name}\nsalary:{self.salary}"
    
    def __len__(self):
        return len(self.name)

e = Employee("Ravi", 24343)
# print(e.name,e.salary)
# print(str(e))
# print(repr(e))
print(len(e))