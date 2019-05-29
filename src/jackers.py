import numpy as np
import random
from board import board
from Player import Player
import copy


def min_max(board, player, opponent, depth, is_max, eval_function):
    if is_max:
        if depth == 0:  # if reached the end of the search or if there's no more moves
            return eval_function(player, board), None

        if player.check_game_over(board):
            return eval_function(player, board), None

        best_move = None

        best_score = -1  # min possible value
        moves = player.check_available_moves(board)
        for (i, j) in moves:
            temp_board = copy.deepcopy(board)
            player.mark_position(temp_board, i, j)
            score = min_max(temp_board, opponent, player, depth-1, False, eval_function)[0]
            if score > best_score:
                best_score = score
                best_move = [i, j]

    else:
        if depth == 0:  # if reached the end of the search or if there's no more moves
            return eval_function(opponent, board), None

        if player.check_game_over(board):
            return eval_function(opponent, board), None

        best_move = None
        best_score = 105  # max possible value
        moves = player.check_available_moves(board)
        for (i, j) in moves:
            temp_board = copy.deepcopy(board)
            player.mark_position(temp_board, i, j)
            score = min_max(temp_board, opponent, player, depth - 1, True, eval_function)[0]
            if score < best_score:
                best_score = score
                best_move = [i, j]

    return best_score, best_move


def play(gameboard, player):

    player = 0
    while gameboard.gameOver() == False:

        print()

        if turn == 1:
            piece = input("Which piece you want to move\n")
            print(" ")

            direction = int(input("left:0 , right:1, or jump:2?\n"))

            print(" ")
            if direction == 2:
                dir = input("which direction?\n")
                print(" ")
                amount = input("how many jumps?\n")
                gameboard.jump(int(piece), int(dir), int(amount))
            else:
                gameboard.mov(int(piece), direction)
        elif turn == -1:
            score, move = min_max(board, players[turn], players[(turn + 1) % 2], 4, True, eval_board_weighted)
            print("Selected postion (" + str(move[0]) + ", " + str(move[1]) + ")")
            valid_move, score = players[turn].mark_position(board, move[0], move[1])
            players[turn].update_scores(players[(turn + 1) % 2], score)

        gameboard.humanView()
        gameboard.printScores()

        turn = (turn + 1) % 2

if __name__ == "__main__":
    end = False
    gameboard = board()
    gameboard.HumanView()

    # pawns = gameboard.returnPawns()
    #
    # human = Player(1,gameboard,pawns)
    # Ai = Player(0,gameboard,pawns)
    # play(gameboard)
    while end == False:
        gameboard.printScores()
        piece = input("Which piece you want to move\n")
        print(" ")

        direction = int(input("left:0 , right:1, or jump:2?\n"))

        print(" ")
        if direction == 2:
            dir = input("which direction?\n")
            print(" ")
            amount = input("how many jumps?\n")
            gameboard.jump(int(piece), int(dir), int(amount))
        else:
            gameboard.mov(int(piece), direction)
        gameboard.printScores()
        print("AI turn to move")
        gameboard.AiMove()









