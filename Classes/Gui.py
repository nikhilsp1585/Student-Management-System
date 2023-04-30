import tkinter as tk
from tkinter import *
from tkinter import ttk
from Classes.initIcons import InitIcons
from Classes.login import Login

class GUIClass:
    def __init__(self,master):
        self.main = master
        self.icons = InitIcons()
        self.infoText = tk.StringVar()
        self.classes = [("#47a5b8",0),("#ff7f00",1)]
        # self.InitLoginScreen()

    def InitLoginScreen(self):

        self.Login = Login(self.main)
        self.Login.createLoginScreen()

    def CreateGUI(self):
        
        theme = ttk.Style(self.main)
        # print(theme.theme_names())
   
        theme.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
        theme.configure('Treeview',rowheight=35,borderwidth=0,relief='flat',font=("Bahnschrift",10,"normal"))
        theme.configure('Treeview.Heading',font=('Bahnschrift',11,'normal'),foreground='#323232')
        theme.map('Treeview',background=[('selected','skyblue')],foreground=[('selected','black')])


            
        self.mainFrame = Frame(self.main,bg='grey')
        self.mainFrame.pack(side='top',fill='both',expand=1)

        # self.menuStrip = Frame(self.mainFrame,relief='flat',height=15)
        # self.menuStrip.pack(side='top',fill='x')

        self.MainMenu = tk.Menu(self.main)

        self.File = tk.Menu(self.MainMenu,tearoff=False)
        self.MainMenu.add_cascade(label="File",menu=self.File)

        self.Data = tk.Menu(self.MainMenu,tearoff=False)
        self.MainMenu.add_cascade(label="Data",menu=self.Data)

        self.View = tk.Menu(self.MainMenu,tearoff=False)
        self.MainMenu.add_cascade(label="View",menu=self.View)

        self.Help = tk.Menu(self.MainMenu,tearoff=False)
        self.MainMenu.add_cascade(label="Help",menu=self.Help)

        self.main.config(menu=self.MainMenu)

        #PanedWindow Instance
        self.panedWindow =  tk.PanedWindow(self.mainFrame,orient='horizontal',relief='flat')

        #Sidebar Frame 
        self.sidebarFrame = Frame(self.panedWindow,bg='white',borderwidth=0,width=262,relief='flat')
        self.sidebarFrame.pack(side='top')

        #treeviewFrame 
        self.treeviewFrame = Frame(self.panedWindow,bg='white')
        self.treeviewFrame.pack(side='right')

        #sidebarFrame Child Widgets
        self.sideBar = Frame(self.sidebarFrame,bg="#343a40",relief='flat',width=262)
        self.sideBar.pack(side='top',fill='both',expand=1,pady=2,padx=2,anchor='nw')

        #Grid Manager Configuration for sideBar: To make sideBar Children resposive
        Grid.rowconfigure(self.sideBar,0,weight=0)
        Grid.columnconfigure(self.sideBar,0,weight=1) 

        #sidebarTitleLabel
        self.sidebarTitleLabel = Label(self.sideBar,text="Admin Panel",bg="#272c30",fg="#F0F0F0" ,anchor="w",font=('Bahnschrift',15,'normal'))
        self.sidebarTitleLabel.grid(column=0,columnspan=2,pady=4,row=0,padx=0,ipadx=10,sticky='nesw')

        # self.separator = Frame(self.sideBar,bg='#E6E6E6',height=2,width=200).grid(row=1,column=0,sticky='nsew',padx=10,pady=(0,4))
        #dashBoard Button
        self.dashBoardButton = Button(self.sideBar,bd=0,bg='#343a40',fg="#F0F0F0",relief='flat',anchor="w",text="Dashboard",font=('Bahnschrift',12,'normal'),activebackground="#272c30",activeforeground="#F0F0F0")
        self.dashBoardButton.grid(column=0,columnspan=2,row=1,pady=(5,0),padx=15,sticky='nesw',ipadx=5,ipady=5)
        
        self.viewStudentsDetailsButton = Button(self.sideBar,bd=0,bg='#343a40',fg="#F0F0F0",relief='flat',anchor='w',text="View Students Details",font=('Bahnschrift',12,'normal'),activebackground="#272c30",activeforeground="#F0F0F0")
        self.viewStudentsDetailsButton.grid(column=0,row=2,pady=(3,0),padx=15,ipadx=5,sticky=('nsew'),ipady=5)

        #manageStudentButton
        self.manageStudentButton = Button(self.sideBar,bd=0,bg='#343a40',fg="#F0F0F0",relief='flat',anchor="w",text="Manage Students",font=('Bahnschrift',12,'normal'),activebackground="#272c30",activeforeground="#F0F0F0")
        self.manageStudentButton.grid(column=0,columnspan=2,row=3,pady=(5,0),padx=15,sticky='nesw',ipadx=5,ipady=5)
        
        #manageStudentTray
        self.manageStudentTray = Frame(self.sideBar,bg='#343a40',relief='flat',width=262)
        self.manageStudentTray.grid(column=0,row=4,padx=15,ipadx=5,sticky='nsew')
        self.manageStudentTray.grid_remove()

        #Grid Manager Configuration for manageStudentTray: To make sideBar Children resposive
        Grid.rowconfigure(self.manageStudentTray,0,weight=0)               
        Grid.columnconfigure(self.manageStudentTray,0,weight=1)  

        #_____________________manageStudentTray Children____________________________________________
        #addStudentButton 
        self.addStudentButton = Button(self.manageStudentTray,bd=0,bg='#343a40',fg="#F0F0F0",relief='flat',anchor='w',text="Add Student",font=('Bahnschrift',12,'normal'),activebackground="#272c30",activeforeground="#F0F0F0")
        self.addStudentButton.grid(column=0,row=0,pady=(5,2),padx=10,ipadx=5,sticky='nsew',ipady=5)
     
        #removeStudentButton 
        self.removeStudentButton = Button(self.manageStudentTray,bd=0,bg='#343a40',fg="#F0F0F0",relief='flat',anchor='w',text="Remove Student",font=('Bahnschrift',12,'normal'),activebackground="#272c30",activeforeground="#F0F0F0")
        self.removeStudentButton.grid(column=0,row=1,pady=(0,2),padx=10,ipadx=5,sticky='nsew',ipady=5)

        #editStudentButton 
        self.editStudentButton = Button(self.manageStudentTray,bd=0,bg='#343a40',fg="#F0F0F0",relief='flat',anchor='w',text="Edit Student",font=('Bahnschrift',12,'normal'),activebackground="#272c30",activeforeground="#F0F0F0")
        self.editStudentButton.grid(column=0,row=2,pady=(0,3),padx=10,ipadx=5,sticky=('nsew'),ipady=5)

        #__________________________________________________________________

        #logoutButton 
        self.logoutButton = Button(self.sideBar,bd=0,bg='#343a40',relief='flat',fg='#F0F0F0',anchor='w',text="Logout",font=('Bahnschrift',12,'normal'),activebackground="#272c30",activeforeground="#F0F0F0")
        self.logoutButton.grid(column=0,row=5,pady=(3,0),padx=15,ipadx=5,sticky=('nsew'),ipady=5)

        #Add sidebarFrame and treeviewFrame as panedWindow's child
        self.panedWindow.add(self.sidebarFrame)
        self.panedWindow.add(self.treeviewFrame)

        self.topBar = Frame(self.treeviewFrame,bg='white',relief='flat')
        self.topBar.pack(side='top',fill='x',pady=(2,5),padx=5)

        Grid.rowconfigure(self.topBar,0,weight=0)               
        Grid.columnconfigure(self.topBar,0,weight=1)  

        self.infoLabel = Label(self.topBar,textvariable=self.infoText,bg="white",fg="#646464",anchor='w',font=('Bahnschrift',14,'normal'))
        self.infoText.set("Dashboard")
        self.infoLabel.grid(row=0,column=0,sticky='nsew',pady=4,padx = 5)

        self.separator = Frame(self.topBar,bg='#E6E6E6',height=2,width=1070).grid(row=1,column=0,sticky='nsew',pady=(0,2),padx=5)
        
        self.dashboardFrame = Frame(self.treeviewFrame,bg="#FFFFFF")
        self.dashboardFrame.pack(side='top',fill='both',anchor='nw',expand=1,padx=8,pady=(0,5)) 

        Grid.rowconfigure(self.dashboardFrame,0,weight=0)               
        Grid.columnconfigure(self.dashboardFrame,0,weight=0)  

        for i,j in self.classes:
            self.roundedButton = Button(self.dashboardFrame,relief='flat',height=7,width=25,anchor="nw",bd=0,text=f"Class {j+1}",font=('Bahnschrift',14,'normal'),bg=i,fg='#FFFFFF',activebackground="#FFFFFF")
            self.roundedButton.grid(row=0,column=j,padx=5,pady=5)
        


        #_____________________________________treeview Section_____________________________________________________________

        self.treeColumns = ['T','D','A']

        self.treeView = ttk.Treeview(self.treeviewFrame,style='Treeview',selectmode='extended')
        self.treeView['columns'] = self.treeColumns
        
        self.treeView.column("#0",minwidth=120,width=120,anchor='center')
        self.treeView.column("#1",minwidth=450,width=450,anchor='w')
        self.treeView.column("#2",minwidth=150,width=150,anchor='center')
        self.treeView.column("#3",minwidth=300,width=300,anchor='w')

        self.treeView.heading("#0",text="ID")
        self.treeView.heading("#1",text="Student Name")
        self.treeView.heading("#2",text="Date of Birth")
        self.treeView.heading("#3",text="Phone number")
        
        #Horizontal Scrollbar
        self.sidebarXScroll = ttk.Scrollbar(self.treeviewFrame,orient='horizontal',command=self.treeView.xview)

        #Vertical Scrollbar
        self.sidebarYScroll = ttk.Scrollbar(self.treeviewFrame,orient='vertical',command=self.treeView.yview)

        #tag_configure of treeview Widget
        self.treeView.tag_configure('even',background='gray95')
        self.treeView.tag_configure('odd',background='white')

        #______________________________________treeview Section End_________________________________________________________
        
        #Pack panedWindow
        self.panedWindow.pack(fill='both',expand=1)
        #Configuration of pane of treeviewFrame
        self.panedWindow.paneconfig(self.sidebarFrame,width=265)
        self.panedWindow.paneconfig(self.treeviewFrame,minsize=950)
