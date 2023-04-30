import tkinter as tk
from tkinter import ttk

class Login():
    def __init__(self,master):
        self.main = master
        self.alreadyloggedin = True
        
    def onCloseEvent(self):
        self.main.destroy()
    
    def loginScreenGUI(self):
        #mainFrame widget in Login Screen Toplevel window

        self.loginMainFrame = tk.Frame(self.loginScreen,bg="#343a40")
        self.loginMainFrame.pack(side='top',fill='both',expand=1)  

        self.topBar = tk.Label(self.loginMainFrame,text="Access your data to Login!",anchor="center",font=('Bahnschrift',15,'normal'),bg="#272c30",fg="#F0F0F0")
        self.topBar.pack(side='top',fill='x',pady=15,padx=(0,30))

        self.hrLine = tk.Label(self.topBar,bg="#F0F0F0")
        self.hrLine.pack(side='right',fill='y',ipady=5)

        self.loginFormControl =  tk.Frame(self.loginMainFrame,bg="#343a40")
        self.loginFormControl.pack(side='top',fill='x',padx=5,pady=5)  

        self.emailText = tk.Label(self.loginFormControl,text="Email :",font=('Bahnschrift',12,'normal'),bg="#343a40",fg="#F0F0F0")
        self.emailText.grid(row=0,column=0,sticky="nw")

        self.emailEntry = ttk.Entry(self.loginFormControl,font=('Bahnschrift',12,'normal'),width=50,background="#272c30",foreground="#F0F0F0")
        self.emailEntry.grid(row=0,column=1,sticky="nw",padx=8)
    
    def createLoginScreen(self):
        if not self.alreadyloggedin:
            self.loginScreen = tk.Toplevel(self.main)
            self.loginScreen.geometry("550x270+400+195")
            self.loginScreen.resizable(False,False)
            self.loginScreen.attributes("-topmost",'true')
            self.loginScreen.grab_set()
            self.loginScreen.protocol("WM_DELETE_WINDOW",self.onCloseEvent)
            self.loginScreenGUI()
        


 
         
