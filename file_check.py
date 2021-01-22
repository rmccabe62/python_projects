import shutil
import os
import datetime 
import tkinter
from tkinter import *
from tkinter import filedialog


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Check Files')

        self.varFileName1 = StringVar()
        self.varFileName2 = StringVar()

        
        
        self.txtFileName1 = Entry(self.master, text=self.varFileName1, font=("Helvetica", 16))
        self.txtFileName1.grid(row=2, column=2, columnspan=2, padx=(200,0), pady=(100,0))

        self.txtFileName2 = Entry(self.master, text=self.varFileName2, font=("Helvetica", 16))
        self.txtFileName2.grid(row=3, column=2, columnspan=2, padx=(200,0), pady=(10,0))

        self.btnBrowse1 = Button(self.master, text="Browse...", command=self.browseFile1)
        self.btnBrowse1.grid(row=2, column=0, padx=(10,0), pady=(100,0))
        self.btnBrowse2 = Button(self.master, text="Browse...", command=self.browseFile2)
        self.btnBrowse2.grid(row=3, column=0, padx=(10,0), pady=(10,0))

        self.btnCheckFiles = Button(self.master, text="Check for Files...", height=2, command=self.checkFiles)
        self.btnCheckFiles.grid(row=4, column=0, padx=(25,0), pady=(10,0))
        self.btnCloseProgram = Button(self.master, text="Close Program", height=2)
        self.btnCloseProgram.grid(row=4, column=2, padx=(350,0), pady=(10,0))
        
    def browseFile1(self):
        filePath1 = filedialog.askdirectory()
        self.varFileName1.set(filePath1)

    def browseFile2(self):
        filePath2 = filedialog.askdirectory()
        self.varFileName2.set(filePath2)

    def checkFiles(self):
        now = datetime.datetime.now()
        ago = now-datetime.timedelta(hours=24)

        source = self.txtFileName1.get()
        destination = self.txtFileName2.get()

        files = os.listdir(source)
        for fname in files:
            path = os.path.join(source, fname)
            mtime = os.path.getmtime(path)
            timeOfFile = datetime.datetime.fromtimestamp(mtime)
            if timeOfFile > ago:
                print('%s modified %s'%(path, timeOfFile))

                shutil.move(path, destination)
        


   



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
