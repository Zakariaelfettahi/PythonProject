#A calculator with all four basic operations

def add(a: int, b: int ) -> int: #type hinting
    return a+b

def subtract(a: int, b: int) -> int:
    return a-b

def multiply(a: int,b: int) -> int:
    return a*b

def divide(a: int, b: int) -> float:
    return a/b

print("Welcome to the most useful calculator in the world!\nWe accept integers only.\n\nFor each operation you have to enter the name of the operation in English.\n")
operation = input("Enter operation (addition, subtraction, multiplication, division): ")

quit = 1 #set quit to 1 to start
while(quit == 1): #infinite loop
    if (operation!= "addition" and operation!= "subtraction" and operation!= "multiplication" and operation!= "division"): #comparative if statement
        print("Invalid operation, Abort mission.")
        exit() #halt execution
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if (operation == "division" and num2 == 0):
        print("Can't solve this one, Abort mission.")
        exit()

    match operation: #match case syntax
        case "addition":
            print("The result is : ", add(num1, num2))
        case "subtraction":
            print(f"The result is: {subtract(num1,num2)}") # different syntax f string
        case "multiplication":
            print(f"The result is: {multiply(num1,num2)}")
        case "division":
            print("The result is: ", divide(num1,num2))
    
    quit = int(input("Keep going? (1 for yes, 0 for no): "))
    while (quit not in [0,1]): #input validation
            quit= int(input(("Invalid input, try again.")))
    if quit == 0:
        exit();



#wow, such a useful project