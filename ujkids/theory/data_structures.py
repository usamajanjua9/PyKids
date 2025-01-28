"""
ujkids - Data Structures in Python 📦
This module explains lists, tuples, dictionaries, and sets with fun examples and exercises.
"""

def introduction():
    """
    📖 Lesson: What are Data Structures?
    """
    print("\n🚀 Data structures help store and organize data efficiently.")
    print("Python has four main built-in data structures:")
    print("1️⃣ Lists → Ordered, changeable collections.")
    print("2️⃣ Tuples → Ordered, but unchangeable collections.")
    print("3️⃣ Dictionaries → Key-value pairs.")
    print("4️⃣ Sets → Unordered collections with unique elements.")


def lists():
    """
    📖 Lesson: Lists in Python
    """
    print("\n📌 Lists store multiple values in one variable.")

    print("\n✅ Example: Creating and accessing lists")
    print("""
fruits = ["🍎 Apple", "🍌 Banana", "🍇 Grapes"]
print("First fruit:", fruits[0])  # Apple
print("All fruits:", fruits)
    """)

    print("\n✅ Example: Adding and removing elements")
    print("""
fruits.append("🍉 Watermelon")  # Adds an item
fruits.remove("🍌 Banana")  # Removes an item
print("Updated list:", fruits)
    """)

    print("\n💡 Challenge: Create a list of your favorite animals and print the second one!")


def tuples():
    """
    📖 Lesson: Tuples in Python
    """
    print("\n📌 Tuples are similar to lists but **cannot be changed** after creation.")

    print("\n✅ Example: Creating a tuple")
    print("""
colors = ("🔴 Red", "🟢 Green", "🔵 Blue")
print("Favorite color:", colors[1])  # Green
    """)

    print("\n❌ Trying to change a tuple (This will cause an error!)")
    print("""
colors[0] = "🟠 Orange"  # ❌ ERROR: Tuples are immutable!
    """)

    print("\n💡 Challenge: Create a tuple of 3 numbers and print their sum!")


def dictionaries():
    """
    📖 Lesson: Dictionaries in Python
    """
    print("\n📌 Dictionaries store data in **key-value pairs**.")

    print("\n✅ Example: Creating a dictionary")
    print("""
student = {
    "name": "Alice",
    "age": 10,
    "grade": "5th"
}

print("Student Name:", student["name"])
print("Student Age:", student["age"])
    """)

    print("\n✅ Example: Adding and updating values")
    print("""
student["hobby"] = "Painting"  # Adding new key-value pair
student["age"] = 11  # Updating an existing key
print("Updated Student:", student)
    """)

    print("\n💡 Challenge: Create a dictionary for your favorite movie with title, year, and genre!")


def sets():
    """
    📖 Lesson: Sets in Python
    """
    print("\n📌 Sets store unique values and are unordered.")

    print("\n✅ Example: Creating a set")
    print("""
numbers = {1, 2, 3, 4, 5, 5, 5}  # Duplicates are removed automatically
print("Unique numbers:", numbers)
    """)

    print("\n✅ Example: Adding and removing elements")
    print("""
numbers.add(10)  # Adding an element
numbers.remove(3)  # Removing an element
print("Updated set:", numbers)
    """)

    print("\n💡 Challenge: Create a set of five colors and check if 'Red' is in it!")


def iterating_data_structures():
    """
    📖 Lesson: Looping through Data Structures
    """
    print("\n📌 You can loop through lists, tuples, dictionaries, and sets.")

    print("\n✅ Example: Looping through a list")
    print("""
fruits = ["🍎 Apple", "🍌 Banana", "🍇 Grapes"]

for fruit in fruits:
    print("I like", fruit)
    """)

    print("\n✅ Example: Looping through a dictionary")
    print("""
student = {"name": "Alice", "age": 10, "grade": "5th"}

for key, value in student.items():
    print(key, ":", value)
    """)

    print("\n💡 Challenge: Loop through a set of numbers and print their squares!")


def mini_exercises():
    """
    📖 Mini Exercises for Data Structures
    """
    print("\n🎯 Mini Exercises")

    print("\n1️⃣ Create a list of 5 cities and print the last city.")

    print("\n2️⃣ Convert a list to a tuple and try modifying it (expect an error).")

    print("\n3️⃣ Create a dictionary for your best friend's details (name, age, hobby).")

    print("\n4️⃣ Find the intersection (common values) of two sets.")

    print("\n💡 Try these in Python and test your understanding!")


# Function to run all lessons in sequence
def run_data_structures():
    """Runs all data structure lessons"""
    introduction()
    lists()
    tuples()
    dictionaries()
    sets()
    iterating_data_structures()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_data_structures()
