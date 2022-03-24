import tkinter
from tkinter import *

print ("Status: OK")

#variable declarations
base = Tk()     #declaring the main window
menu_bar = Menu(base)     #declaring the menubar window
menu_items = Menu(menu_bar, tearoff=0)


#functions
def doSomething():     # function for btn widget
    print("I did something!")
def closePage():     #close the page/program
    base.destroy()
def nothingYet():     # actions for the menu bar items
    print("Nothing yet")
def donothing():
    print("do nothing")
    base.config(background='orange')

#widgets
#creating the do something button
btn = tkinter.Button(
    base,
    text="Do Something",
    command=doSomething
)
# creating the exit button
btn_exit = tkinter.Button(
    base,
    text='Exit',
    command=closePage
)
menubar = Menu(base)
filemenu = Menu(menubar, tearoff=0)


helpmenu = Menu(menubar, tearoff=0)


#widget attributes


base.geometry("550x250")     # setting the window width & height
base.resizable(False, False)    # allow resizable window
base.title('Do Something')

#menu bar
menubar.add_cascade(label="Options", menu=filemenu)

#options menu attributes
filemenu.add_command(label="Exit", command=base.quit)
filemenu.add_command(label="Option 1", command=donothing)
filemenu.add_command(label="Option 2", command=donothing)
filemenu.add_command(label="Option 3", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()

#help menu attributes
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

#output

base.config(menu=menubar)
btn.pack(ipadx=25, ipady=15, expand=True)     # adding the do something button
btn_exit.pack(ipadx=25, ipady=15, expand=True)     # adding the exit button in center but below do something button
base.mainloop()