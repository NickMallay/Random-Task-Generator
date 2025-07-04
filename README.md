# Random-Task-Generator

Random Task Generator

A simple desktop application to store, prioritize, and randomly draw tasks using weighted probabilities. Designed to help reduce decision fatigue and maintain momentum when faced with multiple responsibilities.

This project was built in Python using Tkinter, and is part of the Backend Blitz initiative.

Features

Add and remove tasks through a user-friendly interface

Assign weight (1–5) to each task to influence its chance of being drawn

Draw a task at random, with weight influencing likelihood

Save and load task lists to and from JSON files

Built-in help window with usage instructions

Scrollable list of current tasks with numbering

Getting Started

Requirements

Python 3.x

Tkinter (included with most Python distributions)

Running the App

From the command line:

python task_generator.py

The working directory is automatically set to the script’s location, so save and load features work without any additional setup.

How It Works

Add Mode: Enter a task and assign it a weight between 1 and 5. Higher weights increase the task’s chances of being drawn.

Remove Mode: Enter the task number (as listed) to remove it from the list.

Draw Task: Selects a task randomly, taking weight into account.

Save/Load: Use the top-left buttons to save your current task list or load a previously saved one.

File Structure

task_generator.py      # Main application script
task_list.json         # Auto-generated file to store your task list

Author

Nick Mallay Contact: nickmallay@hotmail.com
