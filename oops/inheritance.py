class Animal: #Parent class (superclass)
    location = "Australia"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Speaking NOw.....")

class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        super().speak() # We are using the speak function of the parent class
        print("woof!")

# a = Animal("Dog")
# a.speak()
d = Dog("Bruno")
d.speak()
print(d.location)