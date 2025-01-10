import tkinter as tk
from math import sin, cos, tan, radians, degrees, log, log10, sqrt, pow

# Memory variable and mode (Radians or Degrees)
memory = 0
angle_mode = "Degrees"  # Default mode

# Function Definitions
def click(button_text):
    """Handle button click events."""
    global memory, angle_mode
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "M+":
        try:
            memory = float(entry.get())
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "MR":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(memory))
    elif button_text == "MC":
        memory = 0
    elif button_text == "sin":
        try:
            value = float(entry.get())
            angle = radians(value) if angle_mode == "Degrees" else value
            result = sin(angle)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "cos":
        try:
            value = float(entry.get())
            angle = radians(value) if angle_mode == "Degrees" else value
            result = cos(angle)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "tan":
        try:
            value = float(entry.get())
            angle = radians(value) if angle_mode == "Degrees" else value
            if cos(angle) == 0:
                raise ValueError("Undefined")
            result = tan(angle)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Undefined")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "log":
        try:
            value = float(entry.get())
            if value <= 0:
                raise ValueError("Invalid input")
            result = log10(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "ln":
        try:
            value = float(entry.get())
            if value <= 0:
                raise ValueError("Invalid input")
            result = log(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid Input")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "RAD/DEG":
        angle_mode = "Radians" if angle_mode == "Degrees" else "Degrees"
        mode_button.config(text=f"Mode: {angle_mode}")
    else:
        entry.insert(tk.END, button_text)

# GUI Setup
window = tk.Tk()
window.title("Advanced Calculator")

# Custom Styling
window.configure(bg="#282c34")
button_bg = "#3c4047"
button_fg = "#000"
entry_bg = "#1c1f26"
entry_fg = "#61dafb"

# Entry widget for user input
entry = tk.Entry(window, font=("Arial", 20), bd=5, insertwidth=4, width=14, justify="right", bg=entry_bg, fg=entry_fg)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Button Layout
buttons = [
    ("C", 1, 0), ("M+", 1, 1), ("MR", 1, 2), ("MC", 1, 3), ("/", 1, 4),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3), ("√", 2, 4),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3), ("x²", 3, 4),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3), ("1/x", 4, 4),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("sin", 5, 3), ("cos", 5, 4),
    ("tan", 6, 3), ("log", 6, 4), ("ln", 6, 2),
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 18), bg=button_bg, fg=button_fg, command=lambda t=text: click(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Mode Button for Radians/Degrees
mode_button = tk.Button(window, text=f"Mode: {angle_mode}", padx=20, pady=20, font=("Arial", 18), bg="#5a5a5a", fg="#000", command=lambda: click("RAD/DEG"))
mode_button.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

# Make the grid cells expand with the window
for i in range(7):
    window.grid_rowconfigure(i, weight=1)
for j in range(5):
    window.grid_columnconfigure(j, weight=1)

# Run the GUI loop
window.mainloop()