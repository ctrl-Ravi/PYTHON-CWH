# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False


# new = list(filter(is_greater_than_9,a))
    
a= [1,3,4,123,43,2,24,154,34,44,45]
new = list(filter(lambda x:x>9,a))

print(new)