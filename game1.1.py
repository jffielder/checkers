#pieces contain their current location, valid moves at that location,
class Piece:
    def __init__(self, params):
        self.params = params

    def get_move_vector(piece):
        '''Returns movement vectors for a piece ex.
        [ [1,1], [-1,-1] ]
        '''
        raise NotImplementedError


# board used to store pieces
class Board:

    def __init__(self, board_size, player_count):
        self.board_size = board_size
        self.player_count = player_count

    def create_piece(params):
        raise NotImplementedError

    def update_loc(params):
        raise NotImplementedError

    def end():
        raise NotImplementedError

# Game controls player turns, valid player selections, valid piece moves, valid manipulation of the board
class GameEngine:

    def __init__(self):
        self.players = players
        self.player_turn = 1
        print "New game created"
        pass
    #boolean return that checks if game has ended
    def game_over():
        raise NotImplementedError

    def turn():

class CheckerGameEngine(Game):


class CheckerPiece(Piece):

    def __init__ (self, params):
        '''nothing needs to be implemented'''
        super(self, params).__init__()

        self.params['kind'] = kind
        self.kinged = params['kinged']



class CheckerBoard(Board):
    pass



def main():
    p = {
    'players' = [1,2],
    'size' = (10,10),

    }
    b = CheckerBoard(p)
