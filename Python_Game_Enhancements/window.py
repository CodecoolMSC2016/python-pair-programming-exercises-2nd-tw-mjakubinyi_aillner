from tkinter import *
#from tkinter import colorchooser
ablak = None

def Gomb():
    global ablak
    ablak.destroy()
   
def szoveg():
    global ablak
    w = 300
    h = 200
    ws = ablak.winfo_screenwidth() # width of the screen
    hs = ablak.winfo_screenheight() # height of the screen
    x = (ws/2)
    y = (hs/3)
    ablak.geometry('%dx%d+%d+%d' % (w, h, x, y))


    l = Label(text="\n\n\nKISEBBRE GONDOLTAM!\n\n\n") 
    gomb = Button(text="Tovább", fg="blue", command = Gomb)

    l.pack()
    gomb.pack()
    ablak.mainloop()

def create_window():
    global ablak
    ablak = Tk()


   