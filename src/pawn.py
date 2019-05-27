class pawn():

    def __init__(self,human,pos,gameboard,number,posBoard):
        if human == 1:
            human = 1
        else:
            human = 0
        self.human = human
        self.pos = pos
        self.gameboard = gameboard
        self.number = number
        self.posBoard = posBoard

    def checkEmpty(self,row,col):

        if self.gameboard[row][col]==0:
            return 1
        elif self.gameboard[row][col]!=0:
            return 0

    def mov(self,destination):
        col = self.pos % 8
        row = self.pos // 8


        if self.human == 1:
            if destination ==0:
                if self.checkEmpty(row-1,col-1):
                    self.gameboard[row][col] = 0
                    self.gameboard[row - 1][col - 1] = self.number
                    p = self.posBoard[row - 1][col - 1]
                    self.pos = p

                else:
                    print("unable to move to that position")
            elif destination ==1:
                if self.checkEmpty(row-1,col+1):
                    self.gameboard[row][col] = 0
                    self.gameboard[row - 1][col + 1] = self.number
                    p = self.posBoard[row - 1][col + 1]
                    self.pos = p
                else:
                    print("unable to move to that position")
        elif self.human ==0:
            if destination == 0:
                if self.checkEmpty(row+1,col-1):
                    self.gameboard[row][col] = 0
                    self.gameboard[row + 1][col - 1] = self.number
                    p = self.posBoard[row + 1][col - 1]
                    self.pos = p
                else:
                    print("unable to move to that position")
            elif destination == 1:
                if self.checkEmpty(row + 1, col +1):
                    self.gameboard[row][col] = 0
                    self.gameboard[row + 1][col + 1] = self.number
                    p =  self.posBoard[row + 1][col + 1]
                    self.pos = p
                else:
                    print("unable to move to that position")


    def update(self,row,col):
        newPosition =self.posBoard[row][col]
        self.pos = newPosition

    def getPos(self):
        return self.pos

    def checkOpponent(self, row, col):
        if self.gameboard[row][col] == 0:
            return 0
        elif (self.gameboard[row][col] > 0) & (self.gameboard[row][col] < 13):
            return 1

    def checkHuman(self,row,col):
        if self.gameboard[row][col] == 0:
            return 0
        elif self.gameboard[row][col] > 12:
            return 1

    def jump(self,destination,amount):
        col = self.pos % 8
        row = self.pos // 8
        if destination == 0:
            if (self.checkEmpty(row-2,col-2)) & (self.checkOpponent(row-1,col-1)):
                self.gameboard[row][col] = 0
                self.gameboard[row - 1][col - 1] = 0
                self.gameboard[row - 2][col - 2] = self.number
                p = self.posBoard[row - 2][col - 2]
                self.pos = p
            else:
                print("unable to move to that location\n")
        elif destination ==1:
            if (self.checkEmpty(row - 2, col + 2)) & (self.checkOpponent(row - 1, col + 1)):
                self.gameboard[row][col] = 0
                self.gameboard[row-1][col+1] = 0
                self.gameboard[row - 2][col + 2] = self.number
                p = self.posBoard[row - 2][col - 2]
                self.pos = p
            else:
                print("unable to move to that location\n")

