# importing tkinter for GUI
import tkinter as tk

calculation = ""

# adding functions
# global allows us to manipulate the whole content

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# evaluate calculation function using eval syntax
# note that eval is not only used for evaluating
# big security issue as it would allow to inject codes if used
# in other types of programs
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
# in case if it doesn't "add up", get it?
    except:
        clear_field()
        text_result.insert(1.0, "Imaginary number, hah!")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# Let us G(root) the textfield
root = tk.Tk()
root.geometry("350x300")
root.resizable(width=False, height=False)

text_result = tk.Text(root, height=2, width=16, font=("calibri", 24))
text_result.grid(columnspan=5)

# add buttons
# command with lambda expression
# lambda just refers to a function if called
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("calibri", 14))
# specify button location
btn_1.grid(row=2, column=1)
# rinse and repeat

# button 2
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("calibri", 14))
btn_2.grid(row=2, column=2)

# button 3
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("calibri", 14))
btn_3.grid(row=2, column=3)

# button 4
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("calibri", 14))
btn_4.grid(row=3, column=1)

# button 5
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("calibri", 14))
btn_5.grid(row=3, column=2)

# button 6
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("calibri", 14))
btn_6.grid(row=3, column=3)

# button 7
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("calibri", 14))
btn_7.grid(row=4, column=1)

# button 8
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("calibri", 14))
btn_8.grid(row=4, column=2)

# button 9
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("calibri", 14))
btn_9.grid(row=4, column=3)

# button 0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("calibri", 14))
btn_0.grid(row=5, column=1)

# buttons parenthesis
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("calibri", 14))
btn_open.grid(row=5, column=2)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("calibri", 14))
btn_close.grid(row=5, column=3)

# button +
# caution! you need to put the operator as a string into add_to_calculations
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("calibri", 14))
btn_plus.grid(row=2, column=4)

# button -
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("calibri", 14))
btn_minus.grid(row=3, column=4)

# button x
btn_multiplication = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("calibri", 14))
btn_multiplication.grid(row=4, column=4)

# button /
btn_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("calibri", 14))
btn_division.grid(row=5, column=4)

# button clear
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("calibri", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

# button equals
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("calibri", 14))
btn_equals.grid(row=6, column=3, columnspan=2, rowspan=2)

root.mainloop()
