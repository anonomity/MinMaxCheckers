class Player:
    def __init__(self,human,board,pawns):


        pawns = self.orderPawns(pawns)
        self.pawns = pawns
        self.human = human
        self.board = board




    # def orderPawns(self,pawns):
    #
    #     opponentPawns = []
    #     for i in range(24):
    #         if self.human ==1:
    #             if pawns[i].getNum() > 14:
    #                 opponentPawns.insert(i,pawns[i])
    #             else:
    #                 pawns.insert(i-12,pawns[i])
    #         elif self.human ==0:
    #             if pawns[i].getNum() > 14:
    #                 pawns.insert(i - 12, pawns[i])
    #             else:
    #                 opponentPawns.insert(i, pawns[i])
    #
    #     self.opponentPawns = opponentPawns
    #
