## A random task generator to refresh my python skills. I am also working on my typing at the moment, so I will be focusing on proper form over speed.
## Prioritize good practises - work iterively, comment often. 

#Feature Specifications
# User added tasks
# Strike completed tasks
# Generate a random Task
# Users can give or change the weight of a task
# Display all tasks


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
    print("HELP - Display this list of options.\nTASKS - Displays a list of all stored tasks.\nADD - Allows you to add another task.\nSTRIKE - Remove a task from the list.\nDRAW - Picks a task at random for you to do, taking into account weight.\nWEIGHT - Allows you to change the weight of a task.")
# A function to display all stored tasks, with a label.
def print_task(task_list):
    print("Your tasks are as follows: ")
    for index, task in enumerate(task_list, 1):
        print(f"{index}. {task}")
#Add function to add new tasks to the list
def add_task():
    while True:
        user_input = input("What task would you like to add? Enter as many as you would like one at a time, then type DONE")
        if user_input == "DONE":
            print("Tasks Added")
            print("-----------")
            input("Press enter to continue")
            break 
        else:
            tasks.append(user_input)
#Strike function to remove a task from the list

#Draw function to pull a random card from a weight adjusted list for the user to do
#Weight function to change the weight of a task

# The stored list of user tasks. Will be populated by the user on start or during use.
tasks = []
# List of valid core loop options
valid_options = ["HELP", "TASKS", "ADD", "STRIKE", "DRAW", "WEIGHT"]
# Have the user add one or multiple tasks, typing DONE when they are finished. 

print("Welcome to Random Task Generator, a task managment and productivity assistant.")
print("To begin, enter a task that needs to be done.")
print("Enter as many as you would like, one at a time. When you are finished, type 'DONE'")
while True:
    user_input = input()
    if user_input == "DONE":
        print("Tasks Added")
        print("-----------")
        input("Press enter to continue")
        break 
    else:
        tasks.append(user_input)

#Core loop. Users can access available functions from here, such as pulling a task, adding a task, checking a help list, etc.
while True:
    user_action = get_valid_input("What would you like to do? (Type HELP for a list of options)", valid_options)
    if user_action == "HELP":
        HELP()
    elif user_action == "TASKS":
        print_task(tasks)
    elif user_action == "ADD":
        add_task()     
    elif user_action == "STRIKE":
        print("WIP")  
    elif user_action == "DRAW":
        print("WIP")  
    elif user_action == "WEIGHT":
        print("WIP")      

