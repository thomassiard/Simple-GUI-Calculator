import tkinter as tk

# Create a main window
window = tk.Tk()
window.title("Simple Calculator")

# Create a text field to display calculations
display = tk.Entry(window, width=20)
display.grid(row=0, column=0, columnspan=4)

# Define functions for each operation
def add_to_display(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        clear_display()
        display.insert(0, result)
    except Exception as e:
        clear_display()
        display.insert(0, "Error")

# Create buttons for digits 0-9 and the arithmetic operations (+, -, *, /)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=5, command=calculate).grid(row=row_val, column=col_val)
    elif button in '0123456789.':
        tk.Button(window, text=button, width=5, command=lambda button=button: add_to_display(button)).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=5, command=lambda button=button: add_to_display(' ' + button + ' ')).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create clear button
tk.Button(window, text='Clear', width=20, command=clear_display).grid(row=row_val, column=0, columnspan=4)

# Run the main event loop
window.mainloop()