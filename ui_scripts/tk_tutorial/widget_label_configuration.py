#! python3.6


import tkinter as tk

# Create main window
win = tk.Tk()
# Setting the title
win.title("responsive GUI Label")
# set minimum size for window resizing
win.minsize(300,100)
# set background color
win.config(bg="#9b9")

# Create Label widget
L = tk.Label(win)

# method 1 to configure label
L["text"] = "blue label".capitalize()

# dict for style options [ bg, fg, bd, ... etc]
styleoptions = {'relief':'groove', 'fg':"white", 'bd':3, 'bg':"#39f"}
# dict for font options ...
fontoptions = {'font':("calibri", 12, "italic","bold","underline")}

# method 2 to configure label
L.config(styleoptions)  # ex 1: style [colors, relief .. etc]
L.config(fontoptions)  # ex 2: font [type, size, mode .. etc]

# place manager ,, options . as a dict
placeoptions = {'relx':0.5, 'rely':0.5, 'relwidth':0.8, 'relheight':0.3, 'anchor':'center'}

# configure place options ..
L.place_configure(placeoptions)


# FLOOTING MENU TESTing
def MSG():
    '''toplevel window'''
    win2 = tk.Toplevel()
    win2.minsize(180,140)
    win2.geometry("50x50")
    msg = tk.Message(win2, bg="#afa", font=("Console", 10, "bold"))
    txt = '''hi, top level window
inherite from main win
executed from floating menu
that can be only accessed from The Blue Label'''
    msg.config(text=txt)
    msg.place(relx=0.5,rely=0.5, relwidth=1, relheight=0.9, anchor='center')

# Menu settings
fm = tk.Menu(win, tearoff=0)
fm.config(bg="#aaf",font=("courier",10,"bold"))
fm.add_command(label="about", command=MSG)

def fm_popup(menu, ev):
    menu.post(ev.x_root+5, ev.y_root)
    

L.bind("<Button-3>", lambda ev: fm_popup(fm, ev))

# start mainloop ...
win.mainloop()
