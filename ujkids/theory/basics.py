"""
ujkids - Basics of Python 🐍
This module introduces kids to Python programming in a simple and interactive way.
"""

def introduction():
    """
    📖 Lesson: Introduction to Python
    """
    print("\n🚀 Welcome to Python Programming!\n")
    print("Python is a simple and fun programming language used by many professionals and students.")
    print("It is great for games, web development, AI, and more!")
    print("\n💡 Fun Fact: Python was named after the comedy series 'Monty Python' 🎭")


def syntax_and_indentation():
    """
    📖 Lesson: Python Syntax and Indentation
    """
    print("\n📌 Python Syntax is very simple!")
    print("Unlike other languages, Python does not use { } or semicolons (;)")
    print("Instead, it uses proper spacing (indentation) to organize the code.")

    # Example:
    print("\n✅ Example of correct Python indentation:")
    print("""
def greet():
    print("Hello, welcome to ujkids!")  # Indented correctly

greet()
    """)

    print("\n❌ Wrong Indentation (This will cause an error!):")
    print("""
def greet():
print("Hello, welcome to ujkids!")  # No indentation (❌ ERROR)
    """)


def variables_and_data_types():
    """
    📖 Lesson: Variables and Data Types
    """
    print("\n📌 Variables are like containers that store information.")

    print("\n✅ Example:")
    print("""
name = "Alice"
age = 10
pi = 3.14
is_happy = True

print("Hello, my name is", name)
print("I am", age, "years old")
print("The value of pi is", pi)
print("Am I happy?", is_happy)
    """)

    print("\n🛠️ Try It Yourself: Change the values of name, age, and is_happy!")


def basic_input_output():
    """
    📖 Lesson: Taking Input and Printing Output
    """
    print("\n📌 Input allows users to enter data. Output displays it on the screen.")

    print("\n✅ Example:")
    print("""
name = input("Enter your name: ")
print("Hello", name, "! Welcome to Python.")
    """)

    print("\n💡 Fun Challenge: Ask the user for their favorite color and print a message!")


def operators():
    """
    📖 Lesson: Operators in Python
    """
    print("\n📌 Operators perform actions on values.")
    
    print("\n✅ Arithmetic Operators:")
    print("""
a = 5
b = 3

print("Addition:", a + b)  # 8
print("Subtraction:", a - b)  # 2
print("Multiplication:", a * b)  # 15
print("Division:", a / b)  # 1.67
print("Exponentiation:", a ** b)  # 5^3 = 125
    """)

    print("\n✅ Comparison Operators (True/False results):")
    print("""
x = 10
y = 20

print(x > y)  # False
print(x < y)  # True
print(x == y)  # False
print(x != y)  # True
    """)

    print("\n🛠️ Challenge: Try using different values and operators!")


def mini_exercises():
    """
    📖 Mini Exercises for Practice
    """
    print("\n🎯 Mini Exercises")
    
    print("\n1️⃣ Fix the indentation error in this code:")
    print("""
def say_hello():
print("Hello, World!")  # ❌ Fix the indentation here
    """)

    print("\n2️⃣ Declare variables for your name, age, and favorite color. Print them.")
    
    print("\n3️⃣ Write a program that asks the user for two numbers and prints their sum.")

    print("\n4️⃣ Use comparison operators to check if your age is greater than 18.")

    print("\n💡 Type the solutions in your Python editor and try running them!")


# Function to run all lessons in sequence
def run_basics():
    """Runs all basic Python lessons"""
    introduction()
    syntax_and_indentation()
    variables_and_data_types()
    basic_input_output()
    operators()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_basics()
