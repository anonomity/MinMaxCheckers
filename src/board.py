import numpy as np
from pawn import pawn
import copy
import random

class board():

    def __init__(self):
        pos = 0
        col = pos % 8
        row = pos // 8
        reso = col % 2
        count = 1
        board = np.zeros([8, 8], dtype=int)
        posBoard = np.zeros([8, 8], dtype=int)
        self.board = board
        self.posBoard = posBoard
        pawns = []
        self.pawns = pawns
        finish = False
        while finish == False:
            if row < 3:
                col = pos % 8
                row = pos // 8
                reso = col % 2
                if (row == 0) | (row == 2):
                    if col == 8 - 1:
                        self.posBoard[row][col] = pos
                        pos += 1
                    elif reso == 0:
                        self.board[row][col] = count

                        pawns.insert(count,pawn(0, pos, self.board, count, self.posBoard))
                        self.posBoard[row][col] = pos

                        pos += 1
                        count += 1
                    else:
                        self.posBoard[row][col] = pos
                        pos += 1
                elif row == 1:
                    if reso == 1:
                        self.board[row][col] = count

                        pawns.insert(count,pawn(0, pos, self.board, count, self.posBoard))
                        self.posBoard[row][col] = pos
                        pos += 1
                        count += 1
                    else:
                        self.posBoard[row][col] = pos
                        pos += 1
            elif (row == 3) | (row == 4):
                self.posBoard[row][col] = pos
                pos += 1
                col = pos % 8
                row = pos // 8
            elif row > 4 & row < 8:
                col = pos % 8
                row = pos // 8
                reso = col % 2
                if (row == 5) | (row == 7):
                    if (col == 8 - 1) & (row == 5):
                        self.board[row][col] = count
                        pawns.insert(count, pawn(1, pos, self.board,count, self.posBoard))
                        self.posBoard[row][col] = pos
                        pos += 1
                        count += 1
                    elif (col == 8 - 1) & (row == 7):
                        self.board[row][col] = count
                        pawns.insert(count, pawn(1, pos, self.board,count, self.posBoard))
                        self.posBoard[row][col] = pos
                        pos += 1
                        count += 1
                        finish = True
                    elif reso == 1:
                        self.board[row][col] = count

                        pawns.insert(count,pawn(1, pos, self.board,count, self.posBoard))
                        self.posBoard[row][col] = pos
                        pos += 1
                        count += 1
                    else:
                        self.posBoard[row][col] = pos
                        pos += 1
                elif (row == 6):
                    if col == 8 - 1:
                        self.posBoard[row][col] = pos
                        pos += 1
                    elif reso == 0:
                        self.board[row][col] = count

                        pawns.insert(count,  pawn(1, pos, self.board,count, self.posBoard))
                        self.posBoard[row][col] = pos
                        pos += 1
                        count += 1
                    else:
                        self.posBoard[row][col] = pos
                        pos += 1


    def HumanView(self):
        pos = 0
        humanView = copy.deepcopy(self.board)
        for i in range(64):
            col = pos % 8
            row = pos // 8
            pawnNum =humanView[row][col]
            if self.pawns[pawnNum-1].checkForKing():
                humanView[row][col] = 9915
            elif (humanView[row][col] < 13) & (humanView[row][col] != 0) :

                humanView[row][col]=69
                pos+=1
            else:
                pos+=1
        print(humanView)
        print(" ")
        # print(self.posBoard)




    def updateBoard(self,board):
        self.board = board


    def jump(self,piece, direction, amount):
        piece = self.pawns[piece-1]
        piece.jump(direction,amount)
        #self.piece.checkForKing()

    def printPawns(self):
        for i in range(self.pawns.__len__()):
            print(i)

    def mov(self,number,dir):
        piece = self.pawns[number-1]
        piece.mov(dir)
        #piece.checkForKing()
        self.HumanView()


    def checkKing(self,pawn):
        if self.pawns[pawn-1].checkForKing():
            return True
        else:
            return False


    def AiMove(self):
        found = False
        while found ==False:
            rpawn = random.randint(1,12)
            destination = random.randint(0,1)
            pos =  self.pawns[rpawn-1].getPos()
            col = pos % 8
            row = pos // 8
            if destination ==0:
                if ((row+1) > 7) | ((col - 1) < 0):
                    pass
                elif self.pawns[rpawn-1].checkEmpty(row+1,col-1):
                    self.board[row][col] = 0
                    self.board[row+1][col-1] = rpawn
                    self.pawns[rpawn-1].update(row+1,col-1)
                    found = True
                    self.HumanView()
                #check if human is there so it can eat
                elif self.pawns[rpawn-1].checkHuman(row+1,col-1):

                    #check if space is empty
                    if self.pawns[rpawn-1].checkEmpty(row+2,col-2):
                        self.pawns[rpawn - 1].update(row+2,col-2)
                        self.board[row][col] = 0
                        self.board[row + 1][col - 1] = 0
                        self.board[row + 2][col - 2] = rpawn
                    else:
                        pass
                else:
                    pass
            elif destination ==1:
                if ((row+1) > 7) | ((col + 1) > 7):
                    pass
                elif self.pawns[rpawn-1].checkEmpty(row+1,col+1):
                    self.board[row][col] = 0
                    self.board[row + 1][col + 1] = rpawn
                    self.pawns[rpawn-1].update(row + 1, col + 1)
                    found = True
                    self.HumanView()
                elif self.pawns[rpawn-1].checkHuman(row+1,col+1):
                    if self.pawns[rpawn - 1].checkEmpty(row + 2, col + 2):
                        self.pawns[rpawn - 1].update(row + 2, col + 2)
                        self.board[row][col] = 0
                        self.board[row + 1][col + 1] = 0
                        self.board[row + 2][col + 2] = rpawn
                    else:
                        pass
                else:
                    pass
        #self.pawns[rpawn-1].checkForKing()