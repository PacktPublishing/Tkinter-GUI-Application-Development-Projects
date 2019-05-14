from tkinter import *
root = Tk()
parent = Frame(root)

#placing widgets top-down
Button(parent, text='ALL IS WELL').pack(fill=X)
Button(parent, text='BACK TO BASICS').pack(fill=X)
Button(parent, text='CATCH ME IF U CAN').pack(fill=X)

#placing widgets side by side
Button(parent, text='LEFT').pack(side=LEFT)
Button(parent, text='CENTER').pack(side=LEFT)
Button(parent, text='RIGHT').pack(side=LEFT)
parent.pack()
root.mainloop()
