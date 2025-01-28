"""
UJKids - Interactive UI 🎨
This module provides a GUI interface for UJKids using Streamlit with an interactive Next/Back navigation system.
"""

import streamlit as st
from ujkids.theory import basics, control_flow, functions, data_structures, oops, file_handling, error_handling, modules, algorithms, projects

# List of lessons in sequential order
LESSONS = [
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

def main():
    """
    🎨 UJKids Main Interface with Interactive Navigation.
    """
    st.set_page_config(page_title="UJKids - Learn Python with Fun!", layout="wide")

    st.title("🧒 UJKids - Learn Python with Fun!")
    st.sidebar.header("📚 Navigation")
    
    # Add some motivation
    st.sidebar.markdown("✨ _Coding is like magic! Keep learning and creating!_ ✨")
    
    # Initialize session state for lesson index
    if "lesson_index" not in st.session_state:
        st.session_state.lesson_index = 0

    # Get current lesson and function
    lesson_title, lesson_function = LESSONS[st.session_state.lesson_index]

    # Display current lesson title with animation
    st.markdown(f"## {lesson_title} 🎓")
    st.markdown("---")

    # Run the current lesson function
    lesson_function()
    
    # Fun progress bar
    progress = (st.session_state.lesson_index + 1) / len(LESSONS)
    st.progress(progress)
    
    # Navigation Buttons with styling
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅ Back", disabled=st.session_state.lesson_index == 0):
            st.session_state.lesson_index -= 1
            st.experimental_rerun()

    with col3:
        if st.button("Next ➡", disabled=st.session_state.lesson_index == len(LESSONS) - 1):
            st.session_state.lesson_index += 1
            st.experimental_rerun()

    # Encouraging Message
    st.markdown("---")
    if st.session_state.lesson_index == len(LESSONS) - 1:
        st.markdown("### 🎉 Congratulations! You've completed all lessons! 🎉")
        st.markdown("_Ready to build your own projects? Keep coding and have fun!_")
    else:
        st.markdown("✨ Keep going! You're doing great! ✨")
    
    # Footer
    st.markdown("---")
    st.markdown("👨‍💻 Developed by UJKids | 🚀 Learning made fun!")

# Run the Streamlit App
if __name__ == "__main__":
    main()