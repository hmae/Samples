

# hello world ;D
'it is an art :)'

import numpy as np
import cv2
import math
def show(img, wid='id'):
    if isinstance(img, str):
        cv2.imshow(wid, cv2.imread(img))
    elif isinstance(img, type(np.array([]))):
        cv2.imshow(wid, img)

w, h = 400, 400

while True:
    img = np.zeros((h,w, 3))

    color = (0,0,200) # B G R

    a = np.arange(-90,270,6)
    r = 100
    cx,cy = (200,200)
    pointWidth = 2
    for ii in np.random.randint(50,200,5):
        color = np.random.random_sample(3)
        for i in a:
            x = cx+int(math.cos((math.pi/180)*i) * ii)
            y = cy+int(math.sin((math.pi/180)*i) * ii)
            #PATTERNS
            img[y-pointWidth:y+pointWidth,x-pointWidth:x+pointWidth] = color
            img[x-pointWidth:y+pointWidth,x-pointWidth:x+pointWidth] = color
            img[y-pointWidth:x+pointWidth,x-pointWidth:x+pointWidth] = color
            img[x-pointWidth:x+pointWidth,x-pointWidth:x+pointWidth] = color

            show(img)  
            if cv2.waitKey(1) == ord('q'):
                break
    if cv2.waitKey(1000) == ord('q'):
        break
cv2.destroyAllWindows()