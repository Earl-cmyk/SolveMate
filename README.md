# 🧮 Scientific Calculator (Tkinter + Math)

A **fully functional scientific calculator** built using only **Python**, **Tkinter**, and **math** — no external libraries or classes.  
Color accent: **Pink** 🎀  

---

## 📋 Features

✅ **Basic Operations**
- Addition, Subtraction, Multiplication, Division  
- Parentheses and Exponentiation (^)

✅ **Scientific Functions**
- Trigonometric: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`  
- Logarithmic: `log` (base 10), `ln` (natural log)  
- Square Root: `√`  
- Factorial: `fact`  
- Constants: `π`, `e`

✅ **Interface**
- Clean pink theme (`#ffb6c1` and `#ffe4ec`)  
- Clear button (`C`)  
- Error handling for invalid input  

---

## 🧠 How It Works

- The calculator uses `eval()` to evaluate expressions safely after replacing mathematical symbols with valid Python math expressions.
- Example conversions:
  - `^` → `**`
  - `√` → `math.sqrt`
  - `sin` → `math.sin`
  - `π` → `math.pi`
- All trigonometric and logarithmic operations rely on the `math` module.

---

## 🚀 How to Run

1. Ensure you have **Python 3.x** installed.
2. Save the script as `scientific_calculator.py`.
3. Run:
   ```bash
   python scientific_calculator.py
The GUI will appear. You can click buttons or type directly into the input field.

## 🖌️ Customization
You can change the accent color by editing:
```
bg="#ffb6c1"  # button background
root.configure(bg="#ffe4ec")  # window background
```
## ⚠️ Notes
Angle unit: Radians (default for Python math functions).
To use degrees, modify trigonometric calls to wrap with math.radians().

Do not enter arbitrary text. The app expects valid math expressions.

## 📁 Requirements
Python Standard Library only
```
tkinter
math
```
No extra installation needed.

## 🧑‍💻 Author
Developed by Dimla (for “SolveMate” project)
Built with Python 🐍 and Tkinter 🎨