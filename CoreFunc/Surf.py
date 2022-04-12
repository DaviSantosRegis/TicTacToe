import itertools as it
import sys
from CoreFunc.Containers import *
import numpy as np
import pygame as pg
class Ev():

    def __init__(self,CanvasExit = True):
        """
        Loading the pygame.Event a way simpler

        """
        self.get = None

        for self.get in pg.event.get():
            pass

        if self.get != None:
            if self.Done(pg.QUIT):
                sys.exit()
    def Done(self,K):
        if self.get != None:
            if self.get.type == K:
                return True


    def Cld(self,Rect,ActiveEv):
        self.Clded = False
        if self.Done(ActiveEv) or ActiveEv == None:
            self.pos = pg.mouse.get_pos()
            self.Clded = True
            self.Index = Iterations([[pg.Rect(RectW).collidepoint(self.pos) for RectW in RectH] for RectH in Rect]).Index(True)

        return self

def Grid(SizeAll,Tam,WithTam = True):
    QuaSize = np.array(SizeAll)//np.array(Tam)
    return [[(*(QuaSize*np.array((x,y))),*QuaSize)[:2*(int(WithTam) + 1)] for x in range(3)] for y in range(3)]




