"""
ujkids - Modules and Packages in Python 📦
This module explains how to use and create modules in Python with fun examples and exercises.
"""

def introduction():
    """
    📖 Lesson: What are Modules?
    """
    print("\n🚀 Modules are files that contain Python code.")
    print("They help organize code and **reuse functions** easily.")
    
    print("\n💡 Example: Imagine a library 📚 where each book (module) contains different knowledge.")


def importing_modules():
    """
    📖 Lesson: Importing Built-in Modules
    """
    print("\n📌 Python has many built-in modules that provide extra features.")

    print("\n✅ Example: Using the `math` module")
    print("""
import math

print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)
    """)

    print("\n✅ Example: Using the `random` module")
    print("""
import random

print("Random number between 1 and 10:", random.randint(1, 10))
    """)

    print("\n💡 Challenge: Use the `datetime` module to print today's date!")


def creating_custom_modules():
    """
    📖 Lesson: Creating Custom Modules
    """
    print("\n📌 You can create your own module and import it into another file.")

    print("\n✅ Example: Creating a module `greetings.py`")
    print("""
# greetings.py
def say_hello(name):
    return f"Hello, {name}!"

# In another file:
import greetings

print(greetings.say_hello("Alice"))
    """)

    print("\n💡 Challenge: Create a module called `math_tools.py` with a function to add two numbers.")


def selective_imports():
    """
    📖 Lesson: Using `from` and `as` for Selective Imports
    """
    print("\n📌 You can import only specific functions from a module.")

    print("\n✅ Example: Using `from` to import only some functions")
    print("""
from math import sqrt, pi

print("Square root of 16:", sqrt(16))
print("Value of pi:", pi)
    """)

    print("\n✅ Example: Using `as` to rename a module")
    print("""
import random as rnd

print("Random number:", rnd.randint(1, 100))
    """)

    print("\n💡 Challenge: Import only the `choice` function from the `random` module and use it.")


def python_packages():
    """
    📖 Lesson: Understanding Python Packages
    """
    print("\n📌 A package is a collection of modules stored in a folder.")

    print("\n✅ Example: Creating a package `utilities`")
    print("""
# utilities/__init__.py  (Makes the folder a package)

# utilities/math_tools.py
def add(a, b):
    return a + b

# In another file:
from utilities import math_tools

print(math_tools.add(3, 5))  # 8
    """)

    print("\n💡 Challenge: Create a package `shapes` with a module for calculating areas!")


def mini_exercises():
    """
    📖 Mini Exercises for Modules
    """
    print("\n🎯 Mini Exercises")

    print("\n1️⃣ Use the `math` module to calculate the cosine of 45 degrees.")

    print("\n2️⃣ Generate a random number between 1 and 50 using the `random` module.")

    print("\n3️⃣ Create a module `greetings.py` with a function that says hello in different languages.")

    print("\n4️⃣ Write a program that imports `datetime` and prints the current time.")

    print("\n5️⃣ Create a package `animals` with modules `dogs.py` and `cats.py`.")

    print("\n💡 Try these in Python and explore modules and packages!")


# Function to run all lessons in sequence
def run_modules():
    """Runs all module-related lessons"""
    introduction()
    importing_modules()
    creating_custom_modules()
    selective_imports()
    python_packages()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_modules()
