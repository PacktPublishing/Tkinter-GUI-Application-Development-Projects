from tkinter import *

root = Tk()
Label(root, text='Click at different \n locations in the frame below').pack()
def callback(event): ##(2)
    print(dir(event))##(3) Inspecting the instance event
    print("you clicked at", event.x, event.y )##(4)
    

frame = Frame(root, bg='khaki', width=130, height=80)
frame.bind("<Button-1>", callback)##(1)
frame.pack()

root.mainloop()
