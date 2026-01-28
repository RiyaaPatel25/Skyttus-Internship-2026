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
a = "Riya"
print(a.upper())

#Ask the user for their birthyear and calculate their current age
birthyear = int(input("Enter your birthyear: "))
currentyear = 2026
currentage = currentyear - birthyear
print("Your current age is ", currentage)

#program to swap the values of two variables
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
a, b = b, a
print("a = ",a)
print("b = ",b)

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
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
ave = (a + b)/2
print("Average of numbers is ", ave)