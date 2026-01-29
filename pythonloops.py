#Print numbers from 1 to 10
for i in range(1,11):
    print(i)

#Display multiplication table for a given number 
n = int(input("Enter a number: "))
for i1 in range(1,11):
    print( n, " x ", i1, " = ", n * i1 ) 

#Find factorial of a number
n1 = int(input("Enter a number: "))
fact = 1
for i2 in range(1,n1 + 1):
    fact *= i2
print("Factorial of a number is: ", fact)

#Generate first N fibonacci numbers
n2 = int(input("Enter a number: "))
a = 0
b = 1
for i3 in range(n2):
    print(a, end=" ")
    a, b = b, a + b,
    
#Check if number is prime
n3 = int(input("Enter a number: "))
if n3 > 1:
    for i3 in range(2,n3):
        if n3 % i3 == 0:
            print("Not prime number")
            break
    else:
        print("Prime number")
else:
    print("Not prime number")            

#Reverse a number 
n4 = int(input("Enter a number: "))
rev = 0
while n4 > 0:
    rev = rev * 10 + n4 % 10
    n4 //= 10
print(rev)    

#count digits in number
n5 = int(input("Enter a number: "))
count = 0
while n5 > 0:
    count += 1
    n5 //= 10
print(count)     
 
#Find sum of even numbers between 1 to 100
sum = 0
for i4 in range(1,101):
    if i4 % 2 == 0:
        sum += i4
print("Sum of even numbers is: ", sum)  

#Print a pyramid pattern
n6 = int(input("Enter number of rows: "))
for i5 in range(1, n6 + 1):
    print(" " * (n6 - i5) + "*" * (2 * i5 - 1))

#Find all divisor of a number
n7 = int(input("Enter a number: "))
for i6 in range(1,n7 + 1):
    if n7 % i6 == 0:
     print(i6)    