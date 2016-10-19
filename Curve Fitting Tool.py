import Tkinter

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        self.initialize()
    
    def initialize(self):
        self.grid()
        
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set("Enter text here.")
        
        button = Tkinter.Button(self,text="Click me !",command=self.OnButtonClick)
        button.grid(column=1,row=0)
        
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set("Hello !")
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        
    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get()+" (You clicked the button)")
        
    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get()+" (You pressed ENTER)")  
              
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Curve Fitting Tool')
    app.mainloop()