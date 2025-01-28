"""
ujkids - Error Handling & Debugging in Python 🛠️
This module explains how to handle errors and debug Python programs with fun examples and exercises.
"""

def introduction():
    """
    📖 Lesson: What are Errors and Exceptions?
    """
    print("\n🚀 Errors are mistakes in a program that stop it from running.")
    print("Exceptions are errors that happen during execution, but we can **handle them** using Python.")
    
    print("\n💡 Example: If you try to divide by zero, Python will raise an exception.")
    print("""
# ❌ This will cause an error:
print(10 / 0)  # ZeroDivisionError
    """)


def try_except():
    """
    📖 Lesson: Try-Except Blocks (Catching Errors)
    """
    print("\n📌 Use `try-except` to catch errors and prevent crashes.")

    print("\n✅ Example: Handling an error")
    print("""
try:
    print(10 / 0)  # This will cause an error
except ZeroDivisionError:
    print("Oops! You can't divide by zero!")
    """)

    print("\n💡 Challenge: Try handling a `ValueError` when converting text to an integer!")


def multiple_exceptions():
    """
    📖 Lesson: Handling Multiple Exceptions
    """
    print("\n📌 Use multiple `except` blocks to catch different types of errors.")

    print("\n✅ Example: Catching multiple errors")
    print("""
try:
    num = int("hello")  # This will cause an error
except ValueError:
    print("Oops! You entered a wrong value.")
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
    """)

    print("\n💡 Challenge: Modify the code to handle both ValueError and TypeError.")


def finally_block():
    """
    📖 Lesson: Using `finally` (Executing Code No Matter What)
    """
    print("\n📌 The `finally` block always runs, even if an error occurs.")

    print("\n✅ Example: Using `finally`")
    print("""
try:
    print(5 / 0)  # This will cause an error
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
finally:
    print("This message always appears.")  # Runs no matter what
    """)

    print("\n💡 Challenge: Add a `finally` block to close a file after reading it.")


def raising_errors():
    """
    📖 Lesson: Raising Custom Errors
    """
    print("\n📌 You can raise errors yourself using `raise`.")

    print("\n✅ Example: Raising an error manually")
    print("""
age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative!")
    """)

    print("\n💡 Challenge: Modify the program to raise an error if age is above 150.")


def debugging_tips():
    """
    📖 Lesson: Debugging Tips & Best Practices
    """
    print("\n🛠️ Debugging is finding and fixing errors in your program.")
    print("Here are some useful tips:")
    print("✅ Read error messages carefully.")
    print("✅ Use `print()` statements to check values.")
    print("✅ Use Python's built-in debugger (`pdb`).")
    print("✅ Keep code simple and well-structured.")

    print("\n💡 Challenge: Find and fix the error in this code:")
    print("""
def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(5))  # ❌ Error: Missing second argument!
    """)


def mini_exercises():
    """
    📖 Mini Exercises for Error Handling
    """
    print("\n🎯 Mini Exercises")

    print("\n1️⃣ Write a Python program that asks for a number and handles `ValueError` if the user enters text.")

    print("\n2️⃣ Modify a division program to catch `ZeroDivisionError` and print a friendly message.")

    print("\n3️⃣ Use `finally` to ensure a message is always printed at the end of your program.")

    print("\n4️⃣ Write a function that raises an error if the input number is negative.")

    print("\n5️⃣ Debug the provided program and fix its syntax errors.")

    print("\n💡 Try these in Python and test your debugging skills!")


# Function to run all lessons in sequence
def run_error_handling():
    """Runs all error handling lessons"""
    introduction()
    try_except()
    multiple_exceptions()
    finally_block()
    raising_errors()
    debugging_tips()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_error_handling()
