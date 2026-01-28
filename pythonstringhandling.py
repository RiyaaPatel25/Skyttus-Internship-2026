#Take a string input and print its length
a = input("Enter a string: ")
print(len(a))

#Convert a sentence to lowercase
b = input("Enter a sentence: ")
print(b.lower())

#Replace spaces with underscore in a string
c = input("Enter a String: ")
print(c.replace(" ","_"))

#Extract the first and last character from a string
d = input("Enter a string: ")
print("First character: ", d[0])
print("Last character: ", d[-1])

#Reverse a string using slicing
e = input("Enter a string: ")
print(e[::-1])

#Count howmany times a letter appears in string
f = input("Enter a string: ")
g = input("Enter a letter: ")
print(f.count(g))

#Check if a word present in sentence
h = input("Enter a sentence: ")
i = input("Enter a Word: ")
print(i in h)

#Take name & age and print using f-string formating
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and my age is {age}.")

#Remove extra spaces from start and end of a string
j = input("Enter a string: ")
print(j.strip())

#Join a list of words into a single string with - between them
words = ["Riya","Patel"]
print("-".join(words))

#Create a list of your Favourite Movie
movies = ["Intersteller", "Inception","Arrival","Gravity","Oblivin"]
print(movies)

#Add a new movie to the list
movies.append("Blade Runner 2049")
print(movies)

#Remove the first movie from the list
movies.pop(0)
print(movies)

#sort a list of number in ascending order
numbers = [3, 5, 2, 1, 4]
numbers.sort()
print(numbers)

#Reverse a list
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)

#Find the largest number in a list
print(max(nums))

#Merge two list into one
merged = nums + numbers
print(merged)

#Access the last element of list without using index number
list = [1, 3, 6, 8]
print(list[-1]) 

#Create a nested list and access a specific inner element
nested = [1, [2, 3], [4, 5]]
print(nested[2][1])

#Count howmany times an element appears in a list
list1 = [1, 3, 5, 2, 3, 6, 3, 2]
print(list1.count(3))