class SimpleCalculator:
    def calculate(self, num_1, num_2, operation):
        if operation == "+":
            return num_1 + num_2
        elif operation == "-":
            return num_1 - num_2
        elif operation == "*":
            return num_1 * num_2
        elif operation == "/":
            return num_1 / num_2
        else:
            print("Please enter a valid operation")
