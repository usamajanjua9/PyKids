"""
ujkids - Control Flow in Python 🧭
This module explains decision-making (if-else) and loops (for, while) with examples and exercises.
"""

def introduction():
    """
    📖 Lesson: Introduction to Control Flow
    """
    print("\n🚀 Control flow helps Python make decisions and repeat actions.")
    print("There are two main types of control flow:")
    print("1️⃣ Conditional Statements (if-else) → Making decisions.")
    print("2️⃣ Loops (for, while) → Repeating actions.")


def if_else_statements():
    """
    📖 Lesson: Conditional Statements (if-else)
    """
    print("\n📌 Conditional Statements: if, elif, else")
    print("Python checks conditions and runs different code based on the result.")

    # Example:
    print("\n✅ Example:")
    print("""
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote! 🗳️")
elif age > 12:
    print("You are a teenager! 🤓")
else:
    print("You are still a child! 🎈")
    """)

    print("\n💡 Try changing the value of `age` to see different results!")


def loops_for():
    """
    📖 Lesson: For Loop
    """
    print("\n📌 Loops help repeat actions multiple times.")

    print("\n✅ Example: Counting 1 to 5 using a `for` loop")
    print("""
for i in range(1, 6):
    print(i)
    """)

    print("\n✅ Example: Looping through a list")
    print("""
fruits = ["🍎 Apple", "🍌 Banana", "🍇 Grapes"]

for fruit in fruits:
    print(fruit)
    """)

    print("\n💡 Challenge: Print all numbers from 1 to 20 using a for loop!")


def loops_while():
    """
    📖 Lesson: While Loop
    """
    print("\n📌 While loops keep running as long as a condition is True.")

    print("\n✅ Example: Printing numbers from 1 to 5 using a while loop")
    print("""
count = 1

while count <= 5:
    print(count)
    count += 1
    """)

    print("\n💡 Challenge: Create a while loop that prints even numbers from 2 to 10!")


def nested_loops():
    """
    📖 Lesson: Nested Loops and If-Else Statements
    """
    print("\n📌 You can put loops inside loops and use if-else inside loops.")

    print("\n✅ Example: Nested loop printing a triangle pattern")
    print("""
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
    """)

    print("\n💡 Challenge: Modify the above program to print a pyramid!")


def break_continue_pass():
    """
    📖 Lesson: Break, Continue, and Pass
    """
    print("\n📌 Special loop controls:")

    print("\n✅ Example: `break` - Stop a loop early")
    print("""
for i in range(1, 10):
    if i == 5:
        break  # Stops the loop when i is 5
    print(i)
    """)

    print("\n✅ Example: `continue` - Skip an iteration")
    print("""
for i in range(1, 10):
    if i == 5:
        continue  # Skips printing 5
    print(i)
    """)

    print("\n✅ Example: `pass` - Placeholder (Does nothing)")
    print("""
for i in range(1, 5):
    if i == 3:
        pass  # This does nothing but keeps the loop structure
    print(i)
    """)

    print("\n💡 Challenge: Write a loop that stops when it finds the number 7!")


def mini_exercises():
    """
    📖 Mini Exercises for Control Flow
    """
    print("\n🎯 Mini Exercises")

    print("\n1️⃣ Write a Python program that asks for a number and prints if it's odd or even.")

    print("\n2️⃣ Use a `for` loop to print all multiples of 3 between 1 and 30.")

    print("\n3️⃣ Use a `while` loop to ask the user for a password until they enter 'PythonRocks'.")

    print("\n4️⃣ Write a program that finds the first number divisible by 7 and 5 between 1 and 100.")

    print("\n💡 Try writing these in Python and test your logic!")


# Function to run all lessons in sequence
def run_control_flow():
    """Runs all control flow lessons"""
    introduction()
    if_else_statements()
    loops_for()
    loops_while()
    nested_loops()
    break_continue_pass()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_control_flow()
