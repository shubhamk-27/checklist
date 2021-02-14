from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("My Checklist App")
root.geometry("400x510")
root.resizable(0, 0)
root.iconbitmap("checklist.ico")

myFont = ("Times New Roman", 12)
rootColour = "#3b5998"
buttonColour = "#f7f7f7"
root.config(bg=rootColour)

inputFrame = Frame(root, bg=rootColour)
outputFrame = Frame(root, bg=rootColour)
buttonFrame = Frame(root, bg=rootColour)
inputFrame.pack()
outputFrame.pack()
buttonFrame.pack()


def printToDO():
    if listEntry.get() == "":
        messagebox.showinfo("Please Enter Something",
                            "Cannot keep the textbox empty")
    else:
        listBox.insert(END, listEntry.get())
        listEntry.delete(0, END)


def removeItem():
    listBox.delete(ANCHOR)


def removeAll():
    listBox.delete(0, END)


def saveList():
    with open("checklist.txt", 'w') as f:
        listTuple = listBox.get(0, END)
        for items in listTuple:
            f.write(items+"\n")


def openList():
    try:
        with open("checklist.txt", 'r') as f:
            for line in f:
                listBox.insert(END, line)
    except:
        pass


listEntry = Entry(inputFrame, width=32, borderwidth=3, font=myFont)
listEntry.insert(0, "Type Here")
listEntry.grid(row=0, column=0, pady=10, padx=15)
listAddButton = Button(inputFrame, text="Add Item",
                       font=myFont, command=printToDO)
listAddButton.grid(row=0, column=1, padx=5, pady=10)

scrollBar = Scrollbar(outputFrame)


listBox = Listbox(outputFrame, width=35, height=17,
                  font=("Times New Roman", 15), yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)
listBox.grid(row=0, column=0)
scrollBar.grid(row=0, column=1, sticky="NS")

listRemoveButton = Button(buttonFrame, text="Remove",
                          borderwidth=7, font=(myFont), width=8, command=removeItem)
listClearButton = Button(buttonFrame, text="Clear",
                         width=8, borderwidth=7, font=(myFont), command=removeAll)
listSaveButton = Button(buttonFrame, text="Save",
                        borderwidth=7, font=(myFont), width=8, command=saveList)
listQuitButton = Button(buttonFrame, text="Quit",
                        command=root.destroy, borderwidth=7, font=(myFont), width=8)
listRemoveButton.grid(row=0, column=0, pady=10)
listClearButton.grid(row=0, column=1)
listSaveButton.grid(row=0, column=2)
listQuitButton.grid(row=0, column=3)
openList()
root.mainloop()
