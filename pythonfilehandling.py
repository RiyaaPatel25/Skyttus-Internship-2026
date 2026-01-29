#a program to read a file and display it contents
with open("Riya.txt", "r") as file1:
    print(file1.read())

#A program to count number of lines in a file
with open("Riya.txt", "r") as file2:
    lines = file2.readlines()
    print("Number of lines: ", len(lines))     

#A program to count how many each word appears in file
from collections import Counter
with open("Riya.txt", "r") as file3:
    words = file3.read().split()
word_count = Counter(words)
for word, count in word_count.items():
    print(word, ":" ,count)
        
#A program to write 5 user entered sentences in file
with open("Riya1.txt", "w",) as file4:
    for i in range(5):
        sentence = input("Enter a sentence: ")
        file4.write(sentence + "\n")
with open("Riya1.txt","r") as file4:
    print(file4.read())        

#A program to append a list of string in existing file
list = ["Riya", "Maitri", "Brij"]
with open("Riya1.txt", "a") as file5:
    for item in list:
        file5.write(item + "\n")  
with open("Riya1.txt","r") as file5:
    print(file5.read())                            

#A program to read a file and print only lines containing a specific word
w = input("Enter a word for searching in a file: ")
with open("Riya.txt","r") as file6:
    for lin in file6:
        if w in lin:
            print(lin.strip())

#A program to replace a specific word in file and save changes
old_word = "Brij"
new_word = "Sunitaben"

with open("Riya.txt", "r") as file7:
    content = file7.read()

content = content.replace(old_word , new_word)

with open("Riya.txt", "w") as file7:
    file7.write(content)

with open("Riya.txt", "r") as file7:
    print(file7.read())    

#Merge the content of two text files into third file
with open("Riya.txt","r") as f1, open("Riya1.txt","r") as f2, open("merged.txt" ,"w") as f3:
    f3.write(f1.read())
    f3.write("\n")
    f3.write(f2.read()) 
with open("merged.txt", "r")as f3:
    print(f3.read())   

#a program to read a CSV file and and display its content in a formatted way
import csv

with open("Riya1.csv","r") as file8:
    reader = csv.reader(file8)
    for row in reader:
        print("\t".join(row))

#A program to back up file by copying its content in another file        
with open("Riya1.txt", "r") as original, open("Riya2.txt","w") as another:
    another.write(original.read())
with open("Riya2.txt", "r") as another:
    print(another.read())    