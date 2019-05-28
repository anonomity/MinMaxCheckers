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









