"""
ujkids - File Handling in Python 📂
This module explains how to read, write, and manipulate files in Python with examples and exercises.
"""

def introduction():
    """
    📖 Lesson: What is File Handling?
    """
    print("\n🚀 File handling allows us to store and retrieve data from files.")
    print("Python makes it easy to work with **text files, CSV files, and JSON files.**")
    
    print("\n💡 Example: Imagine a diary 📖 where you can write and read entries. That's like working with files!")


def reading_files():
    """
    📖 Lesson: Reading Files in Python
    """
    print("\n📌 To read a file, use the `open()` function in **read mode ('r')**.")

    print("\n✅ Example: Reading a file")
    print("""
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Prints file content
    """)

    print("\n💡 Challenge: Create a text file named `my_notes.txt` and try reading it in Python!")


def writing_files():
    """
    📖 Lesson: Writing to Files
    """
    print("\n📌 To write to a file, use `write mode ('w')`. It replaces the existing content.")

    print("\n✅ Example: Writing to a file")
    print("""
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file!")  # Writing data
    """)

    print("\n💡 Challenge: Write your favorite quote into a file called `quotes.txt`.")


def appending_files():
    """
    📖 Lesson: Appending to Files
    """
    print("\n📌 Use `append mode ('a')` to add new content without deleting old data.")

    print("\n✅ Example: Appending data to a file")
    print("""
with open("example.txt", "a") as file:
    file.write("\\nThis is a new line added!")  # Appends data
    """)

    print("\n💡 Challenge: Append three of your favorite foods to `foods.txt`.")


def reading_csv():
    """
    📖 Lesson: Working with CSV Files
    """
    print("\n📌 CSV files store data in a **comma-separated** format (like a table).")

    print("\n✅ Example: Reading a CSV file")
    print("""
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Prints each row of the CSV file
    """)

    print("\n💡 Challenge: Create a CSV file named `students.csv` with names and ages, then read it in Python!")


def writing_csv():
    """
    📖 Lesson: Writing to a CSV File
    """
    print("\n📌 You can store tabular data in CSV files and edit them with Excel.")

    print("\n✅ Example: Writing data to a CSV file")
    print("""
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 12])
    writer.writerow(["Bob", 10])
    """)

    print("\n💡 Challenge: Add more student records to `students.csv`.")


def working_with_json():
    """
    📖 Lesson: Working with JSON Files
    """
    print("\n📌 JSON files store data in a structured format, like Python dictionaries.")

    print("\n✅ Example: Writing data to a JSON file")
    print("""
import json

data = {"name": "Alice", "age": 10, "hobby": "Painting"}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)  # Saves data as JSON
    """)

    print("\n💡 Challenge: Create a dictionary for your favorite book and save it as `book.json`.")


def mini_exercises():
    """
    📖 Mini Exercises for File Handling
    """
    print("\n🎯 Mini Exercises")

    print("\n1️⃣ Create a text file named `story.txt` and write a short story into it.")

    print("\n2️⃣ Write a Python program to read and print the content of `story.txt`.")

    print("\n3️⃣ Modify the `story.txt` file by appending a new paragraph at the end.")

    print("\n4️⃣ Create a CSV file named `friends.csv` with names and favorite colors.")

    print("\n5️⃣ Write a Python program that reads and prints the content of `friends.csv`.")

    print("\n6️⃣ Create a JSON file with your personal details and load it in Python.")

    print("\n💡 Try these in Python and practice your file-handling skills!")


# Function to run all lessons in sequence
def run_file_handling():
    """Runs all file handling lessons"""
    introduction()
    reading_files()
    writing_files()
    appending_files()
    reading_csv()
    writing_csv()
    working_with_json()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_file_handling()
