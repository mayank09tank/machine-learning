
# 1.	Write a lambda function to merge two lists into a dictionary where one list represents keys and the other represents values. 
 
keys = ['name', 'age', 'city']
values = ['Mayank', 21, 'Jaipur']

merge_dict = lambda k, v: dict(zip(k, v))
print(merge_dict(keys, values))
# *****************************************************************************************************************************************************************************

# 2.	Create a class Product with instance variables name and price. Also, add a class variable discount_rate and a method to calculate the discounted price. 
class Product:
    discount_rate = 0.1  # 10% discount (Class Variable)

    def __init__(self, name, price):
        self.name = name  # Instance Variable
        self.price = price  # Instance Variable

    def discounted_price(self):
        return self.price - (self.price * Product.discount_rate)

# Example Usage
p1 = Product("Laptop", 50000)
print(f"Original Price: {p1.price}")
print(f"Discounted Price: {p1.discounted_price()}")
# *****************************************************************************************************************************************************************************

# 3.	Create a base class Shape with a method area(). Derive two subclasses Circle and Rectangle, each implementing their own area() method. (INHERITANCE)  
import math  # For Pi value

class Shape:
    def area(self):
        pass  # Abstract method (isko child class implement karega)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius  # πr²

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth  # l × b

# Example Usage
c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
# # *****************************************************************************************************************************************************************************

# # 4.	Create two base classes Person and Employee, and derive a class Manager from both. (MULTIPLE INHERITANCE)  
class Person:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

class Manager(Person, Employee):
    def __init__(self, name, emp_id, department):
        Person.__init__(self, name)  # Parent 1 ko initialize kiya
        Employee.__init__(self, emp_id)  # Parent 2 ko initialize kiya
        self.department = department

# Example Usage
m = Manager("Mayank", 101, "IT")
print(m.name, m.emp_id, m.department)
# # *****************************************************************************************************************************************************************************

# # 5.	Implement a function play_sound() that accepts different animal objects (Dog, Cat, Cow) and calls their make_sound() method dynamically. (POLYMORPHISM) 
class Dog:
    def make_sound(self):
        return "Bark"

class Cat:
    def make_sound(self):
        return "Meow"

class Cow:
    def make_sound(self):
        return "Moo"

def play_sound(animal):
    print(animal.make_sound())

# Example Usage
play_sound(Dog())  # Output: Bark
play_sound(Cat())  # Output: Meow
play_sound(Cow())  # Output: Moo
# # *****************************************************************************************************************************************************************************

# # 6.	Design a Car Rental System using Object-Oriented Programming (OOP) in Python. The system should include a Vehicle class and derived classes Car and Bike. Implement constructors and use inheritance to manage common and specific attributes
class Vehicle:
    def __init__(self, brand, model, price_per_day):
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day

    def get_details(self):
        return f"{self.brand} {self.model} - ₹{self.price_per_day}/day"

class Car(Vehicle):
    def __init__(self, brand, model, price_per_day, seats):
        super().__init__(brand, model, price_per_day)
        self.seats = seats
    
    def get_details(self):
        return super().get_details() + f" - {self.seats} seats"

class Bike(Vehicle):
    def __init__(self, brand, model, price_per_day, engine_cc):
        super().__init__(brand, model, price_per_day)
        self.engine_cc = engine_cc
    
    def get_details(self):
        return super().get_details() + f" - {self.engine_cc}cc engine"

# Example Usage
c = Car("Toyota", "Innova", 2000, 7)
b = Bike("Honda", "CBR", 1000, 250)

print(c.get_details())
print(b.get_details())
# # *****************************************************************************************************************************************************************************
