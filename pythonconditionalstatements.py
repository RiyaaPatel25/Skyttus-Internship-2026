#check if a person is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("Your are eligible to vote.")
else:
    print("Your are not eligible to vote.")    

#Grade calculator
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("C") 

#Simulate a traffic light 
light = input("Enter the color of signal light: ").lower()
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go") 
else:
    print("Invalid signal light")           

#ATM withdrawal check
balance = int(input("Enter your total balance: "))
amount = int(input("Enter withdrawal amount: "))
if amount <= balance:
    print("Sufficient balance")
else:
    print("Insufficient balance")   

#Check if a number is positive, negative or zero
n = int(input("Enter a number: "))
if n > 0:
    print("Number is Positive")
elif n < 0:
    print("Number is Negative")
else:
    print("Zero") 

#Check if a number lies within a range
num = int(input("Enter a number: "))
if num >= 0 and num <= 100:
    print("Number is within a range")  
else:
    print("Number is out of range")   

#Username and password verification
username = input("Enter username: ")
password = input("Enter password: ")
if username == "riya" and password == "riya@123":
    print("Login Successfully")
else:
    print("Invalid username and password")   

#Electricity bill based on units consumed
unit = int(input("Enter the consumed units: "))
if unit <= 100:
    bill = unit * 2
elif unit <= 200:
    bill = unit * 3
else:
    bill = unit * 4
print("Electricity bill: ", bill)      

#simple calculator
n1 = float(input("Enter the first value: "))
n2 = float(input("Enter the second value: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print(n1 + n2)
elif operator == "-":
    print(n1 - n2)
elif operator == "*":
    print(n1 * n2)
elif operator == "/":
    print(n1 / n2)
else:
    print("Invalid operator")   

# Check type of triangle(Equilateral, isosceles, scalene)
a = float(input("Enter the value of first side: "))
b = float(input("Enter the value of second side: "))
c = float(input("Enter the value of third side: ")) 
if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")                        