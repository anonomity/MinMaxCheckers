import numpy as np
import random
from board import board



if __name__ == "__main__":
    end = False
    gameboard = board()
    gameboard.HumanView()
    while end == False:


        piece =input("Which piece you want to move\n")
        print(" ")
        direction = input("left:0 or right:1?\n")
        gameboard.mov(int(piece),int(direction))
        gameboard.AiMove()




    # while end == False:
    #     print(" ")
    #     piece =input("Which piece you want to move")
    #     print(" ")
    #     pos = findPiece(int(piece),gameBoard)
    #     direction = input("left:0 or right:1 or eatleft:2 or eatright:3?")
    #     print(" ")
    #     new = movpiece(pos, int(direction), gameBoard, piece,1)
    #     gameBoard = new
    #     print(gameBoard)
    #     print(" ")
    #     robotMove(gameBoard)



