import sys
import pygame as pg
import numpy as np
from copy import *

from CoreFunc.Containers import *
import CoreFunc.Surf as Surf

#Loading TicTacToe Logic
class TicTacToe:
    def __init__(self,n):
        self.Players = ["o","x"]
        self.SizeBoard = [n]*2
        self.Blank = ""
        self.IBoard = np.array([[self.Blank]*self.SizeBoard[1]]*self.SizeBoard[0])

        self.Board = copy(self.IBoard)
        self.IsTimePlayerIndex = 0


        self.OXWinCount = {"o":0,"x":0}

        self.Winner = None
        self.Ended = False
        self.NMarked = 0

    def Mark(self,Pos):
        if self.Board[Pos] == self.Blank:
            Player =self.Players[self.IsTimePlayerIndex]
            self.Board[Pos] = Player

            self.UpdateGameStats()

    def UpdateGameStats(self):
        WinIndexesMark = [[self.Board[y] for y in x] for x in self.WinIndexes()]

        self.NMarked += 1
        self.IsTimePlayerIndex = int(not bool(self.IsTimePlayerIndex))


        #loading someboby was winner
        for i,WinIndex in enumerate(WinIndexesMark):
            for Player in self.Players:
                if Iterations(WinIndex).all_equals(Player):
                    self.Winner = Player

                    self.Ended = True

                    break

        if self.NMarked == np.product(self.SizeBoard):
            self.Ended = True

        if self.Winner != None:
            self.OXWinCount[self.Winner] += 1

    def WinIndexes(self):
        # Rows
        n = len(self.Board)
        for r in range(n):
            yield [(r, c) for c in range(n)]
        # Columns
        for c in range(n):
            yield [(r, c) for r in range(n)]
        # Diagonal top left to bottom right
        yield [(i, i) for i in range(n)]
        # Diagonal top right to bottom left
        yield [(i, n - 1 - i) for i in range(n)]
    def Reset(self):

        self.Board = copy(self.IBoard)
        self.NMarked = 0


        self.IsTimePlayerIndex = 0
        self.Winner = None
        self.Ended = False
    
    def A_Reset(self):
        self.Reset()
        self.OXWinCount = {'o':0,'x':0}

TicTacToe = TicTacToe(3)

#Loading TicTacToe Screen
pg.init()
pg.font.init()

pg.display.set_caption("TicTacToe")
pg.display.set_icon(pg.image.load("data/icon.png"))
Width = 350
Height = 300
Canvas = pg.display.set_mode((Width, Height))
while True:
    
    Canvas.fill([0] * 3)
    Ev = Surf.Ev()

    GridPos = Surf.Grid([300] * 2, TicTacToe.SizeBoard)

    # TicTacToe Logic
    GridLean  = Ev.Cld(GridPos,None)
    GridClick = Ev.Cld(GridPos, pg.MOUSEBUTTONUP)

    
    if GridClick.Clded:
        if GridClick.Index != None:
            TicTacToe.Mark(GridClick.Index)

    # BlitingTicTacToe
    for H in range(TicTacToe.SizeBoard[0]):
        for W in range(TicTacToe.SizeBoard[1]):

            Pos = GridPos[H][W]


            pg.draw.rect(Canvas, [70] * 3, Pos)

            pg.draw.rect(Canvas, [0] * 3, Pos, 1)

            Peca = TicTacToe.Board[H][W]
            if Peca != TicTacToe.Blank:
                Img = pg.image.load("data/" + Peca + ".png")
                Canvas.blit(Img, Pos)

    # Bliting PlayerScore Score
    ScoreNumFont = pg.font.SysFont("", 50)
    ScoreImgs = list(map(lambda path: pg.transform.scale(pg.image.load("data/" + path + ".png"), [50] * 2), TicTacToe.Players))
    BGScore = pg.draw.rect(Canvas, [240]*3, [300, 0, 50, Height])
    Pos = list(BGScore.topleft)

    for indplayer in range(len(TicTacToe.Players)):
        ImgScore = Canvas.blit(ScoreImgs[indplayer], Pos)
        Pos[1] += 50
        BackgroundNScore = pg.draw.rect(Canvas, [200]*3, [*ImgScore.bottomleft, *[50] * 2])
        Pos[1] += 50
        NumScoreRect = ScoreNumFont.render(str(TicTacToe.OXWinCount[TicTacToe.Players[indplayer]]), True, [0]*3)
        PosN = np.array(BackgroundNScore.center) - np.array(NumScoreRect.get_size()) // 2
        Canvas.blit(NumScoreRect, PosN)

        if indplayer == TicTacToe.IsTimePlayerIndex:
            PlayerTimeRect = pg.Surface(ImgScore.size)
            PlayerTimeRect.fill([0]*3)
            PlayerTimeRect.set_alpha(150)
            a = Canvas.blit(PlayerTimeRect, ImgScore)
    
    if TicTacToe.Ended:
        TicTacToe.Reset()
    
    ResetButton = pg.draw.rect(Canvas,[0,255,0],[300,200,50,100])
    if Ev.Done(pg.MOUSEBUTTONUP):
        if ResetButton.collidepoint(pg.mouse.get_pos()):

            TicTacToe.A_Reset()


    pg.display.update()


