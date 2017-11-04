
class Piece:
    def __init__(self, params):
        self.params = params

    def get_piece_rules(piece):
        '''Returns rules for a piece ex.
        [ [1,1], [-1,-1] ]
        '''
        raise NotImplementedError



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
