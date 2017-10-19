#checkers

from CheckerPiece import Piece

print "..."

class Board:

    def __init__(self):
        #player 1 pieces
        self.square = {}
        for y in range(0,3): #1st 4 rows are player 1
            for x in range(0,10):
                #every other square
                if y % 2 is 0:
                    if x % 2 is 0:
                        self.square[(x,y)] = Piece(1)

                #odd row has piece on odd square
                else:
                    if x % 2 is not 0:
                        self.square[(x,y)] = Piece(1)
        #player 2 pieces
        for y in range(6,10):
            for x in range(0,10):
                #even row
                if y % 2 is 0:
                    if x % 2 is 0:
                        self.square[(x,y)] = Piece(2)
                #odd row
                else:
                    if x % 2 is not 0:
                        self.square[(x,y)] = Piece(2)


class Game(object)
    #creates new Board
    def __init_ (self):
        board = Board()

        self.turn = 1


    def analyze_loc(loc):
    #returns array of moves from loc
        
