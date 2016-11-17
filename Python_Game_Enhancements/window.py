from tkinter import *
#from tkinter import colorchooser
window = None


def button_command():
    global window
    window.destroy()


def write_message(text):
    global window
    w = 300
    h = 200
    ws = window.winfo_screenwidth()  # a képernyő szélessége
    hs = window.winfo_screenheight()  # a képernyo magassága
    x = (ws / 2)
    y = (hs / 3)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    l = Label(text="\n\n\n" + text + "\n\n\n")
    button = Button(text="Tovább", fg="blue", command=button_command)

    l.pack()
    button.pack()
    window.mainloop()


def create_window():
    global window
    window = Tk()
