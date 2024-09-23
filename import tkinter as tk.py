import tkinter as tk

# Save function for button test
def save():
    file_management_label.config(text="Task list saved.")

def load():
    file_management_label.config(text="Task list loaded")

# UI initialization
root = tk.Tk()
root.title("Random Task Generator")  # Window title
root.geometry("1000x800")  # Window size

# Save button, top left
save_button = tk.Button(root, text="Save", command=save)
save_button.grid(row=0, column=1)

# Load button, to the right of save button
load_button = tk.Button(root, text="Load", command=load)
load_button.grid(row=0, column=2)

# Save/load Label
file_management_label = tk.Label(text="")
file_management_label.grid(row=0, column=3)

# Welcome label
welcome_label = tk.Label(text="Welcome to Random Task Generator!", font=("Helvetica", 21))
welcome_label.grid(row=2, column=1, columnspan=3)

# Create the Canvas widget
canvas = tk.Canvas(root, width=1000, height=800)
canvas.grid(row=3, column=0, columnspan=5, rowspan=4, sticky="nsew")

# Draw a line on the canvas to test
canvas.create_line(500, 0, 500, 800, fill="black", width=3)

# Configure grid rows and columns to allow resizing
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the main TK loop
root.mainloop()