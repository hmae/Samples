#! python3.8

import psutil, time
from threading import Thread as Tr
import tkinter as tk
from tkinter import colorchooser
import json
import os
import win10toast
'''
# internet usage notifier ..
dont aware about when or why your system consume data .
i swear to catch you before your money vanish out 6_6

sorry for how agly the code is , the time was running out to draw it.
it do what it should do . we can make it better ;D
by hmae
'''
class customEntry:
    def __init__(self, master):
        self.Entry = tk.Entry(master)
        self.Entry.bind("<ReturnRelease>", self.on_return)

        self.eq = None

    def get(self):
        return self.Entry.get()
    def insert(self, index, data):
        self.Entry.insert(index, data)
    def delete(self, first, end):
        self.Entry.delete(first, end)
    def clear(self):
        self.delete(0,'end')
    def new(self, data):
        self.clear()
        self.insert(0, data)
    def on_return(self, ev):
        d = self.get()
        if self.eq != None:
            self.eq(d)
        else:
            print('Caut! no Equ to Execute [ try set eq ]')
                
def settingUI(task):
    # / not finished [setting ui window]!
    win = tk.Tk()
    options = {
        'font':'arial 8 bold',
        'foreground-color': '#fff',
        'background-color': '#000',
        'alpha-level': 0.8,
        'ui-location': [0,0],
        }
    data = getoptions()
    data.setdefault(options)
    for k,v in data.items():
        setoptions(k, v)
    data = getoptions()
    
    r, c = 1, 1
    for k,v in data.items():
        tk.Label(win, text=str(k)).grid(row=r, column=c)
        r += 1
    fonten = customEntry(win); fonten.Entry.grid(row=1, column=1)
    fgen = customEntry(win); fgen.Entry.grid(row=2, column=1)
    bgen = customEntry(win); bgen.Entry.grid(row=3, column=1)
    alphaen = customEntry(win); alphaen.Entry.grid(row=4, column=1)
    uilocen = customEntry(win); uilocen.Entry.grid(row=5, column=1)
    
    fonten.eq = lambda value: setoptions('font', value)
    fgen.eq = lambda value: setoptions('foreground-color', value)
    bgen.eq = lambda value: setoptions('background-color', value)
    alphaen.eq = lambda value: setoptions('alpha-level', value)
    uilocen.eq = lambda value: setoptions('ui-location', value)

T = 5 # a lonely lost variable :d find out where it is actually and what is it for ;D .. toast duration ..
def down():
    return psutil.net_io_counters().bytes_recv
def up():
    return psutil.net_io_counters().bytes_sent
def speed():
    a = down()
    aa = up()
    time.sleep(1)
    b = down()
    bb = up()
    return round((b-a)/1024,3), round((bb-aa)/1024,3)
def adjust(ev):
    subwin.attributes("-alpha", getoptions()['alpha-level'])
    subwin.focus_force()
        

def doExit(ev=None):
    global Tr1
    Tr1 = False
    setoptions('ui-location', LOCATIONADJUSTMENT.location)
    subwin.attributes("-alpha", 0.0)
    win.after( 2000, win.destroy )

class window_location_adjustment:
    def __init__(self, window):
        self.window = window
        self.get = False
        self.m_pos = (0,0)
        self.location = [0,0]
    def action(self, ev, state):
        if state == 'hold':
            ev.widget.bind("<Motion>", self.action2)
        else:
            ev.widget.unbind("<Motion>")
            self.get = False
            
    def action2(self, ev):
        if self.get == False:
            self.m_pos = (ev.x, ev.y)
        self.get = True
        self.move(ev)
    def move(self, ev):
        geo, locx, locy = self.window.winfo_geometry().split("+")
        
        # m_pos is the location of mouse on window
        # ev.x,ev.y is the movement
        dx = ev.x - self.m_pos[0] # get dx
        dy = ev.y - self.m_pos[1] # get dy
        
        nlocx = int(locx) + dx # clear the difference
        nlocy = int(locy) + dy # clear the difference
        self.window.geometry("+{}+{}".format( nlocx, nlocy))
        self.location = [nlocx, nlocy]
def Thread1():
    global Tr1
    use = 0
    starttime = time.time()
    endtime = time.time()
    OBJ = win10toast.ToastNotifier()
    while Tr1:
        strDown, strUp = speed()
        strusage = round(down()/1024/1024,3)
        strusage2 = round(up()/1024/1024,3)
        SYM2 = SYM = "MG"
        KK=K='kb'
        if strusage > 1024:
            strusage = round(strusage/1024,3)
            SYM = "GB"
        if strusage2 > 1024:
            strusage2 = round(strusage2/1024,3)
            SYM2 = "GB"
        if strDown > 1024:
            K="Mg"
            strDown = round(strDown/1024, 3)
        if strUp > 1024:
            KK="mg"
            strUp = round(strUp/1024, 3)
        name, signal = getWIFI()
        Lusage.config(text=f"C/D:  {strusage}  {SYM}\nC/U:  {strusage2}  {SYM2}")
        Ldown.config(text =f"D:  {strDown}  {K}")
        Lup.config(text   =f"U:  {strUp}  {KK}")
        La.config(text=f"{name}  {signal}".center(5))

        if K == 'kb':
            use += strusage
        if K == 'Mg':
            use += strusage * 1024
        global T            
        notify = lambda : OBJ.show_toast('WARRING internet speed', 'net download speed limit more than 1 mg ,,,,', duration=T, threaded=True)
        if (use > 1000) and ((time.time()-starttime) < 2 ):
            starttime = time.time()
            use = 0
            if not OBJ.notification_active() and (HS_Notify.get() == True):
                notify()
                T += 1
        else:
            starttime = time.time()
            use = 0
            
        data = getoptions()
        fs.set(data['font'])
        fg.set(data['foreground-color'])
        La.config(    fg=fg.get(), bg=getoptions()['background-color'], font=fs.get())
        Lusage.config(fg=fg.get(), bg=getoptions()['background-color'], font=fs.get())
        Ldown.config( fg=fg.get(), bg=getoptions()['background-color'], font=fs.get())
        Lup.config(   fg=fg.get(), bg=getoptions()['background-color'], font=fs.get())
        


def getoptions():
    if not os.path.exists('netsettings.txt'):
        f = open('netsettings.txt','w')
        f.close()
    with open('netsettings.txt', '+r') as F:
        data = json.load(F)
    return data
def setoptions(option, value):
    data = getoptions()
    data[option] = value
    with open('netsettings.txt', '+w') as W:
        json.dump(data, W, indent=4)

def getWIFI():
    obj = os.popen("netsh wlan show interfaces")
    output = obj.read().split("\n")
    z = {}
    for i in output:
        try:
            a = i.split(" : ")[0].replace(' ','').replace("\r",'')
            b = i.split(" : ")[1].replace("\r",'')
            z.update({a:b})
        except:
            pass
    try:
        ssid   = z["SSID"]
        bssid  = z["BSSID"]
        signal = z["Signal"]
    except:
        ssid = "not connected"
        signal = '0%'
    return ssid, signal



win = tk.Tk()
tk.Label(win, text="NET SPEED", height=5, width=20, font=("verdana",30, "bold","italic","underline",)).pack()
win.update()
win.geometry("+{}+{}".format(int(win.winfo_screenwidth()/2)-int(win.winfo_width()/2), int(win.winfo_screenheight()/2)-int(win.winfo_height()/2)))
win.overrideredirect(1)
win.after(3000, lambda : (win.attributes("-alpha", 0),win.overrideredirect(0) ))
win.title("netspeed")

win.bind("<Configure>", adjust)
subwin = tk.Toplevel()

class temp_label:
    def __init__(self, master):
        self.master = master
        self.variable = tk.Variable()
        self.label = tk.Label(master, textvariable=self.variable, bg=getoptions()['background-color'], fg=getoptions()['foreground-color'], font='arial 8 bold', relief='solid')
        self._timerout = 0.5
        self.THREADED = False
    def text(self, text):
        self.label.config(bg=getoptions()['background-color'], fg=getoptions()['foreground-color'])
        self.label.place(relx=1, rely=1, anchor='se')
        self.variable.set(round(text,3))
        self._timer = self._timerout
        if not self.THREADED:
            obj = Tr(target=self._timeout)
            obj.start()

    def _timeout(self):
        avail = True
        while avail:
            self.THREADED = True
            self._timer -= 0.01
            time.sleep(0.01)
            if self._timer <= 0:
                avail = False
        self.label.place_forget()
        self.THREADED = False
        
def SCROLL(ev):
    # in case Linux , mousewheel event has a problem with delta .
    # event will be pressbutton and checking num == 4 or 5 as scrolling event +up/-down
    V = ev.delta / 120 / 100
    current = getoptions()['alpha-level']
    new = current+V
    TEMPLABEL.text(new)
    if new <= .15:
        return
    if new >= 1.05:
        return
    setoptions('alpha-level', new)
    adjust(1)

subwin.bind('<MouseWheel>', SCROLL)

def X(x,y):
    M.post(x,y)

def Y():
    win.iconify()
    subwin.attributes("-alpha", 0)
def opencurrent():
    os.startfile(os.getcwd())
def openoptions():
    os.startfile('netsettings.txt')
    #settingUI()

def selectColor(sort):
    obj = Tr(target=colorify, args=[sort])
    obj.start()
def colorify(sort):
    f = colorchooser.askcolor(color=getoptions()[sort])
    if not isinstance(f[1] , type(None)):
        setoptions(sort, f[1])

def setfont():
    ww = tk.Toplevel()
    ww.title('F O N T')
    entry = tk.Entry(ww, fg='white', bg='black', justify='center', relief='flat', font='arial 30 bold')
    entry.insert(0, getoptions()['font'])
    entry.pack(fill='both', expand=1)
    def setfont(ev):
        value = entry.get()
        setoptions('font', value)
    entry.bind("<Return>", setfont)
    ww.mainloop()
# MENU --------- START -----------
M = tk.Menu(subwin, tearoff=0)
M.add_command(label="OpenFileLocation", command=opencurrent)
M.add_command(label="Settings", command=openoptions)
M.add_command(label="Foreground Color", command=lambda : selectColor('foreground-color'))
M.add_command(label="Background Color", command=lambda : selectColor('background-color'))
M.add_command(label="Font", command = setfont)
M.add_separator()
M.add_command(label="iconify", command=lambda: Y())
M.add_separator()
topmost = tk.Variable()
topmost.set(True)
HS_Notify = tk.BooleanVar()
HS_Notify.set(False)
subwin.attributes('-topmost', str(topmost.get()))

M.add_checkbutton(label='topmost on',
                  variable = topmost,
                  command=lambda: (subwin.attributes('-topmost', str(topmost.get()))))
M.add_checkbutton(label='HSpeed Notification on', variable=HS_Notify)
M.add_separator()
def RESTART():
    doExit()
    os.startfile('netspeed.pyw')
M.add_command(label='Restart', command=RESTART)
# MENU --------- END -----------



subwin.bind("<Button-3>", lambda ev: X(ev.x_root, ev.y_root))
win.after(1000, lambda:subwin.geometry("+{}+{}".format(getoptions()['ui-location'][0],getoptions()['ui-location'][1])))
subwin.overrideredirect(1)
subwin.title("netspeed")

line = tk.Frame(subwin, height=5); line.pack(side='top',fill='x')
CONTENT = tk.Frame(subwin)
CONTENT.pack()

TEMPLABEL = temp_label(subwin)

fg = tk.StringVar(value='#000')
fs = tk.StringVar(value='')
La = tk.Label(CONTENT, width=18,padx=5, font='arial 8 bold', bg=getoptions()['background-color'], fg=fg.get())
La.grid(row=0, column=0, columnspan=2)

iconic = tk.Label(CONTENT, text='-', font='arial 8 bold', width=1,padx=1, bg="orange", fg='#fff')
iconic.grid(row=1, column=3, columnspan=1)
iconic.bind("<ButtonRelease-1>", lambda ev : Y())
iconic.bind('<Motion>', lambda ev: iconic.config(bg='orange4'))
iconic.bind('<Leave>', lambda ev: iconic.config(bg='orange'))

close = tk.Label(CONTENT, text='x', font='arial 8 bold', width=1,padx=1, bg="red2", fg='#fff')
close.grid(row=0, column=3, columnspan=1)
close.bind("<ButtonRelease-1>", lambda ev : doExit(ev))
close.bind('<Motion>', lambda ev: close.config(bg='red4'))
close.bind('<Leave>', lambda ev: close.config(bg='red2'))

move = tk.Label(CONTENT, text='+', font='arial 8 bold', width=1,padx=1, bg="cyan4", fg='#fff')
move.grid(row=2, column=3, columnspan=1)
move.bind('<Motion>', lambda ev: move.config(bg='#0c535c'))
move.bind('<Leave>', lambda ev: move.config(bg='cyan4'))

Lusage = tk.Label(CONTENT, width=18,padx=5, bg=getoptions()['background-color'], fg=fg.get(), anchor='w')
Lusage.grid(row=1, column=0, columnspan=2, pady=2)

Ldown = tk.Label(CONTENT, width=18,padx=5, bg=getoptions()['background-color'], fg=fg.get(),anchor='w')
Ldown.grid(row=2, column=0, columnspan=2)

Lup = tk.Label(CONTENT,width=18,padx=5, bg=getoptions()['background-color'], fg=fg.get(),anchor='w')
Lup.grid(row=3, column=0, columnspan=2)


subwin.bind("<q>", doExit)
LOCATIONADJUSTMENT = window_location_adjustment(subwin)
subwin.bind("<ButtonPress-1>", lambda ev: LOCATIONADJUSTMENT.action(ev, 'hold'))
subwin.bind("<ButtonRelease-1>", lambda ev: LOCATIONADJUSTMENT.action(ev, 'naaa'))

Tr1 = True
obj = Tr(target=Thread1)
obj.start()
win.wm_protocol('WM_DELETE_WINDOW', doExit)
win.mainloop()


