from tkinter import *
root = Tk()

# Absolute positioning
Button(root, text="Absolute Placement").place(x=20, y=10)

# Relative positioning
Button(root, text="Relative").place(relx=0.8, rely=0.2, relwidth=0.5, width=10, anchor = NE)

root.mainloop()
