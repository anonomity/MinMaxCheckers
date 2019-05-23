import numpy as np


def checkIfEmpty(boardType,playerturn, notTurnPlayer):

    #check if player can move
    #player turn is person whos turns board

    #return 0: not empty(your piece is in the way)
    # 1: empty you can move
    # 2: not empty, players piece is in the way (in that case check if its jumpable

    if boardType == 0:
        pass
    elif boardType ==1:
        pass


def checkIfJumpable():
    pass
    #return 0: players piece is not jumpable
    #return 1: it is jumpable
    ###################################### should also call jumpable again to see if its rejumpable



def findPiece(piece,board):
    pos=0

    for i in range(64):
        col = pos % n
        row = pos // n
        if board[row][col]== piece:
            return pos
        else:
            pos+=1


def movpiece(pos,targetPos,eat,board,piece):
    n=8
    #pos is where piece is located
    #targetPos can either be left: 0 or right:1 or eatleft:2 or eatRight:3 or doubleTrip..ec eat: 4

    col = pos % n
    row = pos // n
    if eat == 0:
        if targetPos == 0:
            board[row][col]=0
            board[row-1][col-1]= piece
        elif targetPos == 1:
            board[row][col] = 0
            board[row - 1][col + 1] = piece
    return board





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
                    print("[  ]")
                    pos += 1
                elif reso == 0:
                    print("[" + str(countDown) + ']', end="")
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                else:
                    print("[  ]", end="")
                    pos += 1
            elif row == 1:
                if col == n - 1:
                    print("[" + str(countDown) + ']')
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                elif reso == 1:
                    print("[" + str(countDown) + ']', end="")
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                else:
                    print("[  ]", end="")
                    pos += 1
        elif (row == 3) | (row == 4):
            bracks = "[  ]" * 8
            print(bracks)
            pos = pos + 8
            col = pos % n
            row = pos // n
        elif row > 4 & row < 8:
            col = pos % n
            row = pos // n
            reso = col % 2
            if (row == 5) | (row == 7):
                if (col == n - 1) & (row ==5):
                    print("[" + str(countDown) + ']')
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                elif (col == n - 1) & (row ==7):
                    print("[" + str(countDown) + ']')
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                    finish = True
                elif reso == 1:
                    print("[" + str(countDown) + ']', end="")
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                else:
                    print("[  ]", end="")
                    pos += 1
            elif (row == 6):
                if col == n - 1:
                    print("[  ]")
                    pos += 1
                elif reso == 0:
                    print("[" + str(countDown) + ']', end="")
                    board[row][col] = True
                    checkers[row][col] = countDown
                    pos += 1
                    countDown -= 1
                else:
                    print("[  ]", end="")
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
        piece =input("Which piece you want to move")
        pos = findPiece(int(piece),gameBoard)
        direction = input("left:0 or right:1?")

        new = movpiece(pos, int(direction), 0, gameBoard, piece)
        gameBoard = new
        print(gameBoard)

