def marks(**kwargs):
    #kwargs is a dicionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f" THe marks of {item} is {kwargs[item]}")

marks(shubham=32,ravi=33,prakss=34,marie=234)