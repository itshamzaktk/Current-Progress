# # print(): Function for displaying output to the terminal or console. Called by parentheses.
# print("Hi There! This is my first python code!")
# print("*" * 40)
# A = 10
# B = 20
# print(
#     f"This is a formatted print statement {A+B}, writing f(format) before the print statement allows us to use variables inside the string."
# )
# print("*" * 125)

# print(
#     r"This is a raw print statement, writng r(raw) brfore the print statement allows us to use special characters and escape sequences without getting an error like this \n"
# )

# # Code Linting: Code analyzing for errors and style issues.

# print("Code Linting")

# 2 + 2

# Code Formatting: Writing code in a consistent style to improve readability.

print("Code Formatting")
# Variables: Containers for storing data values.There are different datatypes available.
X = 1  # Integer.
Y = 2.45  # Float
String = "Hello World!"  # String/Object
Is_Boolean = True  # Boolean
Set = {1, 2, 3}  # Set : Immutable datatype storing unique elements.
Null = set()  # Null/Empty set.
LIST = [4, 5, 6]  # List : Mutable datatype storing any values.
Tuple = (1, 2, 3)  # Tuple : Immutable list of elements.
Dict = {"Key1": "Value1", "Key2": "Value2"}
Empty_Dict = {}
print(type(X))
print(type(Y))
print(type(String))
print(type(Is_Boolean))
print(type(Set))
print(type(Null))
print(type(LIST))
print(type(Tuple))
print(type(Dict))
print(type(Empty_Dict))

# Type Conversion: Only possible in similar category of datatypes.Converting one datatype to another, there are 2 types of conversions:
# Implicit/Auto conversion done by interpreter and Explicit/Manual converion done by users.
# Implicit Conversion:
Add = X + Y
print(Add)
print(type(Add))
# # String Functions/Methods: Functions that can be used on strings to perform various operations.

# print("String Functions/Methods")
# print("*" * 20)
# print(String)
# print(len(String))  # len(): Function for getting the length of a string.
# print(String[0])  # Accessing the first character of the string.
# print(String[-1])  # Accessing the last character of the string.
# print(String[0:5])  # Accessing a substring of the string.
# print(String[:5])  # Accessing a substring of the string from the beginning.
# print(String.upper())  # Converting the string to uppercase.
# print(String.lower())  # Converting the string to lowercase.
# print(
#     String.replace("Hello", "Hi")
# )  # Replacing a substring in the string with another substring.
# print(String.strip())  # Removing whitespace from the beginning and end of the string.
# print(String.lstrip())  # Removing whitespace from the beginning of the string.
# print(String.rstrip())  # Removing whitespace from the end of the string.
# String2 = "hi there!"
# print(String2.capitalize())  # Capitalizing the first character of the string.
# print(String2.title())  # Capitalizing the first character of each word in the string.


# # Numerical Operations: Performing mathematical operations on numbers.

# print("Numerical Operations")
# print("*" * 20)
# A = 10
# B = 20
# C = 2.7
# Sum = A + B
# Sub = B - A
# Mul = A * B
# Div = B / C
# Div_Int_Result = B // C
# Remainder = B % C
# Exponent = A**C
# print(f"Sum: {Sum}")
# print(f"Subtraction: {Sub}")
# print(f"Multiplication: {Mul}")
# print(f"Division: {Div}")
# print(f"Integer Division Result: {Div_Int_Result}")
# print(f"Remainder: {Remainder}")
# print(f"Exponent: {Exponent}")
# Complex_Number = 10 + 5j
# print(f"Complex Number: {Complex_Number}")

# # Importing Libraries/Modules : Importing external libraries or modules to use their functions and classes.
# # Importing math library to use mathematical functions.
# import math  # math is an object

# # Taking User Input: Using the input() function to get input from the user.
# print("Taking User Input")
# print("*" * 20)

# User_Input1 = int(input("Enter an integer: "))
# User_Input2 = float(input("Enter a float: "))
# print(f"User Input 1: {User_Input1}")
# print(f"User Input 2: {User_Input2}")

# # Finding euclidean distance between two points using math.dist() method from math.
# # Euclidean distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
# X1 = float(input("Enter X coordinate of point 1: "))
# Y1 = float(input("Enter Y coordinate of point 1: "))
# X2 = float(input("Enter X coordinate of point 2: "))
# Y2 = float(input("Enter Y coordinate of point 2: "))

# Eucl_Dist = math.dist((X1, Y1), (X2, Y2))
# print(f"Euclidean Distance: {Eucl_Dist}", end="\n\n") # Added additional end="\n\n" to add two new lines after the output for better readability.

# # Comparison Operators: Using comparison operators to compare values and return a boolean result.
# print("Comparison Operators")
# print("*" * 20)

# print(f"Is {User_Input1} greater than {User_Input2} ? : {User_Input1 > User_Input2}")
# print(f"Is {User_Input1} less than {User_Input2} ? : {User_Input1 < User_Input2}")
# print(f"Is {User_Input1} equal to {User_Input2} ? : {User_Input1 == User_Input2}")
# print(f"Is {User_Input1} not equal to {User_Input2} ? : {User_Input1 != User_Input2}")
# print(
#     f"Is {User_Input1} greater than or equal to {User_Input2} ? : {User_Input1 >= User_Input2}"
# )
# print(
#     f"Is {User_Input1} less than or equal to {User_Input2} ? : {User_Input1 <= User_Input2}"
# )
# print("\n")

# # If-Else Statements: Using if-else statements we can check conditions and control the flow of the program based on those conditions.
# print("If-Else Statements")
# print("*" * 20)

# Input1 = float(input("Enter Temperature in Celsius: "))
# if Input1 > 30:
#     print("It's a hot day!")
# else:
#     print("It's a cold day!")
# print("\n")

# Input2 = float(input("Enter Mark: "))
# if Input2 >= 90:
#     print("Grade: A")
# elif Input2 >= 80:
#     print("Grade: B")
# elif Input2 >= 70:
#     print("Grade: C")
# elif Input2 >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")
# print("\n")

# Input3 = float(input("Enter Marks: "))
# # Ternary Operator: A shorthand way of writing an if-else statement in a single line.
# Grade = "Grade : A" if Input3 >= 90 else "Grade : B" if Input3 >= 80 else "Grade : C" if Input3 >= 70 else "Grade : D" if Input3 >= 60 else "Grade : F"

# print(Grade, end="\n\n")  # Added additional end="\n\n" to add two new lines after the output for better readability.

# # Logical Operators: Using logical operators to combine multiple conditions and return a boolean result.
# print("Logical Operators")
# print("*" * 20)

# Age = int(input("Enter Age: "))
# License = str(input("Do you have a driving license? (Yes/No): "))
# Yes = True
# No = False
# if Age >= 18 and License == "Yes":
#     print("You are eligible to drive!")
# else:
#     print("You are not eligible to drive!")
# print("\n")

# # Chaining Comparison Operators: Using comparison operators in a chain to compare multiple values.
# print("Chaining Comparison Operators")
# print("*" * 20)

# Number = int(input("Enter a number: "))
# if 0 < Number < 100:
#     print(f"{Number} is between 0 and 100")

# # Loops: Using loops to repeat a block of code multiple times based on a condition.
# print("Loops")
# print("*" * 10)

# List = [1, 2, 3, 4, 5]
# for ele in List:
#     print(
#         ele, end=" "
#     )  # Added end=" " to print all elements in a single line with space in between.
# print("\n")

# print("Even Numbers From 0 to 10:", end=" ") # Prints this statement and then prints the even numbers from 0 to 10 in a single line with space in between.
# for i in range(0, 10, 2):
#     print(i, end=" ")

# # Nested Loops: Using loops inside another loop to perform more complex iterations.
# for i in range(0, 10, 2):
#     for j in range(1, 10, 2):
#         print(f"( {i} , {j} )")
# print("\n")

# for char in "Python":
#     print(char, end=" ")
# print("\n")

# Number = 100
# while Number > 0:
#     print(Number, end=" ")
#     Number //= 2

# print("\n")


# Command = ""
# while Command.upper() != "EXIT":
#     Command = str(input("Type Command:"))
#     if Command.upper() == "EXIT":
#         print("Exiting the program...")


# # Functions: Named block of code that can be called to perform a specific function anywhere in the program when needed.
# def Greeting(Name):
#     print(f"Greetings {Name}!")


# Name = str(input("Enter Name: "))  # Taking user input for the name.
# Greeting(Name)  # Calling the function and passing the argument "User" to it.


# def Factorial(Number):
#     if Number == 0 or Number == 1:
#         return 1
#     else:
#         return Number * Factorial(Number - 1)


# Number = int(input("Enter Number To Calcalte Its Factorial: "))
# Result = Factorial(Number)
# print(f"Factorial Of {Number} Is : {Result}")

# List = [4, 5, 6, 7]
# def Pack_Unpack(*Numbers):  # * Collects all positional arguments passed to the function to form a tuple.
#     print(Numbers)

# Pack_Unpack(1, 2, 3, 4)

# Pack_Unpack(*List) # * Unpacks the elements of the list into separate arguments.
