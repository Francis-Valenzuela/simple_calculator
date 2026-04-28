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