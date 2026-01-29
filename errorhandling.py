#a program to handle division by zero error
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    d = a / b
    print("Result: ", d)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")    

#a program to handle invalid integer input
try:
    num = int(input("Enter a number: "))
    print("The number is ", num)
except ValueError:
    print("Error: Invalid integer input")    

#A program to open a file and handle the "File not found" error
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not Found")        

#A program to demonstrate multiple exception blocks
try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a another number: "))
    r1 = n1 / n2
    print("Result: ", r1)
except ValueError:
    print("Error: Invalid integer input")
except ZeroDivisionError:
    print("Error : Division by zero is not allowed")    

#A program to use finally for resource cleaner
file = None
try:
    file = open("data.txt", "r")     
    print(file.read())
except FileNotFoundError:
    print("Error: File not found")
finally:
    if file:
        file.close()
        print("File closed") 

#A program to create a custom exception for invalid age (<18)
class InvalidAgeError(Exception):
    pass  
try:
    age = int(input("Enter your age: "))
    if age < 18 :
        raise InvalidAgeError("Age must be 18 or above") 
    print("Access Granted")
except InvalidAgeError as e:
    print("Error: ", e)

#A program to handle IndexError when accessing a list
list = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter a index: "))
    print(list[index])
except IndexError:
    print("Error: Index is out of range")  

#A program that takes two numbers and handles all possible error
try:
    m = float(input("Enter a number: "))
    n = float(input("Enter a another number: "))
    r = m / n
    print("Result: ", r)
except ValueError:
    print("Error: Invalid integer number")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except Exception as e:
    print("Error: ", e)  

#A program to log errors to a file instead of printing them 
import logging

logging.basicConfig(filename = "errors.log", level = logging.ERROR)

try:
    x = int("abc")
except ValueError as e:
    logging.error("ValueError occured", exc_info = True)

#A program that validates an email format and raises an exception for invalid ones
import re

class InvalidEmailError(Exception):
    pass
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern,email):
        raise InvalidEmailError("Invalid email format")
    
try:
    email = input("Enter Email: ")
    validate_email(email)
    print("Valid Email")
except InvalidEmailError as e:
    print("Error: ", e)

    
    