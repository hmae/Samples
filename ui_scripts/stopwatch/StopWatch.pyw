#! python

'''
StopWatch.py
simple script to count time consumed .. 
good to control time that spend on tasks 
'''


import tkinter as tk
import time

from threading import Thread
from threading import Thread as Tr
class window_location_adjustment:
    def __init__(self, window):
        self.window = window
        self.get = False
        self.m_pos = (0,0)
        self.location = [0,0]
        window.bind('<Motion>', self.action)
    def action(self, ev):
        if ev.state == 256:
            if self.get == False:
                self.m_pos = (ev.x, ev.y)
            self.get = True
            self.move(ev)
            
        else:
            self.get = False
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


bg = '#356'
fg = '#ccc'


win = tk.Tk()
window_location_adjustment(win)
win.wm_attributes('-alpha', 0.8)
win.overrideredirect(1)
w , h = 450, 150

x = win.winfo_screenwidth() - 660
y = 20
win.withdraw()
win.geometry("{}x{}+{}+{}".format(w,h,x,y))
win.resizable(False, False)

v1 = tk.StringVar(win, value='00:00:00')
v2 = tk.StringVar(win, value='00')

fr = tk.Frame(win, relief='flat',bg=bg)
fr.pack(fill='both', expand=1)

label1 = tk.Label(fr,relief='flat',
    textvariable=v1,
    fg=fg,
    font='tahoma 70 bold italic ',
    padx=50,
    bg=bg)
label1.place(x=0, y=0)
label2 = tk.Label(fr,relief='flat',
    textvariable=v2,
    fg=fg,
    font='tahoma 30 bold italic ',
    padx=10,
    bg=bg)
label2.place(x=w-110,y=55)

def ToggleButton():
    if STANDARDS['pause'] == True:
        STANDARDS['pause'] = False
        btvar.set('Pause')
        rbtn.configure(state=tk.NORMAL)
    else:
        btvar.set('Resume')
        STANDARDS['pause'] = True
        rbtn.configure(state=tk.DISABLED)
        
def Reset():
    STANDARDS['init'] = time.time()  
    STANDARDS['pause-time'] += STANDARDS['running-time'] 
        
btvar = tk.StringVar(win, value='Pause')
pbt = tk.Button(fr,
                relief='flat',
                bg='#467',
                fg=fg,
                font='tahoma 12 bold',
                textvariable=btvar, command=ToggleButton)
pbt.place(x=70, y=115, relwidth=0.2)
    
rbtn = tk.Button(fr,
                relief='flat',
                bg='#467',
                fg=fg,
                font='tahoma 12 bold',
                text='Reset', command=Reset)
rbtn.place(x=w-180, y=115, relwidth=0.2)

from tkinter import ttk
style = ttk.Style()
style.theme_use('default')
style.configure('mystile.Vertical.TProgressbar', background='purple')

progressvisibility = 0 # change it to < 1 > to enable progress bar
PB = tk.ttk.Progressbar(
    win, style='mystile.Vertical.TProgressbar',
    orient='vertical')
#PB.place(x=w-20, y=1, height=148)

PB['value'] = 5

STANDARDS = {
    'cond':1,
    'pause':0,
    'pause-time':0,
    'init':time.time(),
    'running-time': 0,
    }
class temp_label:
    def __init__(self, master):
        self.master = master
        self.variable = tk.Variable()
        self.label = tk.Label(master, textvariable=self.variable, bg=bg, fg=fg, font='arial 8 bold', relief='solid')
        self._timerout = 0.5
        self.THREADED = False
    def text(self, text):
        self.label.config(bg=bg, fg=fg)
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
current = 0.8
def SCROLL(ev):
    # in case Linux , mousewheel event has a problem with delta .
    # event will be pressbutton and checking num == 4 or 5 as scrolling event +up/-down
    V = ev.delta / 120 / 100
    global current
    new = current+V
    
    temp.text(new)
    if new <= .15:
        return
    if new >= 1.05:
        return
    current = new
    win.attributes("-alpha", new)
temp = temp_label(win)
win.bind("<MouseWheel>",SCROLL)
from tkinter import colorchooser
def colorify(ev, *kwargs):

    f = colorchooser.askcolor()
    if not isinstance(f[1] , type(None)):
        rgb = (abs(f[0][0]-32),abs(f[0][1]-32),abs(f[0][1]-32))
        h0x = (hex(int(rgb[0])),hex(int(rgb[1])),hex(int(rgb[2])))
        new = '#' + ''.join(h0x).replace('0x','')
        for gr in kwargs:
            if ev.widget in gr:
                list(map(lambda wid: wid.config(bg=f[-1]), gr))
##        for i in widgets:
##            i.config(bg=f[1])
##        for ii in btns:
##            ii.config(bg=new)
##        
def timer(*vars):
    init = STANDARDS['init']
    while STANDARDS['cond']:
        now = time.time()-STANDARDS['pause-time']
        runningtime = now - init
        STANDARDS['running-time'] = runningtime
        ms = 100*(runningtime - int(runningtime))
        sec = int(runningtime)
        mint = sec // 60
        hour = mint // 60
        if mint >= 60:

            win.geometry("{}x{}".format(w+160,h))
            label2.place(x=w+40, y=50)
            if progressvisibility == 1:
                PB.place(x=w+140, y=1)
            rbtn.place(x=w-50)
            vars[0].set('%-2.2d:%-2.2d:%2.2d'%(hour, mint%60, sec%60))
            vars[1].set('%-2.2d'%(ms))
        else:

            win.geometry("{}x{}".format(w,h))
            label2.place(x=w-110, y=50)
            if progressvisibility == 1:
                PB.place(x=w-20, y=1, height=148)
            rbtn.place(x=w-180, )
            vars[0].set('%-2.2d:%2.2d'%(mint, sec%60))
            vars[1].set('%-2.2d'%(ms))
        PB['value'] = (runningtime%60)*1.666666666666666666667
        win.update()
        time.sleep(0.01)
        while STANDARDS['pause']:
            STANDARDS['pause-time'] = time.time()-now
            time.sleep(0.2)
    print(STANDARDS['cond'], 'loop end')

def EXIT(*args):
    STANDARDS['cond'] = False
    win.withdraw()
    print('quit')
    win.after(1000, win.destroy)
win.bind('<q>', EXIT)
win.protocol("WM_DELETE_WINDOW", EXIT)

Thread(target=timer, args=([v1,v2])).start()
win.bind("<ButtonRelease-3>", lambda ev: colorify(ev, [label1, label2, fr], [pbt], [rbtn]))
win.after(300, win.deiconify)
win.mainloop()
import sys
sys.exit()

