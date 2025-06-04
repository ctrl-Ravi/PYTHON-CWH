# Decorator is a function that takes a function, it creates a new functon inside its body (wrapper). THen it retruns that new function 
def decorator(func):
    def wrapper():
        print("I am about to execute a fucntion.....")
        func()
        print("i have executed this function......")
    return wrapper


@decorator
def say_hello():
    print("hello!")
    
say_hello()

'''
f will look something like this 
def f():
    print("I am about to execute a fucntion.....")
    print("hello")
    print("i have executed this function......")

'''

# f= decorator(say_hello)
# f()