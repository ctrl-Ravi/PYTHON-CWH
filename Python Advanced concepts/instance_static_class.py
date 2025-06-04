class Emplyoyee:
    company = "pelupa" 
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary

    # Instance methos(default)
    def print_info(self): 
        info= f"name is {self.name} and the salary is {self.salary}"
        print(info)
    # Static Method
    @staticmethod
    def sum(a,b):
        return a+b
    
    #class metthods 
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_compnay(cls,new_company):
        cls.company = new_company

e1 = Emplyoyee("jack",324243)
e2= Emplyoyee("ravi", 234)
# print(Emplyoyee.company)
# # print(Emplyoyee.name
# e1.print_info()
# print(e2.sum(3,2))
e1.print_company()
e1.change_compnay("pelupa store")
# e1.print_company()
print(Emplyoyee.company)