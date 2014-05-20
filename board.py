#!/usr/bin/python3
# -*- coding: utf8 -*-

class Board(dict):
    def __init__(self):
        """initialise empty board dict"""
        dict.__init__(self, {
            (0,0): None, (1,0): None, (2,0): None, (3,0): None, (4,0): None, (5,0): None, (6,0): None, (7,0): None,
            (0,1): None, (1,1): None, (2,1): None, (3,1): None, (4,1): None, (5,1): None, (6,1): None, (7,1): None,
            (0,2): None, (1,2): None, (2,2): None, (3,2): None, (4,2): None, (5,2): None, (6,2): None, (7,2): None,
            (0,3): None, (1,3): None, (2,3): None, (3,3): None, (4,3): None, (5,3): None, (6,3): None, (7,3): None,
            (0,4): None, (1,4): None, (2,4): None, (3,4): None, (4,4): None, (5,4): None, (6,4): None, (7,4): None,
            (0,5): None, (1,5): None, (2,5): None, (3,5): None, (4,5): None, (5,5): None, (6,5): None, (7,5): None,
            (0,6): None, (1,6): None, (2,6): None, (3,6): None, (4,6): None, (5,6): None, (6,6): None, (7,6): None,
            (0,7): None, (1,7): None, (2,7): None, (3,7): None, (4,7): None, (5,7): None, (6,7): None, (7,7): None })
        self.pos_list = sorted(self.keys())
    
    def setupPosition(self, position):
        """Set the position from a position string
        raise if unsuccessful or return None
        """
        index = 0
        for char in position:
            if char in list('rnbqkpRNBQKP'):
                self[self.pos_list[index]] = char
                index += 1
            else:
                index += int(char)
        return None
        
    def possibleKingMove(self, square):
        """Return list of possible squares a King on a given square can move to."""
        final = []
        possibles = [tuple(sum(x) for x in zip(square, (m,n))) for m in range(-1,2) for n in range(-1,2) if (m,n) != (0,0)]
        for pos in possibles:
            if pos in self.pos_list:
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
    
    def printBoard(self):
        """print a pretty board"""
        col = 0
        for pos in [(i,j) for i in range(0,8) for j in range(0,8)]:
            if self[pos] is None:
                print(" . ", end="")
            else:
                print(" " + self[pos] + " ", end="")
            col += 1
            if col == 8:
                col = 0
                print()
                
starting_position = """rnbqkbnrpppppppp88p78PPPPPPPPRNBQKBNR"""
A = Board()
A.setupPosition(starting_position)
#~ A.printBoard()
