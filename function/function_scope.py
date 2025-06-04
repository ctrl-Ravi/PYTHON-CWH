def sum(a,b):
    # a and b are local variables you can't access them outside the function
    c=a+b
    z=1 # it creates a loval variable calle z which is destroyed after this funcion returns
    return c
def greet():
    z = 234 # local varible
    print("hello world")
z=6 # z is the global variable 
print(sum(4,6))
print(z)