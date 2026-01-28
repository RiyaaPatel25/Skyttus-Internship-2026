#Calculate the remainder of two numbers
a = 20
b = 3
r = a % b 
print("Remainder is ", r)

#Check if number is even or odd 
a = int(input("Enter the number: "))
if a % 2 == 0:
    print("Number is Even.")
else:
    print("Number is Odd.")

#Compare two number and print the larger one
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if a > b:
    print("a is larger.")
else:
    print("b is larger.")

#A program to calculate the square and cube of a number
a = int(input("Enter the number: "))
s = a ** 2
c = a ** 3
print("Square of the number is ", s)
print("Cube of the number is ", c)

#Check if two entered number are equal
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if a == b:
    print("Numbers are Equal")
else:
    print("Numbers are not Equal")

#Take two numbers and print true if both are positive else false
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if a > 0 and b > 0: 
    print("True")
else:
    print("False")

#Program to convert float to integer
a = 5.4
r = round(a)
print(r)

#Take a number as string, convert into int, multiply by 10
a = input("Enter: ")
r1 = int(a)
r2 = r1 * 10
print("Integer number is ",r1)
print("Answer is ", r2)

#Program that uses and & or operators to check multiple conditions
age = int(input("Enter your age: "))
if age >= 18  and (age < 60 or age == 60):
    print("You are Eligible")
else:
    print("You're not Eligible")

#Divide two numbers and calculate quotient and remainder
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
q = a // b
r = a % b
print("Quotient is ", q)
print("Remainder is ", r)


