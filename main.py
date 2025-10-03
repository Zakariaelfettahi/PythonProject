#A calculator with all four basic operations

def Calculate(num1, num2, operation):  #funtion to calculate
    match operation: #match case
        case 1:
            return num1 + num2  #num1 num2 are stored in the stack
        case 2:
            return num1 - num2
        case 3:
            return num1 * num2
        case 4:
            return num1 / num2 #result is stored in the heap

def AskOperation(): #function to ask operation
    operation = 0  #initialize operation
    while operation not in [1,2,3,4,5]: #while loop
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
        try:                                                                                                
            operation = int(input("Enter the number corresponding to the operation you want to perform: ")) #try until user provides valid input
        except ValueError:
            operation = int(input("Invalid input. Please enter a valid number:"))
            continue    
    return operation

print("Welcome to the most useful calculator in the world!\nFor each operation you have to enter number corresponding to it.\n")
operation = AskOperation() #Ask operation returns an integer that needs to be stored stored in DATA, therefore the operation = AskOperation() statement
while operation != 5:
    try:
        num1 = float(input("Enter the first number: ")) #float input
        num2 = float(input("Enter the second number: ")) #float input
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if operation == 4 and num2 == 0: #division by zero check
        print("Error: Division by zero is not allowed.")
        continue
    result = Calculate(num1, num2, operation)
    print(f"The result is: {result}\n")
    operation = 0 #reset operation
    operation = AskOperation() #reupdate operation

#wow, such a useful project