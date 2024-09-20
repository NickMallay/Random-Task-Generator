## A random task generator to refresh my python skills. I am also working on my typing at the moment, so I will be focusing on proper form over speed.
## Prioritize good practises - work iterively, comment often. 

#Feature Specifications
# User added tasks
# Strike completed tasks
# Generate a random Task
# Users can give or change the weight of a task
# Display all tasks


def print_task(task_list):
    print("Your tasks are as follows: ")
    for task in task_list:
        print(task)
tasks = []

print("Welcome to Random Task Generator, a task managment and productivity assistant.")
print("To begin, enter a task that needs to be done.")
print("When you are finished type 'DONE'")

while True:
    user_input = input()
    if user_input == "DONE":
        break 
    else:
        tasks.append(user_input)

    
print_task(tasks)
