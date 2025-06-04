# while True:
#     try:
#         a = int( input(("enter number 1 ")))
#         b = int (input(("enter number 2 ")))
#         print(f"The division is  {a/b}")
#     except ValueError:
#         print("please don't perform bad typecast")
#     except ZeroDivisionError:
#         print("please don't divide by 0")

#     except Exception as e: 
#         print("some error occured!",e)

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

if b==0:
    raise ValueError("please don't divide by 0")

print(f"the division is {a/b}")