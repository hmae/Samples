#! python

# Feel Free to use this Script
# But please if you have any notice .. dont hesitate and contact me any time..
#                 [] CODER:>      hmae.py                 #


# U have to install pickle and PIL libraries
# pip install pillow
# pip install pickle

from tkinter import Tk, Button, Frame, Label, INSERT, Toplevel
from tkinter.ttk import LabelFrame
from tkinter import scrolledtext

import pickle
import time
from PIL import Image, ImageTk


class bar:
    def __init__(self, master):
        self.master = master
        #        self.barframe = tk.Frame(self.master)
        self.barframe = Frame(self.master)
        self.barframe.grid(row=0, column=0, sticky="w")

        self.buttons = {}

        self.c = 0

        img = Image.open("add.png")
        img.thumbnail((20, 20))
        img = ImageTk.PhotoImage(img)
        sc.IMG = img
        add_but = Button(
            self.barframe,
            # text="+",
            image=img,
            command=self.add,
        )
        add_but.pack(
            side="left",
        )
        # add_but.invoke()

        img2 = Image.open("label3.png")
        img2.thumbnail((20, 20))
        img2 = ImageTk.PhotoImage(img2)
        sc.IMG2 = img2
        self.img2 = img2

    def add(self, load=None):
        footer_label["text"] = f"[+] Created Note {self.c+1}"
        if len(self.buttons) >= 22:
            footer_label["text"] = f"Max Set of notes :)"
            return
        self.c += 1
        # Get name
        if load is None:
            name = str(self.c)
            # Add Widget
            cont.add(name)
        else:
            name = load
        # Create Button
        but = Button(self.barframe, text=name)
        # Configure command
        but.config(
            command=lambda: cont.show(name),
            compound="center",
            image=self.img2,
            fg="#444",
        )
        # BackUp
        self.buttons[name] = but
        # Place button
        but.pack(side="left")
        # Run the command
        # but.invoke()

    def dell(self):
        self.buttons[cont.current].destroy()


class content:
    def __init__(self, master):
        # Container Frame
        self.cont = Frame(master)
        self.cont.grid(row=1, column=0)

        # Widgets Data Base
        self.widgets = {}

        self.current = None

    def add(self, widget, load=None):
        # print("Add New :",widget)
        # Widget Container
        wid_frame = LabelFrame(self.cont, text="Note {}\n".format(widget))
        # Text Widget Creation
        # TextBox = tk.Text(wid_frame, width=w, height=h, undo=True)
        TextBox = scrolledtext.ScrolledText(wid_frame, width=w, height=h, undo=True)
        TextBox.config(wrap="word")
        TextBox.setvar("NAME", value=widget)
        if load is None:
            # TextBox.insert(tk.INSERT, "Note {}\n".format(widget))
            pass
        else:
            TextBox.insert(INSERT, load)
        TextBox.pack()
        # BackUp
        self.widgets[widget] = [wid_frame, TextBox]
        # Place Widget Frame[container]
        wid_frame.grid(row=0, column=0)

        self.show(widget)

    def show(self, widget):
        cont = self.widgets[widget]
        w = 76
        h = 21
        # print("configured !", w,h)
        cont[0].tkraise()
        cont[1].config(width=w, height=h)
        cont[1].focus_force()
        self.current = widget

        # print("Active ",self.current)

    def dell(self):
        self.widgets[self.current].desteroy()


def Ctrl_event(event):
    """New Space"""
    # print("STATE ",event.state)
    # print("key ",event.keysym)
    if event.state == 4:
        if event.keysym == "s":
            save()
        if event.keysym == "d":
            if cont.current is None:
                print("nothing in the bag !")
                footer_label["text"] = "nothing in the bag !"
                return
            if int(cont.current) <= 1:
                print("delete any note except number #1 :)")
                footer_label["text"] = "delete any note except number #1 :)"
                return
            print("Del ", cont.current)
            footer_label["text"] = "deleted [" + cont.current + "]"
            cont.widgets[cont.current][0].destroy()
            cont.widgets.pop(cont.current)
            menu.buttons[cont.current].destroy()
            menu.buttons.pop(cont.current)
            c = 1
            while True:
                try:
                    menu.buttons[str(int(cont.current) - c)].invoke()
                    # print("C = ",c)
                    break
                except:
                    c += 1


def save(cond=None):
    if cond == "new":
        footer_label["text"] = "[!] no previous DB! , Created New DB [+] load"
        DATA = {"widgets": [["1", ""]]}
        db_out = open("db.pickle.memo", "wb")
        pickle.dump(DATA, db_out)
        db_out.close()
        load()
        return
    widgets = cont.widgets
    buttons = menu.buttons
    db_out = open("db.pickle.memo", "wb")
    print("[+] Saved")
    footer_label["text"] = "[+] Saved"
    DATA = {"widgets": []}
    for i in zip(widgets.items(), buttons.items()):
        # print(f"widget: {i[0]},\nbutton: {i[1]}", end="\n")
        obj = [i[0][0], i[0][1][1].get(0.0, "end")]
        DATA["widgets"].append(obj)
        print(obj)
    pickle.dump(DATA, db_out)
    db_out.close()


def load():
    try:
        db_in = open("db.pickle.memo", "rb")
    except:
        print("no previous DB!")
        footer_label["text"] = "[!] no previous DB!"
        save("new")
        return
    try:
        data = pickle.load(db_in)
    except:
        print("EMPTY DATA")
        return
    print("[+] Loaded")
    footer_label["text"] = "[+] Loaded"
    # print(data)
    for i in data["widgets"]:
        print(i)
        cont.add(i[0], i[1])
        menu.add(i[0])


def NOTE():
    tp = Toplevel(sc)
    tp.title("Thank you xD")
    x = int(sc.winfo_screenwidth() / 2) - int(250 / 2)
    y = int(sc.winfo_screenheight() / 2) - int(50 / 2)
    tp.geometry(f"250x50+{x}+{y}")
    img = Image.open("Heart.png").resize((16, 16))
    img = ImageTk.PhotoImage(img)
    tp.img = img
    tp["bg"] = "green4"
    tp.overrideredirect(1)

    Label(tp, text=" صلي علي الحبيب ", font=("Arial", 12, "bold")).place(
        x=55, y=13, width=150, height=25
    )
    Label(tp, image=img).place(x=60, y=16)
    Label(tp, image=img).place(x=180, y=16)
    tp.focus_force()
    sc.withdraw()
    sc.after(5000, sc.destroy)


# >>>>>>>>>>>> <<<<<<<<<<<< #
# try:
# sc = tk.Tk()
sc = Tk()
w, h = 650, 420
sc.geometry(
    "{}x{}+{}+{}".format(
        w,
        h,
        int(sc.winfo_screenwidth() / 2) - int(w / 2),
        int(sc.winfo_screenheight() / 2) - int(h / 2),
    )
)
sc.wm_attributes("-alpha", 0.96)
sc.title(" MEMO      - we glad to remember what you need sir ^-^ -")
sc.resizable(0, 0)
sc.config(bg="cyan3")
sc.iconbitmap("memo.ico")

cont = content(sc)
menu = bar(sc)

# footer = tk.Frame(sc)
footer = Frame(sc)
footer.grid(row=2)
# footer_label = tk.Label(footer)
footer_label = Label(footer)
footer_label["bg"] = "cyan3"
footer_label.pack()

load()

sc.bind_all("<Key>", Ctrl_event)
sc.protocol("WM_DELETE_WINDOW", lambda: (save(), NOTE()))

sc.mainloop()
##except Exception as E:
##    print("ERROR ", E)
##    sc.destroy()
