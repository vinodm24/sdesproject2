import Tkinter
from Tkinter import *
from tkFileDialog import askopenfilename
#from Tkinter import messagebox

#For running multiple commands using one click
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func        
    
class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        self.initialize()
    
    def initialize(self):
        self.grid()        
        #self.entryVariable = Tkinter.StringVar()
        #self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        #self.entry.grid(row=0,column=0, columnspan=2, pady=5, padx=5)
        #self.entryVariable.set("Enter text here.")
        create = Tkinter.Button(self,text="Create Model",command = self.Window2, height = 1, width = 10)
        create.grid(row=0, column=1, sticky='E', padx=5, pady=5)
        
        use = Tkinter.Button(self,text="Use Model",command = self.OpenFile, height = 1, width = 10)
        use.grid(row=1, column=1, sticky='E', padx=5, pady=5)
        
        quit = Tkinter.Button(self,text="Quit",command = self.destroy)
        quit.grid(row=2, column=2, sticky='E', padx=5, pady=5)
        self.grid_columnconfigure(0,weight=1)
        #self.resizable(True,False)

    #For Opening a file
    def OpenFile(self):
	    filename = askopenfilename()
    
    #def Quit(self):
	#result = messagebox.askyesno("Continue?", "Do you want to quit?")
    def Window2(self):
        self.window2 = Toplevel()
        self.window2.title("Window 2")
        self.window2.transient(self)

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self.window2,textvariable=self.entryVariable)
        self.entry.grid(row=0,column=0, sticky='NSEW',columnspan=2, pady=5, padx=5)
        self.entryVariable.set("Please choose a file using import button")
        
        import_data = Button(self.window2,text="Import Data",command=self.OpenFile)
        import_data.grid(row=1,column=2, rowspan=2, sticky='NSEW')

        back = Button(self.window2, text="Back",command = self.window2.destroy, height = 1, width = 10)
        back.grid(row=1, column=0, sticky='E',pady=5, padx=5)

        next = Button(self.window2,text="Next",command=combine_funcs(self.Window3,self.window2.destroy), height = 1, width = 10)
        next.grid(row=1, column=1, sticky='E',pady=5, padx=5)

    def Window3(self):
        self.window3 = Toplevel()
        self.window3.title("Progress Bar")
        self.window3.transient(self)
        next = Button(self.window3,text="Next",command=combine_funcs(self.Window4,self.window3.destroy))
        next.grid(row=0, column=1, sticky='E',pady=5, padx=5)
        back = Button(self.window3,text="Back",command = combine_funcs(self.window3.destroy,self.Window2))
        back.grid(row=0, column=0, sticky='E',pady=5, padx=5)
        #self.topButton.pack()

    def Window4(self):
        self.window4 = Toplevel()
        self.window4.title("Model")
        save = Button(self.window4,text="Next",command=self.Window4)
        save.grid(row=0,column=1,sticky='E', pady=5, padx=5)
        back = Button(self.window4,text="Back",command = self.window4.destroy)
        back.grid(row=0, column=0, sticky='E',pady=5, padx=5)
              
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Curve Fitting Tool')
    #app.geometry("500x500")
    app.mainloop()
