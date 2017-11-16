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
        self.player_turn = 1
        self.players = 2 #used to switch players each turn
        self.board.grid[(3,3)]= CheckerPiece(2,(3,3)) #testing piece
        pass

    def run(self):
        while not self.game_over():
            self.draw_board()
            print "Player", self.player_turn, "Turn:"

            #get input
            while True:
                try:
                    selection = input("Select a piece x,y:   ")
                except ValueError:
                    print "Input error, try again"

                #check input

                #check if location is empty, then if piece is the players, then determines piecs moves, then if piece has any moves, continue

                if isinstance(self.board.grid.get(selection),Piece):
                    if self.board.grid[selection].player is self.player_turn:
                        self.movement_logic(self.board.grid[selection])
                        if len(self.board.grid[(selection)].moves) is 0:
                            continue
                        print self.board.grid[selection].moves
                        break
                    else:
                        print "Not your piece, try again"
                else:
                    print "No piece selected, try again"

            #get desired move

            move = input( "Select move: ")
            while move not in self.board.grid.get(selection).moves:
                move = input("Invalid Move, Select move: ")

            #make move, remove piece if jump made

            self.board.grid[(move)] = CheckerPiece(self.player_turn, move)
            self.board.grid[(selection)] = None

            #if distance moved is 2 remove jumped piece
            if (move[0] - selection[0]) % 2 is 0:
                print "dist = 2"
                jx = (move[0] - selection[0]) / 2
                jy = (move[1] - selection[1]) / 2
                jloc = ((move[0] - jx), (move[1] - jy))
                self.board.grid[(jloc)] = None




            #switch turns
            self.player_turn = 1 if self.player_turn is self.players else 2

    def movement_logic(self,piece):
        #set vectors
        vectors = [[]]
        if piece.player is 1:
            vectors = [ [-1,1], [1,1] ]
            if piece.kinged:
                vectors.append( [-1,-1] )
                vectors.append( [-1,1] )
        else:
            vectors = [ [-1,-1], [1,-1] ]
            if piece.kinged:
                vectors.append( [1,-1] )
                vectors.append( [1,1] )

        #propagate through board in vector directions
        #clarity
        origin = piece.location
        x0 = origin[0]
        y0 = origin[1]
        grid_size = self.board.board_size

        #find non attack moves

        for x,y in vectors:
            #space is on the board
            if x0+x in range(0,grid_size[0]) and y0+y in range(0,grid_size[1]):
                #space is unoccupied
                if not isinstance(self.board.grid[(x0+x,y0+y)], Piece):
                    piece.moves.append((x0+x,y0+y))
                else:
                    continue

        #find attack moves for non kinged

        #tier one
        for x,y in vectors:
            xx = x0+x
            yy = y0+y
            #while move is in bounds
            space_needed = False
            while xx in range(0, grid_size[0]) and yy in range(0, grid_size[1]):
                #if space has a piece
            #for ii in range(1,4):
                print "in loop"
                if isinstance(self.board.grid[(xx,yy)], Piece):
                    #if the piece is an opponents
                    print "checking: ", xx,yy, "since its a piece"
                    if self.board.grid[(xx,yy)].player is not piece.player:
                        #check space behind if empty
                        print "opponent piece confirmed"
                        xx += x
                        yy += y
                        print "coordinates moved to", (xx,yy), "check if its free"
                        space_needed = True
                        continue
                    #friendly piece
                    else:
                        break
                #empty space and checking for an empty space
                elif space_needed:
                    #add move to attack list, then go back through attack list for more jumps
                    print "Space free, adding", (xx,yy)
                    piece.moves.append((xx,yy))
                    break
                else:
                    break


    def game_over(self):
        pass

    def draw_board(self, select = None):

        #output 0 1 2 3 4 5 6 7
        for i in range(0,self.board.board_size[1]):
            sys.stdout.write(" " + str(i) + " ")

        print ""
        #output grid
        for y in range(self.board.board_size[1]-1, -1, -1):
            for x in range(0, self.board.board_size[0]):
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
    def __init__ (self, player,location):
        self.player = player
        self.kinged = False
        self.location = location
        self.moves = []



class CheckerBoard(Board):

    def __init__(self, board_size):

        self.board_size = board_size
        self.grid = {}

        for y in range(0,board_size[1]):
            for x in range(0,board_size[0]):
                #checker board only plays on both even, or both odd coordinate spaces ex [0,0] or [1,5]
                if (y % 2 is 0 and x % 2 is 0) or (y % 2 is not 0 and x % 2 is not 0):
                    #first 3 rows is player 1, last 3 is player 2, middle is empty
                    if y < 3:
                        self.grid[(x,y)] = CheckerPiece(1,(x,y))
                    elif y > 4:
                        self.grid[(x,y)] = CheckerPiece(2,(x,y))
                    else:
                        self.grid[(x,y)] = None

    def create_piece(params):
        raise NotImplementedError

    def update_loc(params):
        raise NotImplementedError




def main():
    print "Welcome"
    new_game = CheckerGameEngine()

    new_game.run()

    pass

main()
