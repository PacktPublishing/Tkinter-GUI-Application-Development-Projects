from tkinter import *
root = Tk() 
my_label = Label(root,text="I am a label widget")    #(1)
my_button = Button(root,text="I am a button")        #(2)
my_label.pack()                                      #(3)
my_button.pack()                                     #(4)
root.mainloop()
