try:
    a = int(input("Enter The First Number: "))
    b = int(input("Enter The Second Number: "))
    print("What kind of operation do you want to perform. Press + for addition \nPress - for subtraction\nPress / for division\n press * for multiplication")

    operation = input("Enter Operation: ")
    match operation:
        case "+":
            print(f"The result is: {a+b}")
        case "-":
            print(f"The result is: {a-b}")
        case "*":
            print(f"The result is: {a*b}")
        case "/":
            print(f"The result is: {a/b}")
        case default:
            print(f"There was an error")

except Exception as e:
    print("Enter a valid value of a and b")
