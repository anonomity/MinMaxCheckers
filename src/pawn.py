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

        return self.gameboard,self.posBoard

    def jump(self,destination,amount):
        pass

