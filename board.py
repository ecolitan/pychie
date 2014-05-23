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
                    alg_row = int(char)
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
                
    def possibleKingMove(self, square, color):
        """Return list of possible squares a King on a given square can move to."""
        final = []
        possibles = [tuple(sum(x) for x in zip(square, (m,n))) for m in range(-1,2) for n in range(-1,2) if (m,n) != (0,0)]
        for pos in possibles:
            if pos in self.pos_list:
                if self.pieceColor(pos) == color:
                    continue
                else:
                    final.append(pos)
        return sorted(final)
        
    def possibleQueenMove(self, square):
        """Return list of possible squares a Queen on a given square can move to."""
        # combile rook and bishop moves
        bishop = self.possibleBishopMove(square)
        rook = self.possibleRookMove(square)
        allpos = rook + bishop
        return sorted(allpos)
        
    def possibleBishopMove(self, square):
        """Return list of possible squares a Bishop on a given square can move to."""
        final = []
        
        # plus,plus
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos += 1
            ypos += 1
            if (xpos,ypos) in self.pos_list:
                final.append((xpos,ypos))
            else:
                break
        # plus,minus
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos += 1
            ypos -= 1
            if (xpos,ypos) in self.pos_list:
                final.append((xpos,ypos))
            else:
                break
        # minus,plus
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos -= 1
            ypos += 1
            if (xpos,ypos) in self.pos_list:
                final.append((xpos,ypos))
            else:
                break
        # minus,minus
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos -= 1
            ypos -= 1
            if (xpos,ypos) in self.pos_list:
                final.append((xpos,ypos))
            else:
                break
        
        return sorted(final)
        
    def possibleKnightMove(self, square):
        """Return list of possible squares a Knight on a given square can move to."""
        xpos = square[0]
        ypos = square[1]
        final = []
        
        for comb in ((-1,2),(-2,1),(-2,-1),(-1,-2),(1,2),(2,1),(2,-1),(1,-2)):
            if tuple(sum(x) for x in zip(square, comb)) in self.pos_list:
                final.append(tuple(sum(x) for x in zip(square, comb)))
        return sorted(final)
        
    def possibleRookMove(self, square):
        """Return list of possible squares a Rook on a given square can move to."""
        final = []

        # rows
        xpos = square[0]
        ypos = square[1]
        while True:
            xpos += 1
            if (xpos,ypos) in self.pos_list:
                final.append((xpos,ypos))
            else:
                break
        xpos = square[0]
        while True:
            xpos -= 1
            if (xpos,ypos) in self.pos_list:
                final.append((xpos,ypos))
            else:
                break
                
        # cols
        xpos = square[0]
        ypos = square[1]
        while True:
            ypos += 1
            if (xpos,ypos) in self.pos_list:
                final.append((xpos,ypos))
            else:
                break
                xpos = square[0]
        ypos = square[1]
        while True:
            ypos -= 1
            if (xpos,ypos) in self.pos_list:
                final.append((xpos,ypos))
            else:
                break
                xpos = square[0]

        return sorted(final)
        
    def possiblePawnMove(self, square):
        """Return list of possible squares a Pawn on a given square can move to."""
        pass
        if self.pieceColor(square) == 'w':
            sec_rank = ((0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1))
            if square in sec_rank:
                pass
                
        elif self.pieceColor(square) == 'w':
            sec_rank = ((6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7))
            if square in sec_rank:
                pass
        
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

starting_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
A = Board()
A.setupPosition(starting_position)
#~ A.printBoard()
#~ A[(0,0)] = 'R'
#~ A[(1,0)] = 'N'
#~ A[(2,0)] = 'B'
#~ A[(3,0)] = 'Q'
#~ A[(4,0)] = 'K'
#~ A[(5,0)] = 'B'
#~ A[(6,0)] = 'N'
#~ A[(7,0)] = 'R'
#~ A[(0,1)] = 'P'
#~ A[(1,1)] = 'P'
#~ A[(2,1)] = 'P'
#~ A[(3,1)] = 'P'
#~ A[(4,1)] = 'P'
#~ A[(5,1)] = 'P'
#~ A[(6,1)] = 'P'
#~ A[(7,1)] = 'P'
#~ A.printBoard()
