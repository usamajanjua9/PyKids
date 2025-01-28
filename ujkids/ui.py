"""
UJKids - Interactive UI 🎨
This module provides a GUI interface for UJKids using IPython Widgets (ipywidgets) with an interactive Next/Back navigation system.
"""

import ipywidgets as widgets
from IPython.display import display, clear_output
from ujkids.theory import basics, control_flow, functions, data_structures, oops, file_handling, error_handling, modules, algorithms, projects

# List of lessons in sequential order
LESSONS = [
    ("🏠 Home", None),
    ("📖 Basics of Python", basics.run_basics),
    ("🔁 Control Flow (If-Else, Loops)", control_flow.run_control_flow),
    ("🛠️ Functions", functions.run_functions),
    ("📦 Data Structures (Lists, Dicts, Sets)", data_structures.run_data_structures),
    ("🏗️ Object-Oriented Programming", oops.run_oops),
    ("📂 File Handling", file_handling.run_file_handling),
    ("🚀 Error Handling & Debugging", error_handling.run_error_handling),
    ("📦 Modules & Packages", modules.run_modules),
    ("📊 Algorithms & Recursion", algorithms.run_algorithms),
    ("🎮 Mini Projects", projects.run_projects),
]

# Initialize lesson index
total_lessons = len(LESSONS)
lesson_index = 0

# Output widget to update lesson content
output = widgets.Output()

def update_ui():
    """ Update the UI based on the current lesson index. """
    with output:
        clear_output(wait=True)
        lesson_title, lesson_function = LESSONS[lesson_index]

        if lesson_function is None:
            print("\n### Welcome to UJKids! 🚀\n")
            print("An interactive way for kids to learn Python with fun animations and projects!")
        else:
            print(f"\n### {lesson_title} 🎓\n")
            lesson_function()

# Navigation buttons
def next_lesson(_):
    global lesson_index
    if lesson_index < total_lessons - 1:
        lesson_index += 1
        update_ui()

def previous_lesson(_):
    global lesson_index
    if lesson_index > 0:
        lesson_index -= 1
        update_ui()

# Create Next/Back buttons
back_button = widgets.Button(description="⬅ Back")
next_button = widgets.Button(description="Next ➡")
back_button.on_click(previous_lesson)
next_button.on_click(next_lesson)

# Display UI
def main():
    display(widgets.HBox([back_button, next_button]))
    display(output)
    update_ui()

# Run the UI in Jupyter Notebook
main()
