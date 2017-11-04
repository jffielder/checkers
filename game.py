#checkers
import sys
from CheckerPiece import Piece

print "..."

class Board:

    def __init__(self):
        #player 1 pieces
        self.pos = {}
        self.current_player = 1
        for y in range(0,4): #1st 4 rows are player 1
            for x in range(0,10):
                #every other pos
                if y % 2 is 0:
                    if x % 2 is 0:
                        self.pos[(x,y)] = Piece(1)

                #odd row has piece on odd position
                else:
                    if x % 2 is not 0:
                        self.pos[(x,y)] = Piece(1)
        #player 2 pieces
        for y in range(6,10):
            for x in range(0,10):
                #even row
                if y % 2 is 0:
                    if x % 2 is 0:
                        self.pos[(x,y)] = Piece(2)
                #odd row
                else:
                    if x % 2 is not 0:
                        self.pos[(x,y)] = Piece(2)
    def in_bounds(self, coordinate):
        return ( coordinate[0] in range(0,10) and coordinate[1] in range(0,10) )

        #returns list of moves
    def analyze_loc(self, start_pos):
        #start_pos (x,y) form
        next_pos = [ ]
        if self.pos.get(start_pos, Piece(0)).kinged is True:
            directions = [ [-1,1], [1,1], [-1,-1], [1,-1] ]
        else:
            directions = [ [-1,1], [1,1] ]

        #for each in directions check if movment in that direction is out of bounds
        for x,y in directions:
            new_pos = (x + start_pos[0] , y + start_pos[1] )

            if self.in_bounds(new_pos):
                #if a position is occupied by friendly piece, not a valid move
                player = self.get_player(new_pos)
                if player is 0:
                    next_pos.append(new_pos)
                elif player is 1:
                    break
                elif player is 2:
                    new_pos = [x + start_pos[0] , y + start_pos[1] ]
                    if self.in_bounds(new_pos) and self.get_player(new_pos) is 0:
                        next_pos.append(new_pos)
        return next_pos

        #returns list of new moves to merge with move_list
    def get_jump_moves(self, move_list):
        #go through each coordinate and see if a jump can be made, depth first algo
        for move in move_list:
            pass




    #returns params with key 'player' and value of 0 if space is empty
    def get_player(self, coordinate):
        if isinstance(self.pos.get(coordinate), Piece):
            if self.pos[coordinate].player is 1:
                return 1
            elif self.pos[coordinate].player is 2:
                return 2
        else:
            return 0


    def move_piece(self, start, end):
        self.pos[end] = self.pos[start]
        self.pos[start] = None

class Game:
    #creates new Board
    def intro(self):
        print "Welcome"

    def __init__ (self):
        self.board = Board()

        self.current_player = 1

        #intro()

    def draw(self):
        print "Player 1 = o, Player 2 = x"
        outstring = ""
        for i in range(0,10,1):
            outstring += " " + str(i) + " "
        print outstring

        for y in range(9, -1, -1):
            #print str(y+2)
            print ""
            for x in range(10):
                if isinstance (self.board.pos.get( (x,y) ), Piece):
                    if self.board.pos[(x,y)].player is 1:
                        sys.stdout.write( " o " )
                    else:
                        sys.stdout.write( " x " )
                else:
                    sys.stdout.write( " - " )

            sys.stdout.write(str(y))
        print ""

    def over(self):
        pass


def main():
    game = Game()
    game.intro()

    print "checkers"

    while not game.over():
        game.draw()
        print "player 1 choose piece"
        start_loc = tuple(map(int,raw_input().split(',')))
        if game.board.pos.get(start_loc, 0) is not 0:
            if game.board.pos[start_loc].player is game.current_player:
        move_l = game.board.analyze_loc(start_loc)
        print move_l

        end_move = tuple(map(int,raw_input().split(',')))

        if end_move in move_l:
            game.board.move_piece(start_loc, end_move)
        else:
            print "invalid move"




main()
