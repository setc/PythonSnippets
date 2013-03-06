#Memory Puzzle
#Aquí hay unos cuantos créditos
#que me voy a saltar
#Like a boss

import random,pygame,sys
from pygame.locals import *

FPS=30 #Frames per second
WINDOWWIDTH=604 #Tamaño de ventana
WINDOWHEIGHT=480 #ditto
REVEALSPEED=8 #Velocidad de las cajas
BOXSIZE=40
GAPSIZE=10
BOARDWIDTH=10 #Número de columnas
BOARDHEIGHT=7 #Número de filas
assert(BOARDWIDTH*BOARDHEIGHT)%2==0, 'Board needs to have an even number for pairs of matches.'
XMARGIN=int((WINDOWWIDTH-(BOARDWIDTH*(BOXSIZE+GAPSIZE)))/2)
YMARGIN=int((WINDOWHEIGHT-(BOARDHEIGHT*(BOXSIZE+GAPSIZE)))/2)

#        R   G   B
GRAY    =(100, 100, 100)
NAVYBLUE=( 60,  60, 100)
WHITE   =(255, 255, 255)
RED     =(255,   0,   0)
GREEN   =(  0, 255,   0)
BLUE    =(255, 255,   0)
YELLOW  =(255, 255,   0)
ORANGE  =(255, 128,   0)
PURPLE  =(255,   0, 255)
CYAN    =(  0, 255, 255)

BGCOLOR=NAVYBLUE
LIGHTVGCOLOR=GRAY
BOXCOLOR=WHITE
HIGHLIGHTCOLOR=BLUE

DONUT='donut'
SQUARE='diamond'
DIAMOND='diamond'
LINES='lines'
OVAL='oval'

ALLCOLORS=(RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES=(DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS)*len(ALLSHAPES)*2>=BOARDWIDTH*BOARDHEIGHT, "Board is too big for the numbers of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF=pigame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mousex=0 #store x coordinate mouse event
    mousey=0 #ditto with y

    pygame.display.set_caption('Memory Game')
    mainBoard=getRandomizedBoard()
    revealedBoxes=generateRevealedBoxesData(False)

    firsSelection=None #store (x,y) de la primera caja escogida

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True: #Main Game Loop
        mouseClicked=False

        DISPLAYSURF.fill(BGCOLOR) #drawing the window
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get(): #event handling loop
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEMOTION:
                mousex, mousey=event.pos
            elif event.type==MOUSEBUTTONUP:
                mousex,mousey=event.pose
                mouseClicked=True

        boxx,boxy=getBoxAtPixel(mosex,mousey)

        if boxx!=None and boxy!=None:
            #The mouse is currently over a box.
            if not revealedBoxes[boxx][boxy]:
                drawHilightBox(boxx,boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimatioin(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy]=True #set the box as 'revealed'
                if firstSelection==None: #Current box was the first clicked
                    firsSelection=(boxx, boxy)
                else:
                    #check if there is a match between the two icons.
                    icon1shape, icon1color=getShapeAndColor(mainBoard, firsSelection[0],firsSelection[1])
                    icon2shape, icon2color=getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color