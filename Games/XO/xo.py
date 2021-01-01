

'''
Actually Creating XO is very simple to be written in pygame.
but for me i was trying to use pygame functions to understand its functionality.

so have fun with xo ;D 

by hmae
'''
import pygame
from random import randint
import time

def create_screen(func_loop=0, title="Demo", size=(400,300),):
    ## Interface Creator 
    ## USAGE Interface("name", (800,600), MainMenu)
    """
    Screen Title, >> Name of Screen
    Screen Size, >> Size ( width, height )
    Actions Loop as a Function, >> Loop of events
    """
    ## Initialization
    pygame.init()

    ## Screen
    size = size ## Screen ( width, height )

    pygame.display.set_caption( title ) ## title
    screen = pygame.display.set_mode( size ) ## window size
    #global sc
    ## once Created [ sc ] Display Interface Come Out !

    bgColor = ( 30 , 30 , 30 ) ## R G B <.> System

    screen.fill( bgColor ) ## Fill BackGround with a Color !

    if func_loop == 0:
        print("Solid SCREEN , test as u wish \nsc var >> 'sc'")
        globals().update({"sc":screen})
        pass
    else:
        func_loop(screen) ## InterFace Actions Goes Here
    
    ## Update Screen << Should be in InterFaceAction !
    #pygame.display.flip() # Or 
    #pygame.display.update()
    #return sc

def update():
    pygame.display.flip()
    return
def reset(surface):
    surface.fill((30,30,30))
    grid(sc)
def grid(surface):
    'collection of numbers . coordinates many of points;;;;'
    #################
    ##   ##   ##   ##
    #################
    ##   ##   ##   ##
    #################
    ##   ##   ##   ##
    #################
    c = [(100,200,200),(200,100,200),(200,200,100),(200,200,200),(100,100,100),
         (50,50,50),(50,100,50),(50,50,100),(100,50,100),(100,100,50)
         ]
    surface.fill(c[randint(0,len(c)-1)])
    red = (150,0,0)
    green = (0,100,100)
    
    pos_list = [(50,50),(50,100),(50,150),
                (100,50),(100,100),(100,150),
                (150,50),(150,100),(150,150),
                ]
    for pos in pos_list:
        rect = pygame.rect.Rect(pos,(50,50))
        pygame.draw.rect(surface , c[randint(0,len(c)-1)] , rect )
    '''  . → HZ
         ↓    
         VR   |----|----|----|
              |    |    |    |
              |----|----|----|
              |    |    |    |
              |----|----|----|
              |    |    |    |
              |----|----|----|
    '''
    # Hz
    pygame.draw.line(surface, red, (50,50) , (200,50), 2)
    pygame.draw.line(surface, red, (50,100) , (200,100), 2)
    pygame.draw.line(surface, red, (50,150) , (200,150), 2)
    pygame.draw.line(surface, red, (50,200) , (200,200), 2)
    # Vr
    pygame.draw.line(surface, red, (50,50) , (50,200), 2)
    pygame.draw.line(surface, red, (100,50) , (100,200), 2)
    pygame.draw.line(surface, red, (150,50) , (150,200), 2)
    pygame.draw.line(surface, red, (200,50) , (200,200), 2)
    #print(" [True] Grid")
    return 

def X(surface):
    blue = (0,0,150)
    x,y = (48,48)
    img_surf = pygame.Surface((x,y))
    img_surf.fill((0,100,100))
    pygame.draw.aaline(img_surf, blue, (10,10), (40,40), 2)
    pygame.draw.aaline(img_surf, blue, (10,40), (40,10), 2)
    pygame.draw.lines(img_surf, (200,100,200),1,
                      [(0,0),(0,x),(0,x),(x,y),(x,y),(y,0)],1)
    x = img_surf
    return x

def Y(surface):
    blue = (0,0,150)
    x,y = (48,48)
    img_surf = pygame.Surface((x,y))
    img_surf.fill((0,100,100))
    pygame.draw.circle(img_surf, blue,(25,25), 20,2)
    pygame.draw.lines(img_surf, (200,100,200),1,
                      [(0,0),(0,x),(0,x),(x,y),(x,y),(y,0)],1)
    x = img_surf
    return x

create_screen(title="X_O",size=(250,250))
grid(sc)
update()

def Play(surface):
    clock = pygame.time.Clock()
    # rect positions (x_range,y_range)
    nine_rect_positions = {
        1:((50,100),(50,100)),2:((100,150),(50,100)),3:((150,200),(50,100)),
        4:((50,100),(100,150)),5:((100,150),(100,150)),6:((150,200),(100,150)),
        7:((50,100),(150,200)),8:((100,150),(150,200)),9:((150,200),(150,200)),
        }
    def find_pos():
        for p,(x,y) in n.items():
            ##print(p,x,y)
            ##print(m_pos[0],x[0],x[1])
            ##print(m_pos[1],y[0],y[1])
            if m_pos[0] in range(x[0],x[1]) and m_pos[1] in range(y[0],y[1]):
                #print("POS:",p,(x,y))
                return (p,(x,y))
        return (None,((0,0),(0,0)))
    data = {}
    #1,2,3
    #4,5,6
    #7,8,9
    winner_cases = [
        (1,2,3),(4,5,6),(7,8,9),
        (1,4,7),(2,5,8),(3,6,9),
        (1,5,9),(3,5,7)
        ]
    while 1:
        clock.tick(20)
        old_data = data
        if len(data.keys()) == 9:
            print("Game Finish")
            reset(surface)
            data.clear()
        
        for case in winner_cases:
            # case = (1,2,3)
            x = 0
            o = 0    
            for num,t in data.items():
                if num in case:
                    # num = 1
                    if t == "X":
                        x += 1
                    if t == "O":
                        o += 1
            if x == 3:
                print("WINNER: X")
                time.sleep(1)
                for i in range(10):grid(surface)
                reset(surface)
                
                data.clear()
            elif o == 3:
                print("WINNER: O")
                time.sleep(1)
                reset(surface)
                data.clear()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ## QUIT EVENT
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN: ## MOUSE BUTTON EVENT
                m_pos = pygame.mouse.get_pos()
                m_center = (m_pos[0]-25, m_pos[1]-25)
                n = nine_rect_positions
                p,(x,y) = find_pos()
                if p == None and not pygame.mouse.get_pressed()[1]: continue
                d_pos = (x[0]+2,y[0]+2)
                if pygame.mouse.get_pressed()[2]:
                    surface.blit(Y(surface),d_pos)
                    #print("o")
                    data[p] = "O"
                if pygame.mouse.get_pressed()[0]:
                    surface.blit(X(surface),d_pos)
                    #print("x")
                    data[p] = "X"
                if pygame.mouse.get_pressed()[1]:
                    reset(surface)
        update()

Play(sc)
pygame.quit()
