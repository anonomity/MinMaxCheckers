import numpy as np
import random

def checkIfEmpty(pos,board,targetPos,human):

    #check if player can move
    #player turn is person whos turns board

    #return 0: not empty(your piece is in the way)
    # 1: empty you can move
    # 2: not empty, players piece is in the way (in that case check if its jumpable

    col = pos % 8
    row = pos // 8

    ### for human
    if human ==1:
        if targetPos ==0:
            if board[row - 1][col - 1]==0:
                return 1
            elif board[row - 1][col - 1] > 21:
                return 2
            elif board[row - 1][col - 1] < 22:
                return 0
        elif targetPos == 1:
            if board[row - 1][col + 1] == 0:
                return 1
            elif board[row - 1][col + 1] > 21:
                return 2
            elif board[row - 1][col + 1] < 22:
                return 0

    ## for AI
    if human == 0:
        if targetPos == 0:
            if board[row + 1][col - 1]==0:
                return 1
            elif board[row + 1][col - 1] > 21:
                return 0
            elif board[row + 1][col - 1] < 22:
                return 2
        elif targetPos == 1:
            if board[row + 1][col + 1] == 0:
                return 1
            elif board[row + 1][col + 1] > 21:
                return 0
            elif board[row + 1][col + 1] < 22:
                return 2


def checkIfJumpable(targetPos,pos,board):

    #return 0: players piece is not jumpable
    #return 1: it is jumpable
    ###################################### should also call jumpable again to see if its rejumpable
    col = pos % 8
    row = pos // 8

    if board[row - 1][col - 1] > 21:
        #eat left
        if targetPos == 2:
            if board[row - 2][col - 2]==0:
                return True
            else:
                return False
        # eat right
        elif targetPos ==3:
            if board[row - 2][col + 2] == 0:
                return True
            else:
                return False



def findPiece(piece,board):
    pos=0

    for i in range(64):
        col = pos % n
        row = pos // n
        if board[row][col]== piece:
            return pos
        else:
            pos+=1


def movpiece(pos,targetPos,board,piece,human):
    n=8
    #pos is where piece is located
    #targetPos can either be left: 0 or right:1 or eatleft:2 or eatRight:3 or doubleTrip..ec eat: 4

    col = pos % n
    row = pos // n

    ## it means you can move to spot
    if checkIfEmpty(pos,board,targetPos,human) ==1:
        if human == 1:
            if targetPos ==0:
                board[row][col] = 0
                board[row - 1][col - 1] = piece

            elif targetPos ==1:
                board[row][col] = 0
                board[row - 1][col + 1] = piece
        elif human ==0:
            if targetPos == 0:
                board[row][col] = 0
                board[row + 1][col - 1] = piece

            elif targetPos == 1:
                board[row][col] = 0
                board[row + 1][col + 1] = piece

    ## checks if players piece is in the way
    elif checkIfEmpty(pos,board,targetPos,human) == 2:
        #checks if you can eat
        if checkIfJumpable(targetPos,pos,board):
            if targetPos == 2:
                board[row-1][col-1]=0
                board[row-2][col-2]=piece
                ## eat right
            elif targetPos == 3:
                board[row-1][col+1]=0
                board[row-2][col+2]=piece


    # it means your piece is in the way
    elif checkIfEmpty(pos,board,targetPos,human)==0:
        print("your piece is blocking this position, choose other position")
        print(" ")


    return board

#for AI, finds which pieces are movable and puts it into an array arr[
def findAvailablePiece(board):
    pos = 0
    pair = []
    arr = []
    found = False
    human = 0
    while found == False:
        pos = random.randint(0,24)
        targetPos = random.randint(0,1)

        ## you can move
        if checkIfEmpty(pos,board,targetPos,human)==1:
            col = pos % n
            row = pos // n
            if board[row][col]!=0:
                piece = board[row][col]
                return pos, targetPos, piece
                found = True
            else:
                pass






    # for i in range(24):
    #     col = pos % 8
    #     row = pos // 8
    #
    #     #check left space
    #     if checkIfEmpty(pos,board,0) == 1:
    #         pair.insert(board[row][col])
    #         pair.index(0)
    #         arr.index(pair)
    #         pair=[]
    #     #check right space
    #     elif checkIfEmpty(pos,board,1) ==1:
    #         pass
    #
    #     # it means your piece is in the way
    #     elif checkIfEmpty(pos,board,0) == 0:
    #         print("your piece is blocking this position, choose other position")
    #     elif checkIfEmpty(pos,board,1) == 0:
    #         print("your piece is blocking this position, choose other position")
    #
    #     #it means players piece is in the way so should check if you can eat
    #     elif checkIfEmpty(pos,board,0) == 2:
    #         pass #but Ai needs to check if it can eat the piece
    #     elif checkIfEmpty(pos,board,1) == 2:
    #         pass

def robotMove(gameboard):
    result = findAvailablePiece(gameBoard)
    pos = result[0]
    targetPos = result[1]
    piece = result[2]
    new = movpiece(pos,targetPos,gameBoard,piece,0)
    print(new)
    print(" ")


def startingBoard(pos,n):
    col = pos % n
    row = pos // n
    reso = col % 2
    countDown = 33
    board = np.zeros([n, n], dtype=bool)
    checkers = np.zeros([n,n], dtype=int)
    finish = False
    while finish == False:
        if row < 3:
            col = pos % n
            row = pos // n
            reso = col % 2
            if (row == 0) | (row == 2):
                if col == n - 1:
                    # print("[  ]")
                    pos += 1
                elif reso == 0:
                    # print("[" + str(countDown) + ']', end="")
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                else:
                    # print("[  ]", end="")
                    pos += 1
            elif row == 1:
                if col == n - 1:
                    # print("[" + str(countDown) + ']')
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                elif reso == 1:
                    # print("[" + str(countDown) + ']', end="")
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                else:
                    # print("[  ]", end="")
                    pos += 1
        elif (row == 3) | (row == 4):
            bracks = "[  ]" * 8
            # print(bracks)
            pos = pos + 8
            col = pos % n
            row = pos // n
        elif row > 4 & row < 8:
            col = pos % n
            row = pos // n
            reso = col % 2
            if (row == 5) | (row == 7):
                if (col == n - 1) & (row ==5):
                    # print("[" + str(countDown) + ']')
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                elif (col == n - 1) & (row ==7):
                    # print("[" + str(countDown) + ']')
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                    finish = True
                elif reso == 1:
                    # print("[" + str(countDown) + ']', end="")
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                else:
                    # print("[  ]", end="")
                    pos += 1
            elif (row == 6):
                if col == n - 1:
                    # print("[  ]")
                    pos += 1
                elif reso == 0:
                    # print("[" + str(countDown) + ']', end="")
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                else:
                    # print("[  ]", end="")
                    pos += 1

    return board,checkers




if __name__ == "__main__":
    end = False
    n = 8
    board= np.zeros([n,n], dtype= bool)
    # gameBoard = [[False] * 8 for _ in range(8)]  # Proper initialization.

    p = startingBoard(0,8)
    boolBoard = p[0]
    gameBoard = p[1]
    print(p[1])


    while end == False:
        print(" ")
        piece =input("Which piece you want to move")
        print(" ")
        pos = findPiece(int(piece),gameBoard)
        direction = input("left:0 or right:1 or eatleft:2 or eatright:3?")
        print(" ")
        new = movpiece(pos, int(direction), gameBoard, piece,1)
        gameBoard = new

        robotMove(gameBoard)
        print(gameBoard)


