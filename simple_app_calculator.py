while True:
    try:
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
    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("Cannot divide by zero")
        continue

    calculate_again = input("Do you want to calculate again? [y/n]: ")
    if calculate_again != "y":
        break