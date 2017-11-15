import sys

#pieces contain their current location, valid moves at that location,
class Piece:
    def __init__(self, params):
        self.params = params


# board used to store pieces
class Board:

    def __init__(self):
        pass

    def create_piece(params):
        raise NotImplementedError

    def update_loc(params):
        raise NotImplementedError

# Game controls player turns, valid player selections, valid piece moves, valid manipulation of the board
class GameEngine:

    def __init__(self):
        self.players = players
        self.player_turn = 1
        print "New game created"

    #boolean return that checks if game has ended
    def game_over():
        raise NotImplementedError

    def turn():
        raise NotImplementedError


###################################


class CheckerGameEngine(GameEngine):

    def __init__ (self):
        self.board = CheckerBoard( (8,8) )
        pass

    def movement_logic(piece):
        pass

    def game_over(self):
        pass

    def draw_board(self):
        print "Drawing"
        for xy in self.board.grid:
            print xy

        outstring = ""
        #0 1 2 3 4 5 6 7
        for i in range(0,self.board.board_size[1]):
            outstring += " " + str(i) + " "
        print outstring

        for y in range(self.board.board_size[1]-1, -1, -1):
            for x in range(self.board.board_size[0]-1, -1,-1):
                if isinstance (self.board.grid.get ( (x,y) ), Piece):
                    if self.board.grid[(x,y)].player is 1:
                        sys.stdout.write( " o " )
                    else:
                        sys.stdout.write( " x " )
                else:
                    sys.stdout.write( " - " )
            sys.stdout.write(" " + str(y))
            print ""
        pass


#simple object, only has tuples of moves kinged status and player indication
class CheckerPiece(Piece):
    #moves come from engine
    def __init__ (self, player):
        self.player = player
        self.kinged = False



class CheckerBoard(Board):

    def __init__(self, board_size):

        self.board_size = board_size
        self.grid = {}

        for y in range(0,board_size[1]):
            for x in range(0,board_size[0]):
                #game board only plays on both even, or both odd coordinate spaces ex [0,0] or [1,5] are spaces
                if (y % 2 is 0 and x % 2 is 0) or (y % 2 is not 0 and x % 2 is not 0):
                    #first 3 rows is player 1, last 3 is player 2, middle is empty
                    if y < 3:
                        self.grid[(x,y)] = CheckerPiece(1)
                    elif y > 4:
                        self.grid[(x,y)] = CheckerPiece(2)
                    else:
                        self.grid[(x,y)] = None

    def create_piece(params):
        raise NotImplementedError

    def update_loc(params):
        raise NotImplementedError




def main():
    print "Welcome"
    new_game = CheckerGameEngine()

    new_game.draw_board()

    pass

main()
