from simple_app_calculator import SimpleCalculator
class CalculatorRunner(SimpleCalculator):
    def __init__(self):
        self.stored_value = None

    def run(self):
        while True:
            try:
                using_stored_value = 'n'

                if self.stored_value is not None:
                    using_stored_value = input("Do you want to stored value? [y/n]: ").strip().lower()

                if using_stored_value == 'y':
                    num_1 = self.stored_value
                else:
                    num_1 = float(input("Please enter a number: "))
                num_2 = float(input("Please enter another number: "))

                operation = input('Enter operation [+, -, *, /]: ')

                result = self.calculate(num_1, num_2, operation)

                print('Result: ', result)

                use_saved_value = input("Do you want to store value? [y/n]: ").strip().lower()
                if use_saved_value == 'y':
                    self.stored_value = result

            except ValueError:
                print("Please enter a numeric value or operation")
                continue
            except ZeroDivisionError:
                print("Please enter a numeric value")
                continue

            calculate_again = input("Do you want to calculate again? [y/n]: ").strip().lower()
            if calculate_again != 'y':
                print('Thank You')
                break
if __name__ == '__main__':
    calculator = CalculatorRunner()
    calculator.run()