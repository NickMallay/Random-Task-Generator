## A random task generator to refresh my python skills. I am also working on my typing at the moment, so I will be focusing on proper form over speed.
## Prioritize good practises - work iterively, comment often. 

#Feature Specifications
# User added tasks
# Strike completed tasks
# Generate a random Task
# Users can give or change the weight of a task
# Display all tasks
##########
#imports
##########

import random #for randomchoice when drawing a tast
import json #To make save files
import os
import tkinter as tk
# Change the working directory to the directory of this file so that it will save the json files there. 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

##########
# Lists
##########

# The stored list of user tasks. Will be populated by the user on start or during use.
tasks = []
# List of valid core loop options
valid_options = ["HELP", "TASKS", "ADD", "STRIKE", "DRAW", "WEIGHT", "SAVE", "LOAD"]
 



############
# Functions
############


#Add function to add new tasks to the list
def add_task():
        task_description = task_input.get().strip()
        task_weight = int(weight_input.get().strip())
        if task_description and task_weight: # if task_description is empty, this if statment will not be true, so it will go to the else statment
            tasks.append({"task": task_description, "weight": task_weight})
            feed_back_label.config(text=f"Task added! {task_description} with a weight of {task_weight}!")

        else:
            feed_back_label.config(text="Please enter valid text.", fg="red")

#Strike function to remove a task from the list
def STRIKE():
    if not tasks:
        print("No tasks to remove.")
        return
    
    while True:
        try:
            print_task(tasks)
            task_index = int(input("\nEnter the number of the task you would like to remove.\n"))
            if task_index >= 1 and task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1) # -1 to account for default 0 coungting
                print(f"The task '{removed_task['task']}' has been removed.")
                while True:
                    strike_again = input("Would you like to stike another? (YES / NO)")
                    if strike_again == "NO":
                        return
                    elif strike_again == "YES":
                        if not tasks:
                            print("No tasks to remove.")
                            return
                        break
                    else:
                        print("Please enter YES or NO")

                    
                
        except ValueError:
            print("Please enter a valid number.")
#Draw function to pull a random card from a weight adjusted list for the user to do
def DRAW():
    if not tasks:
        print("There are not tasks to draw from.")
        return

    weighted_list = []
    for task in tasks:
        weighted_list.extend([task['task']] * task['weight'])

    selected_task = random.choice(weighted_list)
    print(f"Your random task is: {selected_task}")
#Weight function to change the weight of a task
def WEIGHT():
    if not tasks:
        print("No tasks to change.")
        return
    
    print_task(tasks)
    print("Enter the number of the task you would like to edit")
    while True:
        try:
            weight_change_index = int(input())
            if weight_change_index >= 1 and weight_change_index <= len(tasks):
                while True:
                    try:
                        new_weight = int(input("What would you like to change the weight to? (Please enter a number between 1 and 5)"))
                        if new_weight >= 1 and new_weight <= 5:
                            tasks[weight_change_index - 1]["weight"] = new_weight
                            print(f"The task '{tasks[weight_change_index - 1]['task']} has been updated to a weight of {tasks[weight_change_index - 1]['weight']}")
                            return
                        else:
                            print("Please enter a valid number between 1 and 5")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter valid number.")
#SAVE function using JSON
def save_to_file(task_list, filename="tasks.json"):
    try:
        with open(filename, "w") as file:
            json.dump(task_list, file)
        print("You have saved successfully.")
    except Exception as e:
        print(f"An error has occured while saving '{e}'")
#LOAD function using JSON
def load_file(filename='tasks.json'):
    try:
        with open(filename, "r") as file:
            task_list = json.load(file)
            print(f"{filename} has been loaded.")
            return task_list
    except FileNotFoundError:
            print("No save file found.")
            return
    except Exception as exception:
        print(f"An error occurred while loading: {exception}")
        return


############
# UI 
############


# UI initialization
root = tk.Tk()
root.title("Random Task Generator") # Window title
root.geometry("600x400") # Window size
# Welcome label
welcome_label = tk.Label(root, text="Welcome to the Random Task Generator!", font=("Helvetica", 16))
welcome_label.pack(pady = 20)
# Feedback label to communicate to user
feed_back_label = tk.Label(root, text = "Stuff will appear here", font=("Helvetica", 12), fg="blue")
feed_back_label.pack(pady=10)
#Task Entry Label
task_label = tk.Label(root, text="Please enter a task that needs doing.")
task_label.pack(pady=0)
#Box to enter the task
task_input = tk.Entry(root, width=40)
task_input.pack(pady=0)
#Weight input label
weight_label = tk.Label(root, text="Please enter a number between 1 and 5")
weight_label.pack(pady=0)
#Weight input button
weight_input = tk.Entry(root, width=10)
weight_input.pack(pady=0)
#Button to add the task
add_button = tk.Button(root, text="Confirm to add task.", command=add_task)
add_button.pack(pady=10)
# Start the main TK loop
root.mainloop()






# #Core loop. Users can access available functions from here, such as pulling a task, adding a task, checking a help list, etc.
# while True:
#     user_action = get_valid_input("What would you like to do? (Type HELP for a list of options)\n", valid_options)
#     if user_action == "HELP":
#         HELP()
#     elif user_action == "TASKS":
#         print_task(tasks)
#     elif user_action == "ADD":
#         add_task()     
#     elif user_action == "STRIKE":
#         STRIKE() 
#     elif user_action == "DRAW":
#         DRAW()  
#     elif user_action == "WEIGHT":
#         WEIGHT()      
#     elif user_action == "SAVE":
#         save_to_file(tasks)
#     elif user_action == "LOAD":
#         tasks = load_file()
        
