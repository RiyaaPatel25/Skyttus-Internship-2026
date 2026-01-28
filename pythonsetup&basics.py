# A program to print your name,age and city
name = "Riya"
age = 21
city = "Chikhli"
print(name, age, city)

#Take user input for two numbers and print their sum
a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = a + b
print("Sum: ", c)

#Convert temperature from Celsius to Fahrenheit 
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5 ) + 32
print("Temperature in Fahrenheit: ", fahrenheit)

#store your name in variable and print it in uppercase
name = "Riya"
print(name.upper())

#Ask the user for their birthyear and calculate their current age
birthyear = int(input("Enter your birthyear: "))
currentyear = 2026
currentage = currentyear - birthyear
print("Your current age is ", currentage)

#program to swap the values of two variables
a1 = float(input("Enter the value of a1 : "))
b1 = float(input("Enter the value of b1 : "))
a1, b1 = b1, a1
print("a1 = ",a1)
print("b1 = ",b1)

#Calculate the area of rectangle from user inputs
length = float(input("Enter the length of Rectangle: "))
width = float(input("Enter the width of Rectangle: "))
area = length * width
print("The area of Rectangle is ", area)

#Program to check if number is positive or negative 
num = int(input("Enter the number: "))
if num > 0:
    print("Number is Positive.")
elif num < 0:
    print("Number is Negative.")
else:
    print("Zero")   

#Ask for two numbers and print their average
a2 = float(input("Enter the value of a2: "))
b2 = float(input("Enter the value of b2: "))
ave = (a2 + b2)/2
print("Average of numbers is ", ave)