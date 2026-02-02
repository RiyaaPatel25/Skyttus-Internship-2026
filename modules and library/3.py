#Use random module to generate 5 random integers

import random

numbers = []
for i in range(5):
    numbers.append(random.randint(1,100))

print(numbers)