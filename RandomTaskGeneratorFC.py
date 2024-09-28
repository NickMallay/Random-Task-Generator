import tkinter as tk # To build a UI
import os # To set save directory
import random # To draw random task
import json # To make and load save files

# Change the working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

###########
#Functions
###########

# Save and load functions for button tests
def save(task_list, filename="task_list.json"):
    try:
        with open(filename, "w") as file:
            json.dump(task_list, file)
        feedback_label.config(text="Task list saved.")
    except Exception as e:
        feedback_label.config(text=f"An error has occured: '{e}'")
def load(filename="task_list.json"):
    global task_list
    try:
        with open(filename, "r") as file:
            task_list = json.load(file)
        feedback_label.config(text="Task list loaded")
        print_task(task_list)
    except FileNotFoundError:
        feedback_label.config(text="No save file found.")
        return
    except Exception as exception:
       feedback_label.config(text=f"An error occurred while loading: {exception}")
       return

# Function to swap between add/remove functionality
def add_remove_toggled():
    if add_remove_current.get():
        task_entry_label.config(text="Please enter a task that needs to be done.")
        weight_entry.grid(row=7, column=3)
        weight_entry_label.grid(row=6,column=3)
        confirm_button.config(text="Click to add task")
    else:
        task_entry_label.config(text="Please enter the number of the task to be deleted.")
        weight_entry.grid_remove()
        weight_entry_label.grid_remove()
        confirm_button.config(text="Click to remove task.")

# Function to open a help window
def open_help():
    # Create a new window
    help_window = tk.Toplevel(root)
    help_window.title("Random Task Generator - Help")
    help_window.geometry("400x350")
    # Add helpful info about how to use the program
    help_label = tk.Label(help_window, text="Click a button below to get info on that topic:")
    help_label.pack(pady=5)
    # A non-editable text box that will display help data
    help_text = tk.Text(help_window, state="disabled", width= 40, height= 13, wrap=tk.WORD, font=("Helvetica", "9"))
    help_text.pack()
    # Add a frame to hold the help buttons horizontally, used to avoid converting the entire help window to .grid
    frame_help_button = tk.Frame(help_window)
    frame_help_button.pack(pady=10)
    # Add a button to display "About" information
    about_help_button = tk.Button(frame_help_button, 
                             text="About",                              
                             command=lambda: 
                             (help_text.config(state="normal"), 
                              help_text.delete("1.0", tk.END), 
                              help_text.insert("1.0", 
                                               "Random Task Generator is a project under the Backend Blitz inititive.\n\n"                                
                                                "It can be used to store tasks that need doing and to randomly draw one of those tasks, so you do not have to choose.\n"
                                                "Extra features include the ability to save and load a task file from the computer and the ability to set a weight for each task, "
                                                "making it more likely to show up in a random draw.\n\n"
                                                "For help or more information, contact the author at nickmallay@hotmail.com"),
                                                help_text.config(state="disabled")))
    about_help_button.pack(side="left")
    # Add a Button to display "Add / Remove"
    add_remove_help_button = tk.Button(frame_help_button, 
                             text="Add / Remove",                              
                             command=lambda: 
                             (help_text.config(state="normal"), 
                              help_text.delete("1.0", tk.END), 
                              help_text.insert("1.0",                                               
                                               "While on 'Add' mode, you will be able to enter a task that needs doing into the entry field.\n\n"
                                               "Below you will see another box for entering a task weight.\n"
                                               "Weight is how imporant a task is. A task with a weight of 5 will be much more likely to be pulled on a random draw than a task with a weight of 1.\n\n"
                                               "You can toggle the Add / Remove checkbox into 'Remove' mode by clicking it.\n"
                                               "Enter the number of the task you want to remove into the same box you entered the task.\n\n"
                                               "You can see which number corressponds to which task by checking the task list below."),
                                                help_text.config(state="disabled")))
    add_remove_help_button.pack(side="left")
    # Add a Button to display "Save/Load"
    save_load_help_button = tk.Button(frame_help_button, 
                             text="Save / Load",                              
                             command=lambda: 
                             (help_text.config(state="normal"), 
                              help_text.delete("1.0", tk.END), 
                              help_text.insert("1.0", 
                                                "The 'Save' and 'Load' buttons are located at the top left of the main window.\n\n"
                                                "Use 'Save' to store your current task list so you can pick up where you left off.\n\n"
                                                "'Load' allows you to bring back a previously saved list of tasks, making sure your progress is never lost.\n\n"
                                                "Saving is ideal before closing the program, while loading lets you resume your work later."),
                                                help_text.config(state="disabled")))
    save_load_help_button.pack(side="left")
    # Add a Button to display "Random Draw"
    draw_help_button = tk.Button(frame_help_button, 
                             text="Random Draw",                              
                             command=lambda: 
                             (help_text.config(state="normal"), 
                              help_text.delete("1.0", tk.END), 
                              help_text.insert("1.0", 
                                               "Select 'Random Draw' to have the program randomly choose a task from your list.\n\n" 
                                               "This is perfect when you’re unsure where to start or want to be surprised by your next activity.\n\n" 
                                               "The program takes task weights into account, making a task with a weight of 5 much more likely to be chosen than a task with a weight of 1."),
                                                help_text.config(state="disabled")))
    draw_help_button.pack(side="left")
    # Add a button to close the popup
    help_close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
    help_close_button.pack(pady=10)

# Function to open a draw task window
def open_draw():
    #Create a new window
    draw_window = tk.Toplevel(root)
    draw_window.title("Random Task Generator - Draw")
    draw_window.geometry("300x200")

    def random_draw():
        if not task_list:
            chosen_task_field.config(state="normal")
            chosen_task_field.delete("1.0", tk.END)
            chosen_task_field.insert("1.0","There are no tasks to choose from! Add some or load a file.")
            chosen_task_field.config(state="disabled")
        else:
            weighted_list = []
            for task in task_list:
                weighted_list.extend([task['task']] * int(task['weight']))
            selected_task = random.choice(weighted_list)            
            chosen_task_field.config(state="normal")
            chosen_task_field.delete("1.0", tk.END)
            chosen_task_field.insert("1.0", selected_task)
            chosen_task_field.config(state="disabled")


    
    #Add a label announcing the chosen task
    draw_label = tk.Label(draw_window, text="Your randomly chosen task is:")
    draw_label.pack(pady=2)
    #Add a text field to show the chosen task
    chosen_task_field = tk.Text(draw_window, state="disabled", width= 37, height= 7, wrap=tk.WORD, font=("Helvetica", "9"))
    chosen_task_field.pack(pady=5)
    #add a button to draw another task
    draw_another_button = tk.Button(draw_window, text="Draw Another Task", command=random_draw)
    draw_another_button.pack(pady=0)
    #Add a button to close the popup
    draw_close_button = tk.Button(draw_window, text="Close", command=draw_window.destroy)
    draw_close_button.pack(pady=0)
    random_draw()

# Function to display stored tasks in the task text field
def print_task(task_list):
    if task_list:
        task_display.config(state="normal")
        task_display.delete("1.0", tk.END)
        for index, task in enumerate(task_list, 1):
            task_display.insert(tk.END, f"{index}. {task['task']} (Weight: {task['weight']})\n")
        task_display.config(state="disabled")
    else:
        task_display.config(state="normal")
        task_display.delete("1.0", tk.END)
        task_display.insert("1.0", "There are no tasks stored! Add some or click load.")
        task_display.config(state="disabled")
# A function to add a new task to the list
def add_task():
    if task_entry.get() == "" or weight_entry.get() == "":
       feedback_label.config(text="Please enter a task and task weight.")
    else:
        task_description = task_entry.get()
        task_weight = weight_entry.get()
        task_list.append({"task": task_description, "weight": task_weight})
        task_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
        feedback_label.config(text=f"'{task_description}' had been added with a weight of '{task_weight}'")
        print_task(task_list)
# A function to remove a stored task
def remove_task():
    try:
        #Convert the user input to a number
        index = int(task_entry.get())

        #Check if the index number is actually in the list
        if len(task_list) < 1:
            feedback_label.config(text="There are no tasks to remove!")
        elif index < 1 or index > len(task_list):
            feedback_label.config(text=f"Please enter a the number corresponding to the task you want to remove. (1-{len(task_list)})")
            return
        else:
            removed_task = task_list.pop(index - 1)
            print_task(task_list)
            feedback_label.config(text=f"{removed_task['task']} has been removed.")
            task_entry.delete(0, tk.END)
    except ValueError:
        feedback_label.config(text="Error. Please enter a valid number.")

# A function to determin if pushing the Confirm Task button is in Add or Remove mode
def add_or_remove():
    if add_remove_current.get():
        add_task()
    else:
        remove_task()

#######################
# LISTS and VARIABLES
#######################
task_list = []


###########################
# USER INTERFACE ELEMENTS   
###########################

# UI initialization
root = tk.Tk()
root.title("Random Task Generator") # Window title
root.geometry("650x500") # Window size
# Variable to track current state of Add/Remove checkbox
add_remove_current = tk.BooleanVar()
add_remove_current.set(True)
# A checkbutton that determins if the entry field and button add or remove a task.
add_remove_checkbox = tk.Checkbutton(root, text="Toggle Add / Remove", variable=add_remove_current, command=add_remove_toggled)
add_remove_checkbox.grid(row= 3, column= 3)



# Save button, top left
save_button = tk.Button(root, text="Save", command=lambda: save(task_list))
save_button.grid(row=0, column=1)
# Load button, to the right of save button
load_button = tk.Button(root, text="Load", command=load)
load_button.grid(row=0, column=2)
# Feedback Label
feedback_label = tk.Label(text="")
feedback_label.grid(row=0, column=3, sticky="nw")

# Welcome label
welcome_label = tk.Label(text="Welcome to Random Task Generator!", font=("Helvetica", 21))
welcome_label.grid(row=2, column=3, pady= 20)
# A label to ask for input
task_entry_label = tk.Label(text="Please enter a task that needs to be done")
task_entry_label.grid(row=4,column=3)
# A entry field for task entry or deletion
task_entry = tk.Entry(root, width= 60)
task_entry.grid(row=5, column=3)
# A second label for weight only available when checked to add.
weight_entry_label = tk.Label(text="Please enter how important the task is from 1-5")
weight_entry_label.grid(row=6,column=3)
# A second entry field for weight, only avaialbe checked to add.
weight_entry = tk.Entry(root, width=5)
weight_entry.grid(row=7, column=3)
# A button to commit the changes written above
confirm_button = tk.Button(root, text="Click to add task", command=add_or_remove)
confirm_button.grid(row=8,column=3, pady=10)


# Create and display a task display label
task_display_label = tk.Label(root, text= "Stored Tasks:")
task_display_label.grid(row=9, column=3, sticky="s" )
# Create and display a frame to hold a text and scroll widget to show stored tasks
task_frame = tk.Frame(root)
task_frame.grid(row=10, column= 3, pady= 10)
# Create and place a text widjet into the frame to show stored tasks
task_display = tk.Text(task_frame, wrap=tk.WORD, height=10, width=40, state=tk.DISABLED)
task_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Create and place a scrollbar on the right side of the task frame to allow scrolling throuhg long lists of tasks
task_display_scrollbar = tk.Scrollbar(task_frame, command=task_display.yview)
task_display_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Sets the scrollbar to the proportionally correct position
task_display.config(yscrollcommand=task_display_scrollbar.set)

# Create and show a button to draw a task randomly
draw_button = tk.Button(root, text="Draw a task", command=open_draw)
draw_button.grid(row=11, column=3)
# Create and show a help button in bottom right corner
help_button = tk.Button(root, text="?", command=open_help)
help_button.grid(row=11, column=4, sticky="se")

# Start the main TK loop
root.mainloop()
