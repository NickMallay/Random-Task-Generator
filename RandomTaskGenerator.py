## A random task generator to refresh my python skills. I am also working on my typing at the moment, so I will be focusing on proper form over speed.
## Prioritize good practises - work iterively, comment often. 

#Feature Specifications
# User added tasks
# Strike completed tasks
# Generate a random Task
# Users can give or change the weight of a task
# Display all tasks

#imports
import random

# The stored list of user tasks. Will be populated by the user on start or during use.
tasks = []
# List of valid core loop options
valid_options = ["HELP", "TASKS", "ADD", "STRIKE", "DRAW", "WEIGHT"]
 


# Function to get a valid input on a question. Valid lists defined above.
def get_valid_input(prompt, valid_options):
        while True:
            user_input = input(prompt)
            if user_input in valid_options:
                return user_input
            else:
                print(f"Invalid choice. Please select one of the following: {', '.join(valid_options)}")
#Help function to display all available options from the main loop
def HELP():
    print("\nHELP - Display this list of options.\nTASKS - Displays a list of all stored tasks.\nADD - Allows you to add another task.\nSTRIKE - Remove a task from the list.\nDRAW - Picks a task at random for you to do, taking into account weight.\nWEIGHT - Allows you to change the weight of a task.\n")
# A function to display all stored tasks, with a label. Indexed, to allow targeted removal
def print_task(task_list):
    if task_list:
        print("Your tasks are as follows: ")
        for index, task in enumerate(task_list, 1):
            print(f"{index}. {task['task']}")
    else:
        print("There are no tasks stored.")
#Add function to add new tasks to the list
def add_task():
    while True:
        task_description = input("Enter a task you need done. When you don't have any more tasks to add, type DONE\n")
        if task_description == "DONE":
            print("Tasks Added")
            print("-----------")
            input("Press enter to continue")
            break 
        else:
            while True:
                try:
                    task_weight = int(input("How important is this task? (1 = Not super important. 5 = Life or death.)\n"))
                    if task_weight < 1 or task_weight > 5:
                        print("Please enter a number between 1 and 5.")
                    else:
                        break
                except ValueError:
                    print("Please enter a number between 1 and 5")
            tasks.append({"task": task_description, "weight": task_weight})
            print(f"'{task_description}' has been added with a weight of {task_weight}")
#Strike function to remove a task from the list
def STRIKE():
    if not tasks:
        print("No tasks to remove.")
        return
    
    print_task(tasks)
    while True:
        try:
            task_index = int(input("\nEnter the number of the task you would like to remove.\n"))
            if task_index >= 1 and task_index <= len(tasks):
                removed_task = tasks.pop(task_index - 1) # -1 to account for default 0 coungting
                print(f"The task '{removed_task['task']}' has been removed.")
                break
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




# Have the user add one or multiple tasks, typing DONE when they are finished.
print("Welcome to Random Task Generator, a task managment and productivity assistant.")
add_task()  

#Core loop. Users can access available functions from here, such as pulling a task, adding a task, checking a help list, etc.
while True:
    user_action = get_valid_input("What would you like to do? (Type HELP for a list of options)\n", valid_options)
    if user_action == "HELP":
        HELP()
    elif user_action == "TASKS":
        print_task(tasks)
    elif user_action == "ADD":
        add_task()     
    elif user_action == "STRIKE":
        STRIKE() 
    elif user_action == "DRAW":
        DRAW()  
    elif user_action == "WEIGHT":
        WEIGHT()      

