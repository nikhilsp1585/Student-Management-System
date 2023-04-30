from xv import *
from audioop import add
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tracemalloc import stop
from turtle import width
from Classes.Gui import GUIClass

def toggleManageStudentTray():
    global Con

    if(Con=="F"):
    # if (bool(gui.Con.get())):
        gui.manageStudentTray.grid()
        Con = ("T")
    else:
        gui.manageStudentTray.grid_remove()
        Con = "F"

def toggleShowStudentsDetails():
    global curWidget

    if curWidget == 'Dash' and not curWidget =='Tree':
        gui.sidebarYScroll.pack(side='right',fill='y')
        gui.treeView.pack(side='top',fill='both',anchor='nw',expand=1,padx=8,pady=(0,5))
        gui.sidebarXScroll.pack(side='bottom',fill='x')

        gui.dashboardFrame.pack_forget()
        gui.infoText.set("Student Details")
        curWidget = 'Tree'

def toggleDashboard():
    global curWidget

    if curWidget == 'Tree' and not curWidget =='Dash':
        gui.treeView.pack_forget()
        gui.sidebarYScroll.pack_forget()
        gui.sidebarXScroll.pack_forget()
        gui.dashboardFrame.pack(side='top',fill='both',anchor='nw',expand=1,padx=8,pady=(0,5))

        gui.infoText.set("Dashboard")
        curWidget = 'Dash'


# Data Operation

def createToplevel():
    toplevel = Toplevel(main)
    toplevel.geometry("350x550+320+87")
    toplevel.attributes('-topmost', 'true')
    toplevel.config(bg="#272c30")
    toplevel.grab_set()

    return toplevel

def addStudent():
    stoplevel  = createToplevel()
    
    stoplevel.title("Add a new student")
    stoplevel.mainloop()


if __name__ == "__main__":
    
    main = Tk()
    main.title("Student Management System")
    main.geometry("1150x650+108+29")

    mainWidth = main.winfo_width()
    mainHeight = main.winfo_height()

    main.minsize(930,580)
    
    #Configure Grid Manager Configuration For Dynamically resize the Widgets
    # Grid.rowconfigure(main,0,weight=1,minsize=mainWidth/2) 
    # Grid.columnconfigure(main,0,weight=1,minsize=mainHeight/2) 

    Con = "F"
    curWidget = 'Dash'
    gui = GUIClass(main)
    # gui.InitLoginScreen()
    gui.CreateGUI() 
    gui.manageStudentButton.config(command=toggleManageStudentTray)
    gui.viewStudentsDetailsButton.config(command=toggleShowStudentsDetails)
    gui.dashBoardButton.config(command=toggleDashboard)
    gui.addStudentButton.config(command=addStudent)

    main.mainloop()
