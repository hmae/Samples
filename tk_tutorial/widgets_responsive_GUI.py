#! python3.6


'''
any widget can be anything

place option is very powerful if you know how to use it

place provide multiple options
[like]
>> relx : relative x position according to master total width
        percentage between 0.0 and 1.0
>> rely : the same as relx , but for y direction 'height'

>> relwidth : relative width for the widget ..
        flexible width option according to master total width ..
>> relheight: the same as relwidth , but for y direction 'height'
'''

import tkinter as tk
import os

sc = tk.Tk()
sc.title(f"Responsive WIDGET location    PID({os.getpid()})")
sc.config(bg="#000")
sc.minsize(800,400)


## LINE 1
label2 = tk.Message(sc)
label2.config(text="""Simple Label [Sunken, borderwidth=30,
fixed size 200,100]
fixed location""",)

label = tk.Label(sc)
label.config(font=("Verdana", 8, "italic"))
label.config( bd=30 , relief="sunken")
label.config( bg="gray" )

label2.place(x=100,y=50, anchor="n",)
label.place(x=300,y=50, anchor="n", width=200, height=150)

def hover():
    label.config(bg="blue")
    label.config(fg="white")
def motion(ev):
    if ev.x < 255 and ev.x > 15 and ev.y < 255 and ev.y > 15:
        c = "#" + ''.join(list(map(hex, (ev.x, ev.y, 150)))).replace("0x",'')
    else:
        c = "gray"
    label.config(bg=c)
#label.bind("<Enter>", lambda ev: hover())
label.bind("<Leave>", lambda ev: label.config(bg="gray"))
label.bind("<Motion>", lambda ev: motion(ev))


## LINE 2
alabel2 = tk.Message(sc)
alabel2.config(text="""Simple Label [Sunken, borderwidth=30,
rel size relwidth=0.35,relheight=0.25]
rel location""",)
alabel = tk.Label(sc)
alabel.config(font=("Verdana", 8, "italic"))
alabel.config( bd=30 , relief="sunken")
alabel.config( bg="gray" )


alabel2.place(relx=0.15, rely=0.6, anchor="n")
alabel.place(relx=0.5, rely=0.6, anchor="n", relwidth=0.35, relheight=0.25)

def ahover():
    alabel.config(bg="blue")
    alabel.config(fg="white")
def amotion(ev):
    if ev.x < 255 and ev.x > 15 and ev.y < 255 and ev.y > 15:
        c = "#" + ''.join(list(map(hex, (ev.x, ev.y, 150)))).replace("0x",'')
    else:
        c = "gray"
    alabel.config(bg=c)
#label.bind("<Enter>", lambda ev: hover())
alabel.bind("<Leave>", lambda ev: alabel.config(bg="gray"))
alabel.bind("<Motion>", lambda ev: amotion(ev))


FULL = False
title = tk.Label(sc, text="Responsive GUI", fg="cyan", bg="#111", font=("broadway",22,"italic"))
title.place(relx=0.5, rely=0, anchor="n", relwidth=1)

footer = tk.Label(sc, text="COPYRIGHTS @ hmae.py", fg="cyan", bg="#111", font=("broadway",22,"italic"))
footer.place(relx=0.5, rely=1, anchor="s", relwidth=1)
def toggle():
    global FULL
    FULL = False if FULL else True
    return FULL
sc.bind("<F5>", lambda ev: sc.attributes("-fullscreen", toggle()))


# for playing :D

from tkinter import scrolledtext
textwidget = scrolledtext.ScrolledText(sc, font=("console", 10,"bold"))

textwidget.config(bg="#143", fg="#895", wrap="word")

textwidget.tag_config("center", justify="center", foreground="orange", font=("courier",12, "bold"))
textwidget.tag_config("red", justify="center",foreground="#f44", font=("courier",12, "bold"))

txt="""----------------
how are you
[responsive gui]
according to master
[size & position]
----------------
"""
textwidget.insert("end", txt, 'center')
textwidget.insert("end", "RIGHT WHAT EVER YOU WANT :D\n----------------", "red")
textwidget.insert("end", "\nthis is normal text\nwithout any tags\nwithout any changes\n\n")


textwidget.place(relx=0.75, relheight=1, relwidth=0.25)

textwidget_ind = tk.Label(sc, text="")
textwidget_ind.place(relx=0.75, rely=1, relwidth=0.25, anchor="sw")
# while writing ..
def update(ev):
    print(ev)
    textwidget_ind.config(text="Line: {}    Col: {}".format(*textwidget.index("insert").split(".")))
    textwidget_ind.update()
textwidget.bind("<Key>", update)


# Color Chooser
from tkinter import colorchooser

menu = tk.Menu(sc, tearoff=0)
menu.add_command(label="Choose Color", command= lambda :color(menu.NEWEVENT))
menu.add_separator()
menu.add_command(label="\u22EE",)
menu.add_command(label="Quit", command= lambda :sc.destroy())
def popup(ev):
    menu.post(ev.x_root, ev.y_root)
    menu.NEWEVENT = ev
def color(ev):
    default="#143"
    color = colorchooser.askcolor(default)
    ev.widget.config(bg=color[1])
    
    

textwidget.bind_all("<Button-3>", popup)



# LAST line but not THE LAST :D thank you ^_^
sc.state("zoomed")
sc.mainloop()

print("ENDED ,, thankyou")

