import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Shop Now')

        
        
        self.txtEnterChoice = Entry(self.master, font=("Helvetica", 16))
        self.txtEnterChoice.grid(row=2, column=2, columnspan=3, padx=(100,0), pady=(80,0))
        self.lblEnterTxt = Label(self.master, text="Enter Text: ",)
        self.lblEnterTxt.grid(row=2, column=0, padx=(10,0), pady=(80,0))
        self.lblTextResult = Label(self.master, text="")
        self.lblTextResult.grid(row=3, column=0, padx=(10,0), pady=(80,0))

        self.btnAddTxt = Button(self.master, text="Add Text", command=self.addText)
        self.btnAddTxt.grid(row=2, column=5, padx=(10,0), pady=(80,0))
        
        self.btnCreatePg = Button(self.master, text="Webpage", command=self.CreateWebpage)
        self.btnCreatePg.grid(row=3, column=0, padx=(10,0), pady=(40,0))

    def addText(self):
        getText = self.txtEnterChoice.get()
        self.lblTextResult.config(text=getText)

    def CreateWebpage(self):
        f = open("shop_options.html", "w")
        f = open("shop_options.html", "a")

        
        url = "shop_options.html"
        user_text = self.txtEnterChoice.get()
        f.write("<html><body><h1>"+user_text+"</h1></body></html>")
        f.close()

        webbrowser.open_new_tab(url)
        webbrowser.open_new(url)
                

        
        
               

        








if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
