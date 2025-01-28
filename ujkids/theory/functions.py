"""
ujkids - Functions in Python 🔄
This module explains how functions work in Python with fun examples and exercises.
"""

def introduction():
    """
    📖 Lesson: What are Functions?
    """
    print("\n🚀 Functions help us organize code and avoid repetition.")
    print("Think of functions like a **recipe** 📖 that tells Python how to do something.")
    
    print("\n✅ Example of a simple function:")
    print("""
def greet():
    print("Hello! Welcome to ujkids! 🎉")

greet()  # Calling the function
    """)

    print("\n💡 Challenge: Try changing the greeting message!")


def defining_functions():
    """
    📖 Lesson: How to Define and Call Functions
    """
    print("\n📌 Defining a function is simple! Use `def` followed by the function name.")

    print("\n✅ Example: Defining and calling a function")
    print("""
def say_hello():
    print("Hello, world!")

say_hello()
    """)

    print("\n💡 Challenge: Create a function that prints your name!")


def function_parameters():
    """
    📖 Lesson: Function Parameters
    """
    print("\n📌 Functions can accept inputs (parameters) to customize their behavior.")

    print("\n✅ Example: Function with parameters")
    print("""
def greet(name):
    print("Hello", name, "! Welcome to ujkids!")

greet("Alice")
greet("Bob")
    """)

    print("\n💡 Challenge: Create a function that takes a number and prints its square!")


def return_values():
    """
    📖 Lesson: Returning Values from Functions
    """
    print("\n📌 Functions can return values instead of just printing.")

    print("\n✅ Example: Function that returns a value")
    print("""
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)
    """)

    print("\n💡 Challenge: Write a function that returns the area of a circle (pi * r^2).")


def lambda_functions():
    """
    📖 Lesson: Lambda Functions (Anonymous Functions)
    """
    print("\n📌 Lambda functions are small one-line functions in Python.")

    print("\n✅ Example: Using `lambda` to create a quick function")
    print("""
square = lambda x: x * x
print("Square of 5 is:", square(5))
    """)

    print("\n💡 Challenge: Create a lambda function to check if a number is even or odd!")


def recursion():
    """
    📖 Lesson: Recursion in Python
    """
    print("\n📌 Recursion is when a function calls itself to solve a problem.")
    
    print("\n✅ Example: Factorial using recursion")
    print("""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
    """)

    print("\n💡 Challenge: Create a recursive function to calculate the sum of numbers from 1 to n!")


def mini_exercises():
    """
    📖 Mini Exercises for Functions
    """
    print("\n🎯 Mini Exercises")

    print("\n1️⃣ Create a function that takes two numbers and returns their product.")

    print("\n2️⃣ Write a function that takes a name and prints 'Good morning, [name]!'.")

    print("\n3️⃣ Modify the `factorial` function to check if a number is negative before running.")

    print("\n4️⃣ Create a function that finds the largest number in a list.")

    print("\n💡 Try these in Python and test your skills!")


# Function to run all lessons in sequence
def run_functions():
    """Runs all function-related lessons"""
    introduction()
    defining_functions()
    function_parameters()
    return_values()
    lambda_functions()
    recursion()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_functions()
