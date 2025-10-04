#A calculator with all four basic operations

def Calculator():
    finished = False
    result = 0
    operator = ''

    number_input = input("Enter a number or '=' to finish: ")
    if number_input == '=':
        print("No calculation performed.")
        return 0
    else:
        number = float(number_input)
        result = number

    while not finished:
        operator = input("Enter an operator (+, -, *, /) or '=' to finish: ")

        if operator == '=':
            finished = True
            print("Final result:", result)
            return result

        next_number = float(input("Enter another number: "))

        if operator == '+':
            result += next_number
        elif operator == '-':
            result -= next_number
        elif operator == '*':
            result *= next_number
        elif operator == '/':
            if next_number != 0:
                result /= next_number
            else:
                print("Error: Division by zero.")
        else:
            print("Invalid operator. Please try again.")

        print("Current result:", result)

        

print(Calculator())


#wow, such a useful project