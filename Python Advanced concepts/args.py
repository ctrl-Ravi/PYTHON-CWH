def sum(*args):
    # args will be a tuple of all the values passed to sum
    print(args)
    total =0
    for item in args:
        total+=item
    return total

print(sum(23,23,233,23))