#!python


'''

Weird Numpy Tricks xD
have fun .. 

this script include Threading and Multiprocessing Test

[ using Threads to do multiple tasks in the same time in one process ]
benefits >
    responsive smooth program,
    get the best benefit of time.

[ using multiprocessing to execute multiple parallel processes separately ]
benefits >
    use the full power of cpu cores


'''

import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
from threading import Thread
from PIL import Image


def viewField(width, height):
    array = np.float32(np.zeros((height, width, 3)))
    return array


def line(imgarr, x1,x2, y1,y2, color):
    field = zip(range(y1,y2),range(x1,x2))
    for i in field:
        imarr[i] = color

class drawer:
    def __init__(self, instanceDrawing:bool):
        self.instanceDrawing = instanceDrawing
            
    def rectangle(self, field, p1, p2, color, width, fill=0):
        x1,y1 = p1
        x2, y2 = p2
        if fill:
            field[y1:y2, x1:x2] = color
        else:
            field[y1:y1+width, x1:x2] = color
            field[y2:y2+width, x1:x2] = color
            field[y1:y2, x1:x1+width] = color
            field[y1:y2, x2:x2+width] = color
            field[y2:y2+width, x2:x2+width] = color
    def circle(self, center, radius, color, width, percent=1,  fill=0):
        cx, cy = center
        while self.repeat:
            #self.field = self.getfield.copy()
            for seta in range(0, int(360*percent), 2):
                x = cx+int(np.math.cos((np.math.pi/180)*seta) * radius)
                y = cy+int(np.math.sin((np.math.pi/180)*seta) * radius)
                if color is None:
                    color = lambda :np.random.random_sample(3)*255
                self.field[y:y+width,x:x+width] = color()
                if not self.instanceDrawing:
                    time.sleep(0.0105)
                if not self.repeat:
                    break
    
    def MovingAround(self, item, color):
        size = self.field.shape[0:2]
        
        dx = 10
        dy = 10
        padding = 50
        posx = padding
        posy = padding
        objsize = item.shape[0:2]
        while self.repeat:
            posx += dx
            posy += dy
            # boundary Conditions ..
            '''
                    |   p
                    |   a
            --------+   d
                        y
                padx
            '''
            if posx+objsize[1] >= size[1]-padding:
                dx = -10
            if posy+objsize[0] >= size[0]-padding:
                dy = -10
            '''
                   padx 
                p    
                a    +---+
                d    |
                y
            '''
            if posx <= padding:
                dx = 10
            if posy <= padding:
                dy = 10
            
            self.field = self.getfield.copy()
            self.field[ 0+posy:objsize[0]+posy, 0+posx:objsize[1]+posx] = item
            if not self.instanceDrawing:
                time.sleep(0.05)
            if not self.repeat:
                break
            
def prog():
    w, h = 800,600
    pin = drawer(0)
    pin.w, pin.h = w,h
    field = viewField(w,h)
    field = np.float32(field)
    
    # thinking point !
    field = cv2.cvtColor(field, cv2.COLOR_BGRA2RGB) # Doesnt do anything since it 0,0,0 color array .. what is should do with zeros !
    
    field[10:30, 50:100, 0] = 1 # set first channel to max [1 as 255 as #FF]
    field[10:30, 100:150, 1] = 1 # set second channel to max [1 as 255 as #FF]
    field[10:30, 150:200, 2] = 1 # set third channel to max [1 as 255 as #FF]
    # comment the following to see changes !
    field = cv2.cvtColor(field, cv2.COLOR_BGRA2RGB) # here take effect because it has color values already ..
    
    pin.rectangle(field, (50,50), (field.shape[1]-50, field.shape[0]-50), [0.5,0.5,0.5], 10, 0 )
    pin.field = field
    pin.getfield= field
    pin.repeat = 1
    
    def GG():
        obj1 = viewField(50,50)
        obj2 = viewField(50,50)
        obj3 = viewField(50,50)

        obj1[:, :, 0] = 1
        obj2[:, :, 1] = 1
        obj3[:, :, 2] = 1
        
        obj1 = cv2.cvtColor(obj1, cv2.COLOR_BGRA2RGB)
        obj2 = cv2.cvtColor(obj2, cv2.COLOR_BGRA2RGB)
        obj3 = cv2.cvtColor(obj3, cv2.COLOR_BGRA2RGB)
        
        bigone = np.hstack([obj1, obj2, obj3])
        
        Thread(target=pin.MovingAround, args=[bigone, '']).start()
        #return # comment this return .. to draw punch of circles xD
        for i in range(100):
            if not pin.repeat:
                return
            color = lambda :np.random.random_sample(3)
            #color=None
            Thread(target=pin.circle, args=[(400,300), np.random.randint(100,200), color, np.random.randint(1,15), 1,1]).start()
            
            time.sleep(0.03)
    Thread(target=GG).start()
    #Thread(target=pin.rectangle, args=(field, (100,100), (300,200), (0.5,0.5,0), 2, 0)).start()
    while 1:
        
        cv2.imshow('numpy player pixels coloring .. show using opencv    @hmae', pin.field)
        if cv2.waitKey(100) == ord('q'):
            pin.repeat=0
            break
    cv2.destroyAllWindows()

import multiprocessing

if __name__ == '__main__':
    print("...")
    for i in range(1):
        th = multiprocessing.Process(target = prog)
        th.start()
    





##########################################################################
##########################################################################
#######################################################################
