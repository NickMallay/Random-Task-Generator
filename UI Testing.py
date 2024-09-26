import tkinter as tk

#save and load functions for button tests
def save():
    feedback_label.config(text="Task list saved.")

def load():
    feedback_label.config(text="Task list loaded")
#Function to swap between add/remove functionality
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
#Add a task to the list
def add():
    feedback_label.config(text=f"{task_entry.get()} added to list with a weight of {weight_entry.get()}.")
#A function to draw another task

#Function to open a help window
def open_help():
    #Create a new window
    help_window = tk.Toplevel(root)
    help_window.title("Random Task Generator - Help")
    help_window.geometry("300x200")
    #Add helpful info about how to use the program
    help_label = tk.Label(help_window, text="test text")
    help_label.pack(pady=20)
    #Add a button to close the popup
    help_close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
    help_close_button.pack(pady=50)

#Function to open a help window
def open_draw():
    #Create a new window
    draw_window = tk.Toplevel(root)
    draw_window.title("Random Task Generator - Draw")
    draw_window.geometry("300x200")

    #A function to draw another task and display
    def draw_another():
        draw_label.config(text="test another draw")

    #Add helpful info about how to use the program
    draw_label = tk.Label(draw_window, text="test task draw")
    draw_label.pack(pady=20)
    #add a button to draw another task
    draw_another_button = tk.Button(draw_window, text="Draw Another Task", command=draw_another)
    draw_another_button.pack(pady=0)
    #Add a button to close the popup
    draw_close_button = tk.Button(draw_window, text="Close", command=draw_window.destroy)
    draw_close_button.pack(pady=0)

    

# UI initialization
root = tk.Tk()
root.title("Random Task Generator") # Window title
root.geometry("650x500") # Window size

#Variable to track current state of Add/Remove checkbox
add_remove_current = tk.BooleanVar()
add_remove_current.set(True)

#A checkbutton that determins if the entry field and button add or remove a task.

add_remove_checkbox = tk.Checkbutton(root, text="Toggle Add / Remove", variable=add_remove_current, command=add_remove_toggled)
add_remove_checkbox.grid(row= 3, column= 3)



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


#Create and display a task display label
task_display_label = tk.Label(root, text= "Stored Tasks:")
task_display_label.grid(row=9, column=3, sticky="s" )
# Create and display a frame to hold a text and scroll widget to show stored tasks
task_frame = tk.Frame(root)
task_frame.grid(row=10, column= 3)
#Create and place a text widjet into the frame to show stored tasks
task_display = tk.Text(task_frame, wrap=tk.WORD, height=10, width=40, state=tk.DISABLED)
task_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#Create and place a scrollbar on the right side of the task frame to allow scrolling throuhg long lists of tasks
task_display_scrollbar = tk.Scrollbar(task_frame, command=task_display.yview)
task_display_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# Sets the scrollbar to the proportionally correct position
task_display.config(yscrollcommand=task_display_scrollbar.set)

# Create and show a button to draw a task randomly
draw_button = tk.Button(root, text="Draw a task", command=open_draw)
draw_button.grid(row=11, column=3)
# Create and show a help button in bottom right corner
help_button = tk.Button(root, text="?", command=open_help)
help_button.grid(row=12, column=4, sticky="se")

# Start the main TK loop
root.mainloop()
