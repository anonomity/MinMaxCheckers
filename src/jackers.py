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
        direction = int(input("left:0 , right:1, or jump:2?\n"))

        print(" ")
        if direction ==2:
            dir = input("which direction?\n")
            print(" ")
            amount = input("how many jumps?\n")
            gameboard.jump(int(piece),int(dir),int(amount))
        else:
            gameboard.mov(int(piece), direction)
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



