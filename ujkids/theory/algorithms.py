"""
ujkids - Algorithms in Python 🚀
This module explains sorting, searching, and recursion with simple examples and exercises.
"""

def introduction():
    """
    📖 Lesson: What are Algorithms?
    """
    print("\n🚀 An **algorithm** is a step-by-step method to solve a problem.")
    print("Think of it like a **recipe** 🍳 for solving coding problems efficiently.")

    print("\n💡 Example: A simple algorithm to find the largest number in a list.")
    print("""
numbers = [5, 8, 2, 10, 3]
largest = max(numbers)
print("Largest number is:", largest)
    """)

    print("\n✅ Let's explore sorting, searching, and recursion!")


def bubble_sort():
    """
    📖 Lesson: Bubble Sort Algorithm
    """
    print("\n📌 Bubble Sort repeatedly swaps adjacent elements to sort a list.")

    print("\n✅ Example: Bubble Sort Implementation")
    print("""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

arr = [5, 2, 9, 1, 5, 6]
bubble_sort(arr)
print("Sorted array:", arr)
    """)

    print("\n💡 Challenge: Modify the function to sort in **descending order**.")


def selection_sort():
    """
    📖 Lesson: Selection Sort Algorithm
    """
    print("\n📌 Selection Sort finds the smallest element and moves it to the correct position.")

    print("\n✅ Example: Selection Sort Implementation")
    print("""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Find the smallest value
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
    """)

    print("\n💡 Challenge: Modify the function to find the **largest element first** instead.")


def linear_search():
    """
    📖 Lesson: Linear Search Algorithm
    """
    print("\n📌 Linear Search checks each element one by one.")

    print("\n✅ Example: Linear Search Implementation")
    print("""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found the target
    return -1  # Not found

arr = [10, 20, 30, 40, 50]
index = linear_search(arr, 30)
print("Found at index:", index)
    """)

    print("\n💡 Challenge: Modify the function to return a **list of all occurrences** of the target.")


def binary_search():
    """
    📖 Lesson: Binary Search Algorithm
    """
    print("\n📌 Binary Search is faster than Linear Search but needs a sorted list.")

    print("\n✅ Example: Binary Search Implementation")
    print("""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found

arr = [10, 20, 30, 40, 50]
index = binary_search(arr, 30)
print("Found at index:", index)
    """)

    print("\n💡 Challenge: Modify the function to search for the **smallest number greater than the target**.")


def recursion_factorial():
    """
    📖 Lesson: Recursion (Factorial Example)
    """
    print("\n📌 Recursion is when a function **calls itself**.")

    print("\n✅ Example: Factorial using Recursion")
    print("""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
    """)

    print("\n💡 Challenge: Modify the function to handle **negative numbers**.")


def recursion_fibonacci():
    """
    📖 Lesson: Fibonacci Sequence Using Recursion
    """
    print("\n📌 The Fibonacci sequence is **1, 1, 2, 3, 5, 8, ...**")

    print("\n✅ Example: Fibonacci using Recursion")
    print("""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci number at position 6:", fibonacci(6))
    """)

    print("\n💡 Challenge: Modify the function to use a **loop instead of recursion**.")


def big_o_notation():
    """
    📖 Lesson: Understanding Algorithm Efficiency (Big-O)
    """
    print("\n📌 Big-O notation helps us understand how **fast or slow** an algorithm is.")

    print("\n✅ Example: Comparing Algorithm Speeds")
    print("""
O(1)  - Constant Time  ->  Looking up an item in a dictionary.
O(log n) - Logarithmic Time  ->  Binary search in a sorted list.
O(n)  - Linear Time  ->  Checking each item in a list (linear search).
O(n^2) - Quadratic Time  ->  Nested loops (bubble sort).
O(2^n) - Exponential Time  ->  Fibonacci using recursion.
    """)

    print("\n💡 Challenge: Find out the **Big-O complexity** of selection sort!")


def mini_exercises():
    """
    📖 Mini Exercises for Algorithms
    """
    print("\n🎯 Mini Exercises")

    print("\n1️⃣ Implement **bubble sort** and test it with a list of numbers.")

    print("\n2️⃣ Implement **binary search** and test it with a sorted list.")

    print("\n3️⃣ Modify the **factorial function** to work with numbers up to 100.")

    print("\n4️⃣ Implement an algorithm to find the **largest number in a list**.")

    print("\n5️⃣ Compare **linear search vs binary search** on a large dataset.")

    print("\n💡 Try these in Python and improve your algorithm skills!")


# Function to run all lessons in sequence
def run_algorithms():
    """Runs all algorithm-related lessons"""
    introduction()
    bubble_sort()
    selection_sort()
    linear_search()
    binary_search()
    recursion_factorial()
    recursion_fibonacci()
    big_o_notation()
    mini_exercises()


# Run lessons when the file is executed
if __name__ == "__main__":
    run_algorithms()
