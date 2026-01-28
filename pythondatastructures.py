#create a tuple with 5 numbers
tuple = (1, 2, 3, 4, 5)
print(tuple)

#Access the third element in tuple
print(tuple[2])

#unpack a tuple into separate variables
num = (2, 3, 4)
a, b, c = num
print(a)
print(b)
print(c)

#create a set of 5 friuts
fruits = {"Mango", "Apple", "Banana", "Grapes", "Kiwi"}
print(fruits)

#add a new fruit to set
fruits.add("Pineapple")
print(fruits)

#Remove an element from set
fruits.remove("Kiwi")
print(fruits)

#Union of two set
set1 = {1, 2, 3}
set2 = {4, 5}
r = set1 | set2   # r = set1.union(set2)
print(r)

#intersection of two set
s1 = {1, 2, 5}
s2 = {2, 3}
r1 = s1 & s2     # r1 = set1.intersection(set2)
print(r1)

#check if one set is subset of another
s3 = {1, 2}
s4 = {1, 2, 3}
r2 = s3 <= s4    # r2 = s3.issubset(s4)
print(r2)

#convert a list with duplicate values into a set to remove duplicate
l = [1, 2, 3, 3, 4, 5, 5, 6]
s = set(l)
print(s)

#create a dictionary storing student names and marks 
students = {
    "Riya" : 95,
    "Maitri" : 92,
    "Krisha" : 97,
    "Ashiya" : 95
} 
print(students)

#Add a new key-value pair to an existing dictionary
students["Pooja"] = 91
print(students)

#Delete a key-value pair from a dictionary
del students["Krisha"]
print(students)

#Merge two dictionaries into one
dic1 = {"a": 1, "b": 2}
dic2 = {"c": 3, "d": 4}
merged = dic1 | dic2
print(merged)

#check if a key exist in a dictionary
print("Riya" in students )

#count word frequency in a given string using a dictionary
text = input("Enter a string: ")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)

#find key with maximum value in dictionary
student = {"a": 3, "b": 6, "d":4}
maxkey = max(student, key=student.get)
print(maxkey)

#reverse keys and values in dictionary
reverse_dict = {}
for key, value in student.items():
    reverse_dict[value] = key
print(reverse_dict)    

#update the value for a specific key
student["b"] = 9
print(student)

#convert a list of tuples into dictionary
data = [("Riya", 2), ("Riha", 6),("Pooja", 8)]
dict = dict(data)
print(dict)