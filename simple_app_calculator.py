stored_value = None
while True:
    try:
        using_stored_value = "n"

        if stored_value is not None:
            using_stored_value = input("Do you want to stored value? [y/n]: ")

        if using_stored_value == "y":
            num_1 = stored_value
        else:
            num_1 = int(input("Enter a number: "))

        num_2 = float(input("Enter another number: "))

        operation = input("Enter operation [+, -, *, /]: ")
        if operation == "+":
            result = num_1 + num_2
        elif operation == "-":
            result = num_1 - num_2
        elif operation == "*":
            result = num_1 * num_2
        elif operation == "/":
            result = num_1 / num_2
        else:
            print("Please enter a valid operation")

        print("Result:", result)

        use_saved_value = input("Do you want to store value? [y/n]: ")
        if use_saved_value == "y":
            stored_value = result
    except ValueError:
        print("Please enter a number")
        continue
    except ZeroDivisionError:
        print("Cannot divide by zero")
        continue

    calculate_again = input("Do you want to calculate again? [y/n]: ")
    if calculate_again != "y":
        break