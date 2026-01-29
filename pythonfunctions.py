#function to check if a number is prime 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 2 == 0:
            return False
    return True   
print(is_prime(5))

#Function to reverse a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("riya"))

#Function to find the factorial 
def factorial(f):
    if f < 0:
        return None
    
    result = 1
    for i in range(1, f + 1):
        result *= i
    return result

print(factorial(5))

#function to calculate simple interest
def interest(p, r, n1):
    return (p * r * n1)/100

print(interest(1000,2,2))

#Function to check if word is palindrome
def is_palindrome(word):
    return word == word[::-1]
        
print(is_palindrome("madam"))  

#Function to count vowels in a string
def count_vowels(str):
    vowels = ("aeiouAEIOU")
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Riya")) 

#Function to merge two lists
def merge_lists(list1, list2):
    return list1 + list2
print(merge_lists((1, 2, 3), (3, 4, 5)))

#Function to find gcd of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print(gcd(4,6))
    
#Function to find area of an rectangle
def area_rectangle(length, width):
    return length * width
print(area_rectangle(3,2)) 

#Function to check armstrong number
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num
print(is_armstrong(153))