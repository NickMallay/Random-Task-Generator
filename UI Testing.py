import tkinter as tk

#save and load functions for button tests
def save():
    feedback_label.config(text="Task list saved.")

def load():
    feedback_label.config(text="Task list loaded")
#Function to swap between add/remove functionality
def add_remove_toggled():
    if add_remove_current.get():
        pass
#Add a task to the list
def add():
    feedback_label.config(text=f"{task_entry.get()} added to list with a weight of {weight_entry.get()}.")

# UI initialization
root = tk.Tk()
root.title("Random Task Generator") # Window title
root.geometry("600x280") # Window size

#Variable to track current state of Add/Remove checkbox
add_remove_current = tk.BooleanVar()

#A checkbutton that determins if the entry field and button add or remove a task.
add_remove_checkbox = tk.Checkbutton(root, text="Toggle Add / Remove", variable=add_remove_current)



#save button, top left
save_button = tk.Button(root, text="Save", command=save)
save_button.grid(row=0, column=1)
#Load button, to the right of save button
load_button = tk.Button(root, text="Load", command=load)
load_button.grid(row=0, column=2)
#feedback Label
feedback_label = tk.Label(text="")
feedback_label.grid(row=0, column=3, sticky="nw")
#welcome label
welcome_label = tk.Label(text="Welcome to Random Task Generator!", font=("Helvetica", 21))
welcome_label.grid(row=2, column=3, pady= 20)
#A label to ask for input
task_entry_label = tk.Label(text="Please enter a task that needs to be done")
task_entry_label.grid(row=4,column=3)
#A entry field for task entry or deletion
task_entry = tk.Entry(root, width= 60)
task_entry.grid(row=5, column=3)
#A second label for weight only available when checked to add.
weight_entry_label = tk.Label(text="Please enter how important the task is from 1-5")
weight_entry_label.grid(row=6,column=3)
#A second entry field for weight, only avaialbe checked to add.
weight_entry = tk.Entry(root, width=5)
weight_entry.grid(row=7, column=3)
#A button to commit the changes written above
confirm_button = tk.Button(root, text="Click to add task", command=add)
confirm_button.grid(row=8,column=3, pady=10)
# Start the main TK loop
root.mainloop()
