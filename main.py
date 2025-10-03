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

if (operation!= "addition" and operation!= "subtraction" and operation!= "multiplication" and operation!= "division"): #comparative if statement
    print("Invalid operation, Abort mission.")
    exit() #halt execution

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match operation: #match case syntax
    case "addition":
        print("The result is : ", add(num1, num2))
    case "subtraction":
        print("The result is: ", subtract(num1,num2))
    case "multiplication":
        print("The result is: ", multiply(num1,num2))
    case "division":
        print("The result is: ", divide(num1,num2))


#wow, such a useful project