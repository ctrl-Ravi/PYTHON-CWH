def divide(a,b):

    try:
        c=a/b
        print(c)
        return c
    except Exception as e:
        print(e)
        return None

    # this is always excuted no matterif try compltely executed or not 
    finally:
        print("This is always excuted")


a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
divide(a,b)