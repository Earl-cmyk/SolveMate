import tkinter as tk
import math

# Functions
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval_entry(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def eval_entry(expr):
    expr = expr.replace("^", "**")
    expr = expr.replace("√", "math.sqrt")
    expr = expr.replace("π", "math.pi")
    expr = expr.replace("e", "math.e")
    expr = expr.replace("sin", "math.sin")
    expr = expr.replace("cos", "math.cos")
    expr = expr.replace("tan", "math.tan")
    expr = expr.replace("log", "math.log10")
    expr = expr.replace("ln", "math.log")
    expr = expr.replace("fact", "math.factorial")
    expr = expr.replace("asin", "math.asin")
    expr = expr.replace("acos", "math.acos")
    expr = expr.replace("atan", "math.atan")
    return eval(expr)

def create_button(text, row, col, colspan=1):
    btn = tk.Button(root, text=text, font=("Arial", 14, "bold"), bg="#ffb6c1",
                    fg="black", height=2, width=6, relief="ridge", borderwidth=2)
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
    btn.bind("<Button-1>", click)

# GUI setup
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#ffe4ec")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=6, pady=10, padx=10, ipady=10, sticky="nsew")

buttons = [
    ["C", "(", ")", "^", "√", "/"],
    ["7", "8", "9", "*", "sin", "cos"],
    ["4", "5", "6", "-", "tan", "log"],
    ["1", "2", "3", "+", "ln", "π"],
    ["0", ".", "fact", "e", "asin", "acos"],
    ["atan", "=", "", "", "", ""]
]

for r, row in enumerate(buttons, start=1):
    for c, val in enumerate(row):
        if val != "":
            create_button(val, r, c)

# Grid scaling
for i in range(6):
    root.grid_columnconfigure(i, weight=1)
for i in range(len(buttons) + 1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
