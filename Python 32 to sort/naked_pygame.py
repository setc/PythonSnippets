#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sebastián Torrente
#
# Created:     17/08/2012
# Copyright:   (c) Sebastián Torrente 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()