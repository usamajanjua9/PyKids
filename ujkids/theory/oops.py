"""
ujkids - Object-Oriented Programming (OOP) in Python 🏗️
This module explains OOP concepts in Python with fun examples and exercises.
"""

def introduction():
    """
    📖 Lesson: What is Object-Oriented Programming (OOP)?
    """
    print("\n🚀 OOP is a way of organizing and structuring code using objects.")
    print("In OOP, we create **classes** that act like blueprints for objects.")
    print("Each object can have **attributes (data)** and **methods (actions).**")
    
    print("\n💡 Example: Think of a class as a recipe for making cakes 🍰")
    print("Each cake (object) follows the same recipe but can have different flavors (attributes).")


def classes_objects():
    """
    📖 Lesson: Creating Classes and Objects
    """
    print("\n📌 A class is like a blueprint, and an object is created using that blueprint.")

    print("\n✅ Example: Defining a simple class and creating objects")
    print("""
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Blue")

print("Car 1:", car1.brand, "in", car1.color, "color")
print("Car 2:", car2.brand, "in", car2.color, "color")
    """)

    print("\n💡 Challenge: Create a class `Dog` with attributes `name` and `breed`!")


def attributes_methods():
    """
    📖 Lesson: Attributes and Methods
    """
    print("\n📌 Objects have attributes (data) and methods (functions inside a class).")

    print("\n✅ Example: Adding methods to a class")
    print("""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "says Woof! 🐶")

dog1 = Dog("Buddy", "Labrador")
dog1.bark()
    """)

    print("\n💡 Challenge: Add a `walk` method to the `Dog` class that prints 'Dog is walking'.")


def constructor_self():
    """
    📖 Lesson: `__init__` Constructor and `self`
    """
    print("\n📌 The `__init__` method is called when we create a new object.")
    print("The `self` keyword represents the instance of the class.")

    print("\n✅ Example: Understanding `__init__`")
    print("""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 12)
print("Student Name:", student1.name)
print("Student Age:", student1.age)
    """)

    print("\n💡 Challenge: Modify the `Student` class to include a `grade` attribute.")


def inheritance():
    """
    📖 Lesson: Inheritance (Reusing Code)
    """
    print("\n📌 Inheritance allows one class to **inherit properties** of another.")

    print("\n✅ Example: Creating a child class")
    print("""
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(self.name, "makes a sound.")

class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof! 🐶")

dog = Dog("Buddy")
dog.sound()
    """)

    print("\n💡 Challenge: Create a `Bird` class that inherits from `Animal` and adds a `fly` method!")


def polymorphism():
    """
    📖 Lesson: Polymorphism (Different Behaviors for Same Method)
    """
    print("\n📌 Polymorphism allows different objects to use the same method differently.")

    print("\n✅ Example: Overriding a method")
    print("""
class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog barks!")

class Cat(Animal):
    def speak(self):
        print("Cat meows!")

dog = Dog()
cat = Cat()

dog.speak()  # Dog barks!
cat.speak()  # Cat meows!
    """)

    print("\n💡 Challenge: Create a `Car` class and override the `start_engine` method in a `ElectricCar` class!")


def mini_exercises():
    """
    📖 Mini Exercises for OOP
    """
    print("\n🎯 Mini Exercises")

    print("\n1️⃣ Create a `Person` class with attributes `name` and `age` and a method `introduce`.")

    print("\n2️⃣ Modify the `Dog` class to include an `age` attribute.")

    print("\n3️⃣ Create a `Vehicle` class and a `Car` class that inherits from it.")

    print("\n4️⃣ Write a program where a `Parent` class has a `greet` method, and a `Child` class overrides it.")

    print("\n💡 Try these in Python and test your knowledge!")


# Function to run all lessons in sequence
def run_oops():
    """Runs all OOP lessons"""
    introduction()
    classes_objects()
    attributes_methods()
    constructor_self()
    inheritance()
    polymorphism()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_oops()
