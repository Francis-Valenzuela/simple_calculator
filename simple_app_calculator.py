while True:
    num_1 = float(input("Enter a number: "))
    num_2 = float(input("Enter another number: "))

    operation = input("Enter operation [+, -, *, /: ")
    if operation == "+":
        print(num_1 + num_2)
    elif operation == "-":
        print(num_1 - num_2)
    elif operation == "*":
        print(num_1 * num_2)
    elif operation == "/":
        print(num_1 / num_2)

    calculate_again = input("Do you want to calculate again? [y/n]: ")
    if calculate_again != "y":
        break