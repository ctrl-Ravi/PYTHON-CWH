def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"hello {a}")

'''
It replaces the unction say_hello with func
def decorator(func):
        def wrapper(a):
            for i in range(n):
                say_hello(a)
        return wrapper
    return decorator
'''

say_hello("ravi")