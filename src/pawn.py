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
        king = 0
        self.king = king
#TODO 14 and 13 are faulty 15
    def checkEmpty(self,row,col):

        if self.gameboard[row][col]==0:
            return 1
        elif self.gameboard[row][col]!=0:
            return 0

#TODO: move functionality is faulty when getting to king place

    def mov(self,destination):
        col = self.pos % 8
        row = self.pos // 8


        if self.human == 1:
            if destination ==0:
                if ((row-1) < 0) | ((col - 1) < 0):
                    pass
                elif self.checkEmpty(row-1,col-1):
                    self.gameboard[row][col] = 0
                    self.gameboard[row - 1][col - 1] = self.number
                    p = self.posBoard[row - 1][col - 1]
                    self.pos = p
                else:
                    print("unable to move to that position")

            elif destination ==1:
                if ((row - 1) < 0) | ((col + 1) > 7):
                    pass
                elif self.checkEmpty(row-1,col+1):
                    self.gameboard[row][col] = 0
                    self.gameboard[row - 1][col + 1] = self.number
                    p = self.posBoard[row - 1][col + 1]
                    self.pos = p

                else:
                    print("unable to move to that position")



        elif self.human ==0:
            if destination == 0:
                if ((row + 1) > 7) | ((col - 1) < 0):
                    pass
                elif self.checkEmpty(row+1,col-1):
                    self.gameboard[row][col] = 0
                    self.gameboard[row + 1][col - 1] = self.number
                    p = self.posBoard[row + 1][col - 1]
                    self.pos = p
                else:
                    print("unable to move to that position")

            elif destination == 1:
                if ((row + 1) > 7) | ((col + 1) > 7):
                    pass
                elif self.checkEmpty(row + 1, col +1):
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

    def getNum(self):
        return self.number

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

#TODO: Add Polyjump function for human and AI
    def jump(self,destination,amount):
        col = self.pos % 8
        row = self.pos // 8
        count = 0
        if amount ==1:
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
        else:
            for i in range(amount):
                col = self.pos % 8
                row = self.pos // 8
                if ((row - 2) < 0) | ((col - 2) < 0):
                    pass
                elif (self.checkEmpty(row-2,col-2)) & (self.checkOpponent(row-1,col-1)):
                    self.gameboard[row][col] = 0
                    self.gameboard[row - 1][col - 1] = 0
                    self.gameboard[row - 2][col - 2] = self.number
                    p = self.posBoard[row - 2][col - 2]
                    self.pos = p
                    count+=1
                elif ((col + 2) > 7 ):
                    pass
                elif (self.checkEmpty(row - 2, col + 2)) & (self.checkOpponent(row - 1, col + 1)):
                    self.gameboard[row][col] = 0
                    self.gameboard[row-1][col+1] = 0
                    self.gameboard[row - 2][col + 2] = self.number
                    p = self.posBoard[row - 2][col - 2]
                    self.pos = p
                    count += 1

    def checkForKing(self):
        row = self.pos // 8
        king = False
        if self.human == 1:
            if row ==0:
                self.king = 1
                return True
            else:
                pass
        elif self.human ==0:
            if row ==7:
                self.king =1
                return True
            else:
                pass