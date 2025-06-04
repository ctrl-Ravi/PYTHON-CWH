a = 34
b = "34"
d = 223

print(a)
print(type(a))
print(b)
print(type(b))

# Convert b to an integer
c = int(b)
print("convert",c)
print(type(c))

e= str(d)
print(e)
print(type(e))

# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int) # Output: 10
# Convert integer to string
num = 25
num_str = str(num)
print(num_str) # Output: "25"
# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int) # Output: 3

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")

