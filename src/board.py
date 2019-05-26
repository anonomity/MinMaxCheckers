import numpy as np
from pawn import pawn

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
        for i in range(64):
            col = pos % 8
            row = pos // 8
            humanView = self.board
            if (self.board[row][col] < 13) & (self.board[row][col] != 0) :

                humanView[row][col]=69
                pos+=1
            else:
                pos+=1
        print(humanView)
        print(" ")
        # print(self.posBoard)




    def updateBoard(self,board):
        self.board = board


    def printPawns(self):
        for i in range(self.pawns.__len__()):
            print(i)

    def mov(self,number,dir):
        piece = self.pawns[number-1]
        newboard = piece.mov(dir)
        self.board = newboard[0]
        self.posBoard = newboard[1]
        self.HumanView()

    def AiMov(self):
