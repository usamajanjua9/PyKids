"""
ujkids - Mini Python Projects 🎯
This module contains small Python projects to help kids practice coding.
"""

import random

def introduction():
    """
    📖 Lesson: What Are Mini Projects?
    """
    print("\n🚀 Mini projects are small programs that solve simple problems.")
    print("They help you practice **logic, loops, functions, and conditionals.**")
    
    print("\n💡 Let's build fun projects together!")


def number_guessing_game():
    """
    🎮 Project 1: Number Guessing Game
    """
    print("\n🎲 Welcome to the Number Guessing Game!")

    print("\n✅ Example: Code for Number Guessing Game")
    print("""
import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess < secret_number:
        print("Try a higher number!")
    else:
        print("Try a lower number!")
    """)

    print("\n💡 Challenge: Modify the game to count the number of attempts!")


def simple_calculator():
    """
    🎮 Project 2: Simple Calculator
    """
    print("\n🧮 Let's create a simple calculator.")

    print("\n✅ Example: Code for a Calculator")
    print("""
def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", num1 + num2)
        elif operator == "-":
            print("Result:", num1 - num2)
        elif operator == "*":
            print("Result:", num1 * num2)
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator!")

calculator()
    """)

    print("\n💡 Challenge: Modify the calculator to support exponentiation (`**`).")


def todo_list():
    """
    🎮 Project 3: To-Do List Manager
    """
    print("\n📋 Let's create a simple to-do list manager.")

    print("\n✅ Example: Code for a To-Do List")
    print("""
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks added yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    task_num = int(input("Enter task number to remove: "))
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number!")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
    """)

    print("\n💡 Challenge: Add an option to mark tasks as completed.")


def rock_paper_scissors():
    """
    🎮 Project 4: Rock, Paper, Scissors Game
    """
    print("\n✊✋✌️ Let's play Rock, Paper, Scissors!")

    print("\n✅ Example: Code for Rock, Paper, Scissors")
    print("""
import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win!")
    else:
        print("😢 You lose!")

    if input("Play again? (yes/no): ").lower() != "yes":
        break
    """)

    print("\n💡 Challenge: Add a score counter to track wins and losses!")


def password_generator():
    """
    🎮 Project 5: Password Generator
    """
    print("\n🔑 Let's create a random password generator.")

    print("\n✅ Example: Code for Password Generator")
    print("""
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print("Generated password:", generate_password(12))
    """)

    print("\n💡 Challenge: Modify the function to generate a password without special characters.")


def quiz_game():
    """
    🎮 Project 6: Quiz Game
    """
    print("\n🧠 Let's create a fun quiz game!")

    print("\n✅ Example: Code for a Quiz Game")
    print("""
questions = {
    "What is the capital of France?": "paris",
    "What is 2 + 2?": "4",
    "What is the color of the sky?": "blue"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ").lower()
    if user_answer == answer:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌ The correct answer is", answer)

print("Final Score:", score, "out of", len(questions))
    """)

    print("\n💡 Challenge: Add more questions and track high scores!")


def tic_tac_toe():
    """
    🎮 Bonus Project: Tic-Tac-Toe
    """
    print("\n🎲 Tic-Tac-Toe (Bonus Challenge)")

    print("\n💡 Challenge: Implement a **Tic-Tac-Toe** game using a 3x3 grid!")


def final_challenge():
    """
    🚀 Final Challenge: Create Your Own Project!
    """
    print("\n🎯 Your Final Challenge: Build your own Python project!")
    print("Choose any topic and try to create something **fun and useful.**")

    print("\n💡 Some ideas:")
    print("✅ A simple **weather app** using an API.")
    print("✅ A **story generator** that writes random stories.")
    print("✅ A **calculator** that solves math problems step by step.")

    print("\n🔥 Ready? Start coding and create something amazing!")


# Function to run all projects
def run_projects():
    """Runs all mini projects"""
    introduction()
    number_guessing_game()
    simple_calculator()
    todo_list()
    rock_paper_scissors()
    password_generator()
    quiz_game()
    tic_tac_toe()
    final_challenge()


# Run projects when the file is executed
if __name__ == "__main__":
    run_projects()
