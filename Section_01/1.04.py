from tkinter import *
root = Tk()

frame = Frame(root)
# demo of side and fill options
Label (frame, text="Pack Demo of side and fill").pack()
Button(frame, text="A").pack(side=LEFT, fill=Y)
Button(frame, text="B").pack(side=TOP,  fill=X)
Button(frame, text="C").pack(side=RIGHT, fill=NONE)
Button(frame, text="D").pack(side=TOP, fill=BOTH)
frame.pack() # note the top frame does not expand nor does it fill in 
                #X or Y directions

# demo of expand options - best understood by expanding the root widget
# and seeing the effect on all the three buttons below.
Label (root, text="Pack Demo of expand").pack()
Button(root, text="I do not expand").pack()
Button(root, text="I do not fill x but I expand").pack(expand = 1)
Button(root, text="I fill x and expand").pack(fill=X, expand=1)

root.mainloop()
