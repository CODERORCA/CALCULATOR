# importing tkinter packs for displaying time
from tkinter import *
from tkinter.ttk import *

# importing string function of time
from time import strftime

# establish the root
root = Tk()
root.title("Clock")
root.resizable(width=False, height=False)
root.attributes("-topmost", True)


# definining time in form of a string
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# customizing the label
label = Label(root, font=("Segoe UI Bold Italic", 60), background = "black", foreground = "white")
label.pack(anchor='center')

# say it is time you want to have as an output
time()

#setting the loop to keep it running
mainloop()