#Create a car class with attribute like brand, model, speed and method to accelerate/break
class Car:
    def __init__(self,brand,model,speed = 0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, increase):
        self.speed += increase
        print("Car speed after Acceleration: ",self.speed)

    def brake(self,decrease):
        self.speed -= decrease
        print("Car speed after braking: ",self.speed)

car = Car("Toyota","Camry")
car.accelerate(30)
car.brake(10)    

#Create a bank account with deposit and withdraw method
class Account:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Balance in Account after deposit amount : ",self.balance)

    def withdraw(self,amount):
        self.balance -= amount
        print("Balance in Account after withdraw amount: ",self.balance)

account = Account(20000)
account.deposit(6000)
account.withdraw(2000)

#Create a student class with method to calculate the average marks
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)
    
student = Student("Riya",(88,90,92))
print("Average mark: ", student.average())

#Create a rectangle class with method to find area and perimeter
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width 

    def perimeter(self):
        return self.length + self.width   

r = Rectangle(20,10)
print("Area of Rectangle is ",r.area())
print("Perimeter of Rectangle is ", r.perimeter())   

#Create a employee class that displays salary details
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name: ",self.name)
        print("Salary: ",self.salary)

e = Employee("Riya","25000")
e.display()            

#Create a book class to store title,author and price and display it
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book Title: ",self.title)    
        print("Book Author: ",self.author)
        print("Book Price: ",self.price)

b = Book("Ramayan","Valmiki",400)
b.display()        

#Create a circle class to find area and circumference
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 2 * 3.14 * self.radius

    def circumference(self):
        return 4 * 3.14 * (self.radius ** 2)

cir = Circle(4)
print("Area of circle is ",cir.area())
print("Circumference of circle is ",cir.circumference())            

#Create a laptop class with method to apply discount on price
class Laptop:
    def __init__(self,price,rate):
        self.price = price
        self.rate = rate

    def discount(self):
        return self.price * self.rate / 100
    
    def after_discount(self):
        return self.price - self.discount

l = Laptop(50000,12)
print("Laptop price before discount: ", l.price)
print("Laptop price after discount: ",l.discount())  

#Create a flight class with seat booking functionallity
class Flight:
    def __init__(self,seats):
        self.seats = seats
    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked")
        else:
            print("No seats available")

f = Flight(1)
f.book_seat()
f.book_seat()                    

#Create a shop card with method to add and list products
class Shop:
    def __init__(self):
        self.products = []

    def add_products(self,product):
        self.products.append(product)

    def show_products(self):
        print("Products: ",self.products)

shop = Shop()
shop.add_products("Book")
shop.add_products("Pen")
shop.show_products()                