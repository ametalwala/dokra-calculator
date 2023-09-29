print("Welcome to the Dokra Calculator!")
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Define dictionary to map letters to numbers
letter_to_digit = {
    'a': 1, 
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5, 
    'f': 6, 
    'g': 7, 
    'h': 8, 
    'i': 9,
    '0': 0
}

# Define a function to map a digit back to a letter
def digit_to_letter(digit):
    for key, value in letter_to_digit.items():
        if value == digit:
            return key
    return str(digit) # Return the digit iteself if not found 


while True: 
    # taking input from user
    choice = input("Enter choice(1/2/3/4): ")
    
    # confirming choice is one of the four options
    if choice in ('1', '2', '3', '4'): 
        try: 
            letter_num1 = input("Enter first dokra (a-i; 0 = 0): ").lower()
            letter_num2 = input("Enter second dorka (a-i; 0 = 0): ").lower()
            
            current_digit = letter_to_digit.get(letter_num1, 0)
            digit = letter_to_digit.get(letter_num2, 0)
            
            operator_mapping = {'1': '+', '2': '-', '3': '*', '4': '/'}
            operator = operator_mapping[choice]
            
            # Function to evalutate expressions
            def evaluate_expression(current_digit, operator, digit):
                if choice == '1': 
                    return current_digit + digit
                elif choice == '2':
                    return current_digit - digit
                elif choice == '3': 
                    return current_digit * digit
                elif choice == '4':
                    if digit == 0:
                        print("Division by zero is not allowed.")
                        return None
                    return current_digit / digit
            result = evaluate_expression(current_digit, operator, digit)
                
            if result is not None: 
                result_letter = digit_to_letter(result)
                print(f"{letter_num1} {operator} {letter_num2} = {result_letter}")    
        except ValueError: 
            print("Invalid input. Please enter a valid dokra")
        except ZeroDivisionError: 
            print("Division by zero is not allowed.")
        except Exception as e:
            print("An error occurred:", e)
            # calling letter to number dict
                
        # Asking if user wants to perform additional calculations
        # breaking while loop if answer is no 
        next_calculation = input("Let's do another one? (bro pls/nah): ")
        if next_calculation.lower() == "nah": 
            break 
    else: 
        print("Invalid")