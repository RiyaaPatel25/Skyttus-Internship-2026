#Create a base class Animal and subclasses dog and cat
class Animal:
    def speak(self):
        print("Animals make a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.speak()
c.speak()

#Create a heirarchy for vehicle - car - electricCar
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("ElectricCar is charging")

e = ElectricCar()
e.start()
e.drive()
e.charge() 

#Implement method override in a base and derived class
class Shape:
    def area(self):
        print("Area is not defined")

class Rectangle(Shape):
    def area(self):
        print("Area = length * width") 

r = Rectangle()
r.area()               

#Demonstrate multiple inheritance with two parent classes
class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Coding")

child = Child()
child.skills() 

#Create a polymorphic function that works with different shapes
class Circle:
    def draw(self):
        print("Drawing circle")

class Square:
    def draw(self):
        print("Drawing square")

def render(shape):
    shape.draw()

render(Circle())
render(Square())

#Create a bank system with SavingsAccount and CurrentAccount classes
class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,amount):
        pass

class SavingsAccount(BankAccount):
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("SavingsAccount balance: ",self.balance)
        else:
            print("Insufficient Balance")

class CurrentAccount(BankAccount):
    def withdraw(self,amount):
        self.balance -= amount
        print("Current Balance: ",self.balance)

sav = SavingsAccount(3000)
curr = CurrentAccount(1500)

sav.withdraw(2000)
curr.withdraw(500)

#Create a class with private attribute and getter/setter methods
class Employee:
    def __init__(self):
        self.__salary = 0

    def set_salary(self,amount1):
        self.__salary = amount1

    def get_salary(self):
        return self.__salary

emp = Employee()
emp.set_salary(30000)
print("Salary: ", emp.get_salary())

#Create a teacher and student class to show inheritance
class Teacher:
    def __init__(self,name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching")

class Student(Teacher):
    def study(self):
        print(self.name, "is studying")

stu = Student("Riya")
stu.teach()
stu.study() 

#Create a MusicPlayer class and and subclass spotify to override play method
class MusicPlayer:
    def play(self):
        print("Music Playing")

class Spotify(MusicPlayer):
    def play(self):
        print("Music playing on Spotify")

sp = Spotify()
sp.play()

#Demonstrate the use of super() in inheritence
class Person:
    def __init__(self,name):
        self.name = name 

class Employee(Person):
    def __init__(self, name,email):
        super().__init__(name)
        self.email = email 

    def show(self):
        print("Name: ", self.name)
        print("Email: ", self.email)    

e = Employee("Riya","riya@gmail.com")
e.show()
