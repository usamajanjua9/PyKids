"""
Setup script for ujkids 📦
This file allows ujkids to be installed and used as a package.
"""

from setuptools import setup, find_packages

setup(
    name="ujkids",
    version="1.0.2",  # ✅ Updated version number
    author="Dr. Usama Arshad",
    author_email="usamajanjua9@gmail.com",
    description="An interactive Python learning library for kids with animations, games, and exercises.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/usamajanjua9/ujkids/tree/main",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
        "matplotlib",
        "pygame",
        "pandas"
    ],  
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "ujkids=ujkids.ui:main",
        ]
    },
    python_requires=">=3.6",
)
