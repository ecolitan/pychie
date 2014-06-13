#!/usr/bin/python3
# -*- coding: utf8 -*-

class Board(dict):
    def __init__(self):
        """initialise empty board dict"""
        dict.__init__(self, {
            (0,7): None, (1,7): None, (2,7): None, (3,7): None, (4,7): None, (5,7): None, (6,7): None, (7,7): None,
            (0,6): None, (1,6): None, (2,6): None, (3,6): None, (4,6): None, (5,6): None, (6,6): None, (7,6): None,
            (0,5): None, (1,5): None, (2,5): None, (3,5): None, (4,5): None, (5,5): None, (6,5): None, (7,5): None,
            (0,4): None, (1,4): None, (2,4): None, (3,4): None, (4,4): None, (5,4): None, (6,4): None, (7,4): None,            
            (0,3): None, (1,3): None, (2,3): None, (3,3): None, (4,3): None, (5,3): None, (6,3): None, (7,3): None,
            (0,2): None, (1,2): None, (2,2): None, (3,2): None, (4,2): None, (5,2): None, (6,2): None, (7,2): None,
            (0,1): None, (1,1): None, (2,1): None, (3,1): None, (4,1): None, (5,1): None, (6,1): None, (7,1): None,
            (0,0): None, (1,0): None, (2,0): None, (3,0): None, (4,0): None, (5,0): None, (6,0): None, (7,0): None })
            
        self.pos_list = sorted(self.keys())
        self.to_move = 'w'
        self.castle = {'w-king': False, 'w-queen': False, 'b-king': False, 'b-queen': False}
        self.ep = None
        self.halfmove_count = 0
        self.fullmove_count = 1
        
    def setupPosition(self, position):
        """Set the position from a FEN position string
        raise if unsuccessful or return None
        """
        count = 0
        x_index = 0
        y_index = 7
        field = 0
        for char in position:
            if field == 0:
                #Position
                if char in list('rnbqkpRNBQKP'):
                    self[x_index,y_index] = char
                    x_index += 1
                    count += 1
                    if count % 8 == 0:
                        y_index -= 1
                        x_index = 0
                elif char in list('12345678'):
                    x_index += int(char)
                    count += int(char)
                    if count % 8 == 0:
                        y_index -= 1
                        x_index = 0
                elif char == '/':
                    continue
                elif char == ' ':
                    field += 1
                    continue
                else:
                    raise ValueError
            elif field == 1:
                #To-Move
                if char in list('wW'):
                    self.to_move = 'w'
                elif char in list('bB'):
                    self.to_move = 'b'
                elif char == ' ':
                    field += 1
                else:
                    raise ValueError
            elif field == 2:
                #Castling Rights
                if char == 'K':
                    self.castle['w-king'] = True
                elif char == 'Q':
                    self.castle['w-queen'] = True
                elif char == 'k':
                    self.castle['b-king'] = True
                elif char == 'q':
                    self.castle['b-queen'] = True
                elif char == '-':
                    continue
                elif char == ' ':
                    field += 1
                else:
                    raise ValueError
            elif field == 3:
                #EnPassant Square
                if char == '-':
                    self.ep = None
                elif char in list('abcdefgHABCDEFGH'):
                    alg_col = char
                    alg_col = ['a','b','c','d','e','f','g','h'].index(alg_col.lower())
                elif char in list('12345678'):
                    alg_row = int(char)-1
                    self.ep = (alg_col,alg_row)
                elif char == ' ':
                    field += 1
                else:
                    raise ValueError
            elif field == 4:
                #halfmove clock
                hm_l = []
                if char in list('0123456789'):
                    hm_l.append(char)
                elif char == ' ':
                    if hm_l:
                        self.halfmove_count = int(''.join(map(str,hm_l)))
                    else:
                        self.halfmove_count = 0
                    field += 1
                else:
                    raise ValueError
            elif field == 5:
                #Fullmove Counter
                fm_l = []
                if char in list('0123456789'):
                    fm_l.append(char)
                elif char == ' ':
                    if fm_l:
                        self.fullmove_count = int(''.join(map(str,fm_l)))
                    else:
                        self.fullmove_count = 1
                    field += 1
                else:
                    raise ValueError
            elif field == 6:
                return None
            else:
                raise Exception
                
    def possibleKingMove(self, square, color=None):
        """Return list of possible squares a King on a given square can move to."""
        if color is None:
            color = self.to_move
        final = []
        possibles = [tuple(sum(x) for x in zip(square, (m,n))) for m in range(-1,2) for n in range(-1,2) if (m,n) != (0,0)]
        for pos in possibles:
            if pos in self.pos_list:
                if self.pieceColor(pos) == color:
                    continue
                else:
                    final.append(pos)
        return sorted(final)
        
    def possibleCastling(self):
        """Return a dict if castling is possible right now
        {'w-king': T|F, 'w-queen': T|F, 'b-king': T|F, 'b-queen': T|F}
        """
        final = {'w-king': False, 'w-queen': False, 'b-king': False, 'b-queen': False}
        if ((self.castle['w-king']) and
            (not self.isOccupied((5,0))) and
            (not self.isOccupied((6,0))) and
            (not self.isCheck((5,0), 'w')) and
            (not self.isCheck((6,0), 'w'))):
            final['w-king'] = True
        elif ((self.castle['w-queen']) and
            (not self.isOccupied((3,0))) and
            (not self.isOccupied((2,0))) and
            (not self.isOccupied((1,0))) and
            (not self.isCheck((3,0), 'w')) and
            (not self.isCheck((2,0), 'w'))):
            final['w-queen'] = True
        elif ((self.castle['b-king']) and
            (not self.isOccupied((5,7))) and
            (not self.isOccupied((6,7))) and
            (not self.isCheck((5,7), 'b')) and
            (not self.isCheck((6,7), 'b'))):
            final['b-king'] = True
        elif ((self.castle['b-queen']) and
            (not self.isOccupied((3,7))) and
            (not self.isOccupied((2,7))) and
            (not self.isOccupied((1,7))) and
            (not self.isCheck((7,7), 'b')) and
            (not self.isCheck((2,7), 'b'))):
            final['b-queen'] = True
        return final
        
    def possibleQueenMove(self, square, color=None):
        """Return list of possible squares a Queen on a given square can move to."""
        if color is None:
            color = self.to_move
        # combile rook and bishop moves
        bishop = self.possibleBishopMove(square,color)
        rook = self.possibleRookMove(square,color)
        allpos = rook + bishop
        return sorted(allpos)
        
    def possibleBishopMove(self, square, color=None):
        """Return list of possible squares a Bishop on a given square can move to."""
        if color is None:
            color = self.to_move
            
        final = []
        
        # right,up
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos += 1
            ypos += 1
            if (xpos,ypos) in self.pos_list:
                if self.pieceColor((xpos,ypos)):
                    if self.pieceColor((xpos,ypos)) == color:
                        break
                    final.append((xpos,ypos))
                    break
                else:
                    final.append((xpos,ypos))
            else:
                break
        # right,down
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos += 1
            ypos -= 1
            if (xpos,ypos) in self.pos_list:
                if self.pieceColor((xpos,ypos)):
                    if self.pieceColor((xpos,ypos)) == color:
                        break
                    final.append((xpos,ypos))
                    break
                else:
                    final.append((xpos,ypos))
            else:
                break
        # left,up
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos -= 1
            ypos += 1
            if (xpos,ypos) in self.pos_list:
                if self.pieceColor((xpos,ypos)):
                    if self.pieceColor((xpos,ypos)) == color:
                        break
                    final.append((xpos,ypos))
                    break
                else:
                    final.append((xpos,ypos))
            else:
                break
        # left,down
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos -= 1
            ypos -= 1
            if (xpos,ypos) in self.pos_list:
                if self.pieceColor((xpos,ypos)):
                    if self.pieceColor((xpos,ypos)) == color:
                        break
                    final.append((xpos,ypos))
                    break
                else:
                    final.append((xpos,ypos))
            else:
                break
        
        return sorted(final)
        
    def possibleKnightMove(self, square, color=None):
        """Return list of possible squares a Knight on a given square can move to."""
        if color is None:
            color = self.to_move
        xpos = square[0]
        ypos = square[1]
        final = []
        
        for comb in ((-1,2),(-2,1),(-2,-1),(-1,-2),(1,2),(2,1),(2,-1),(1,-2)):
            if tuple(sum(x) for x in zip(square, comb)) in self.pos_list:
                final.append(tuple(sum(x) for x in zip(square, comb)))
                final = [pos for pos in final if self.pieceColor(pos) != color]
        return sorted(final)
        
    def possibleRookMove(self, square, color=None):
        """Return list of possible squares a Rook on a given square can move to."""
        if color is None:
            color = self.to_move
        final = []

        # rows
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos += 1
            if (xpos,ypos) in self.pos_list:
                if self.pieceColor((xpos,ypos)):
                    if self.pieceColor((xpos,ypos)) == color:
                        break
                    final.append((xpos,ypos))
                    break
                else:
                    final.append((xpos,ypos))
            else:
                break
        xpos = square[0]
        while True:
            xpos -= 1
            if (xpos,ypos) in self.pos_list:
                if self.pieceColor((xpos,ypos)):
                    if self.pieceColor((xpos,ypos)) == color:
                        break
                    final.append((xpos,ypos))
                    break
                else:
                    final.append((xpos,ypos))
            else:
                break
        # cols
        xpos = square[0]
        ypos = square[1]
        while True:
            ypos += 1
            if (xpos,ypos) in self.pos_list:
                if self.pieceColor((xpos,ypos)):
                    if self.pieceColor((xpos,ypos)) == color:
                        break
                    final.append((xpos,ypos))
                    break
                else:
                    final.append((xpos,ypos))
            else:
                break
        xpos = square[0]
        ypos = square[1]
        while True:
            ypos -= 1
            if (xpos,ypos) in self.pos_list:
                if self.pieceColor((xpos,ypos)):
                    if self.pieceColor((xpos,ypos)) == color:
                        break
                    final.append((xpos,ypos))
                    break
                else:
                    final.append((xpos,ypos))
            else:
                break
                xpos = square[0]

        return sorted(final)
        
    def possiblePawnMove(self, square, color=None):
        """Return list of possible squares a Pawn on a given square can move to."""
        if color is None:
            color = self.to_move
        xpos = square[0]
        ypos = square[1]
        final = []
        #white pawns
        if color == 'w':
            second_rank = ((0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1))
            if square in second_rank:
                #step forwards
                for step in [1,2]:
                    if not self.isOccupied((xpos,ypos+step)):
                        final.append((xpos,ypos+step))
                    else:
                        break
            else:
                if not self.isOccupied((xpos,ypos+1)):
                    final.append((xpos,ypos+1))
            #captures
            squares = [(xpos-1,ypos+1),(xpos+1,ypos+1)]
            for pos in squares:
                if pos in self.pos_list:
                    if self.pieceColor(pos) != color and self.pieceColor(pos):
                        final.append(pos)
            #ep
            if self.ep in [(xpos-1,ypos+1),(xpos+1,ypos+1)]:
                final.append(self.ep)
            
                
        elif color == 'b':
            second_rank = ((6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7))
            if square in second_rank:
                #step forwards
                for step in [-1,-2]:
                    if not self.isOccupied((xpos,ypos+step)):
                        final.append((xpos,ypos+step))
                    else:
                        break
            else:
                if not self.isOccupied((xpos,ypos-1)):
                    final.append((xpos,ypos-1))
            #captures
            squares = [(xpos-1,ypos-1),(xpos+1,ypos-1)]
            for pos in squares:
                if pos in self.pos_list:
                    if self.pieceColor(pos) != color:
                        final.append(pos)
            #ep
            if self.ep in [(xpos-1,ypos-1),(xpos+1,ypos-1)]:
                final.append(self.ep)
        return sorted(final)
        
    def possiblePawnAttacking(self, square, color=None):
        """Return a list of the squares a Pawn in a given square attacks"""
        if color is None:
            color = self.to_move
        xpos = square[0]
        ypos = square[1]
        final = []
        if color == 'w':
            squares = [(xpos-1,ypos+1),(xpos+1,ypos+1)]
        elif color == 'b':
            squares = [(xpos-1,ypos-1),(xpos+1,ypos-1)]
            
        for pos in squares:
            if pos in self.pos_list:
                final.append(pos)

        return sorted(final)
        
    def printBoard(self):
        """print a pretty board"""
        
        for y in [7,6,5,4,3,2,1,0]:
            for x in [0,1,2,3,4,5,6,7]:
                if self[x,y] is None:
                    print(" . ", end="")
                else:
                    print(" " + self[x,y] + " ", end="")
            print()
    
    def pieceColor(self, square):
        """Return color of piece on a square or None"""
        if self[square] in list('rnbqkp'):
            return 'b'
        elif self[square] in list('rnbqkp'.upper()):
            return 'w'
        else:
            return None
            
    def isOccupied(self, square):
        """Return True or False if a square is occupied"""
        if self[square]:
            return True
        else:
            return False
            
    def attackedSquares(self, square):
        """Return list of attacked squares for whatever piece is on square or None
        Pieces do not attack their own squares
        """
        piece = self[square]
        color = self.pieceColor(square)
        
        if piece is None:
            return None
        elif piece.lower() == 'r':
            return self.possibleRookMove(square,color)
        elif piece.lower() == 'n':
            return self.possibleKnightMove(square,color)
        elif piece.lower() == 'b':
            return self.possibleBishopMove(square,color)
        elif piece.lower() == 'q':
            return self.possibleQueenMove(square,color)
        elif piece.lower() == 'k':
            return self.possibleKingMove(square,color)
        elif piece.lower() == 'p':
            return self.possiblePawnAttacking(square,color)
        else:
            raise Exception
    
    def isCheck(self, square, color):
        """Return true or false if a king of given color would be in check.
        Relies on all possiblePieceMove() methods except king castling.
        """
        for pos in self.pos_list:
            if ((color == 'w' and self.pieceColor(pos) == 'b') or
               (color == 'b' and self.pieceColor(pos) == 'w')):
                if square in self.attackedSquares(pos):
                    return True
        return False
        
if __name__ == '__main__':
    starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    A = Board()
    A.setupPosition(starting_position)
    A.printBoard()
