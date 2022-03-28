#imports
import tkinter
from tkinter import *
from newsapi import NewsApiClient
import requests

print ("Status: OK")

#variable declarations
base = Tk()     #declaring the main window
menu_bar = Menu(base)     #declaring the menubar window
menu_items = Menu(menu_bar, tearoff=0)
frame = Frame(base)
left_frame = Frame(base)
identifierLabels = Label(base,
                         text="Identifiers",
                         justify=LEFT,
                         padx=10)

newsResponse = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=8e78d3fb179c4f219bb0f4d4145bb303")
newsapi = NewsApiClient(api_key='8e78d3fb179c4f219bb0f4d4145bb303')
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          category='business',
                                          language='en',
                                          country='us')
var = StringVar()
lbl = Message(base, textvariable = var, relief=FLAT)


# /v2/top-headlines/sources
sources = newsapi.get_sources()

#functions
def doSomething():     # function for btn widget
    print(newsResponse.json().get("articles")[1].get("author"))
    var.set(newsResponse.json().get("articles")[0])
def closePage():     #close the page/program
    base.destroy()
def nothingYet():     # actions for the menu bar items
    print("Nothing yet")
def donothing():
    print("do nothing")
def colorChange():
    base.config(background="orange")
def optionOne():
    base.config(background="yellow")
def optionTwo():
    base.config(background="orange")
def optionThree():
    base.config(background="lightblue")
#widgets
#creating the do something button
btn = tkinter.Button(
    base,
    text="Do Something",
    command=doSomething
)
#creating the low of day button
btn_low = tkinter.Button(
    base,
    text="Low",
    command=doSomething
)
#creating the height of day
btn_high = tkinter.Button(
    base,
    text="High",
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
base.config(background="lightblue")
base.geometry("550x750")     # setting the window width & height
base.resizable(False, False)    # allow resizable window
base.title('Do Something')

#menu bar
menubar.add_cascade(label="Options", menu=filemenu)

#options menu attributes
filemenu.add_command(label="Exit", command=base.quit)
filemenu.add_command(label="Option 1", command=optionOne)
filemenu.add_command(label="Option 2", command=optionTwo)
filemenu.add_command(label="Option 3", command=optionThree)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()

#help menu attributes
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

#output

base.config(menu=menubar)
identifierLabels.pack(side=LEFT)
btn.pack(ipadx=25, ipady=15, expand=True)     # adding the do something button
btn_low.pack(ipadx=5, ipady=5, expand=FALSE, side=RIGHT)     # adding the low of (day, week, month, year) button
btn_high.pack(ipadx=5, ipady=5, expand=FALSE)     # adding the low of (day, week, month, year) button
btn_exit.pack(ipadx=25, ipady=15, expand=TRUE)     # adding the exit button in center but below do something button
left_frame.pack(side=LEFT)
lbl.pack(ipadx=5, ipady=10, expand=TRUE)
frame.pack()     #left holding frame
base.mainloop()
