#Calculate the remainder of two numbers
a = 20
b = 3
c = a % b 
print("Remainder is ", c)

#Check if number is even or odd 
d = int(input("Enter the number: "))
if d % 2 == 0:
    print("Number is Even.")
else:
    print("Number is Odd.")

#Compare two number and print the larger one
e = int(input("Enter the value of e: "))
f = int(input("Enter the value of f: "))
if e > f:
    print("e is larger.")
else:
    print("f is larger.")

#A program to calculate the square and cube of a number
g = int(input("Enter the number: "))
square = g ** 2
cube = g ** 3
print("Square of the number is ", square)
print("Cube of the number is ", cube)

#Check if two entered number are equal
h = int(input("Enter the value of h: "))
i = int(input("Enter the value of i: "))
if h == i:
    print("Numbers are Equal")
else:
    print("Numbers are not Equal")

#Take two numbers and print true if both are positive else false
j = int(input("Enter the value of j: "))
k = int(input("Enter the value of k: "))
if j > 0 and k > 0: 
    print("True")
else:
    print("False")

#Program to convert float to integer
l = 5.4
m = round(l)
print(m)

#Take a number as string, convert into int, multiply by 10
r = input("Enter: ")
r1 = int(r)
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
a1 = int(input("Enter the value of a: "))
b1 = int(input("Enter the value of b: "))
quotient = a // b
remainder = a % b
print("Quotient is ", quotient)
print("Remainder is ", remainder)


