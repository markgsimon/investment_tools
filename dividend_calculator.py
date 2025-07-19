# dividend_calculator.py

def get_float_input(prompt):
    """A helpter function to get a valid non-negative float from the user."""
    while True:
        try:
            # Get input and remove any comas
            value_str = input(prompt).replace(',','')
            value = float(value_str)
            if value >= 0:
                return value
            else:
                print("Input annot be negative. Please enter a positive number or zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 10.50 or 20,000.")

def get_int_input(prompt):
    """A helper function to get a valid positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

