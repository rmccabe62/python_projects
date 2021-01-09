import shutil
import os
import datetime as dt
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

        self.btnCheckFiles = Button(self.master, text="Check for Files...", height=2)
        self.btnCheckFiles.grid(row=4, column=0, padx=(25,0), pady=(10,0))
        self.btnCloseProgram = Button(self.master, text="Close Program", height=2)
        self.btnCloseProgram.grid(row=4, column=2, padx=(350,0), pady=(10,0))
        
    def browseFile1(self):
        filePath1 = filedialog.askdirectory()
        self.varFileName1.set(filePath1)

    def browseFile2(self):
        filePath2 = filedialog.askdirectory()
        self.varFileName2.set(filePath2)


    source = 'C:/Users/rmcca/OneDrive/Documents/GitHub/python_projects/newFiles/'

    # get the files that have been modified in the last 24 hours
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)

    for root, dirs,files in os.walk('.'):
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                print('%s modified %s'%(path, mtime))
                
    # set the destination pathy to the modified files
    destination = 'C:/Users/rmcca/OneDrive/Documents/GitHub/python_projects/updatedFiles/'
    files = os.listdir(source)

    for i in files:
        #move the files represented by i to the destination folder
        shutil.move(source+i, destination)



























if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
