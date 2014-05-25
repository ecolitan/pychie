#!/usr/bin/python3
# -*- coding: utf8

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.empty_board = "8/8/8/8/8/8/8/8 w - - 0 1"
        self.start_board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.test_board1 = "r1b1k2r/ppp2ppp/2nq4/3n2N1/2BP4/P7/1P1B1PPP/R2Q1K1R b kq - 2 12"

        self.Board_empty = Board()
        self.Board_start = Board()
        self.Board_test1 = Board()
        self.Board_empty.setupPosition(self.empty_board)
        self.Board_start.setupPosition(self.start_board)
        self.Board_test1.setupPosition(self.test_board1)

    def test_possibleKingMove(self):
        k1 = (4,4)
        k2 = (0,0)
        k3 = (4,0)
        sq1 = sorted([(3,3), (3,4), (3,5), (4,3), (4,5), (5,3), (5,4), (5,5)])
        sq2 = sorted([(0,1), (1,1), (1,0)])
        sq3 = sorted([])
        
        self.assertEqual(sq1, self.Board_empty.possibleKingMove(k1, 'w'))        
        self.assertEqual(sq2, self.Board_empty.possibleKingMove(k2, 'w'))
        self.assertEqual(sq3, self.Board_start.possibleKingMove(k3, 'w'))
    
    def test_possibleQueenMove(self):
        q1 = (4,4)
        q2 = (3,0)
        sq1 = sorted([(0,0),(1,1),(2,2),(3,3),(5,5),(6,6),(7,7),
                      (5,3),(6,2),(7,1),(3,5),(2,6),(1,7),
                      (3,4),(2,4),(1,4),(0,4),(5,4),(6,4),(7,4),
                      (4,3),(4,2),(4,1),(4,0),(4,5),(4,6),(4,7)])
        sq2 = sorted([])
        
        self.assertEqual(sq1, self.Board_empty.possibleQueenMove(q1,'w'))
        self.assertEqual(sq2, self.Board_start.possibleQueenMove(q2,'w'))
    
    def test_possibleBishopMove(self):
        #complete
        b1 = (0,0)
        b2 = (4,4)
        b3 = (2,0)
        b4 = (2,3)
        b5 = (3,1)
        b6 = (2,7)
        
        sq1 = sorted([(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
        sq2 = sorted([(0,0),(1,1),(2,2),(3,3),(5,5),(6,6),(7,7),
                      (5,3),(6,2),(7,1),(3,5),(2,6),(1,7)])
        sq3 = sorted([])
        sq4 = sorted([(1,4),(0,5),(1,2),(0,1),(3,4),(3,2),(4,1)])
        sq5 = sorted([(2,0),(2,2),(1,3),(0,4),(4,0),(4,2),(5,3)])
        sq6 = sorted([(3,6),(4,5),(5,4),(6,3),(7,2)])
        
        self.assertEqual(sq1, self.Board_empty.possibleBishopMove(b1,'w'))
        self.assertEqual(sq2, self.Board_empty.possibleBishopMove(b2,'w'))
        self.assertEqual(sq3, self.Board_start.possibleBishopMove(b3,'w'))
        self.assertEqual(sq4, self.Board_test1.possibleBishopMove(b4,'w'))
        self.assertEqual(sq5, self.Board_test1.possibleBishopMove(b5,'w'))
        self.assertEqual(sq6, self.Board_test1.possibleBishopMove(b6,'b'))
        
    def test_possibleKnightMove(self):
        n1 = (0,0)
        n2 = (4,4)
        n3 = (1,0)
        sq1 = sorted([(1,2),(2,1)])
        sq2 = sorted([(3,6),(2,5),(2,3),(3,2),(5,6),(6,5),(6,3),(5,2)])
        sq3 = sorted([(0,2),(2,2)])

        self.assertEqual(sq1, self.Board_empty.possibleKnightMove(n1,'w'))
        self.assertEqual(sq2, self.Board_empty.possibleKnightMove(n2,'w'))
        self.assertEqual(sq3, self.Board_start.possibleKnightMove(n3,'w'))
    
    def test_possibleRookMove(self):
        r1 = (0,0)
        r2 = (4,4)
        r3 = (0,0)

        sq1 = sorted([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                      (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)])
        sq2 = sorted([(3,4),(2,4),(1,4),(0,4),(5,4),(6,4),(7,4),
                      (4,3),(4,2),(4,1),(4,0),(4,5),(4,6),(4,7)])
        sq3 = sorted([])
        
        self.assertEqual(sq1, self.Board_empty.possibleRookMove(r1, 'w'))
        self.assertEqual(sq2, self.Board_empty.possibleRookMove(r2, 'w'))
        self.assertEqual(sq3, self.Board_start.possibleRookMove(r3, 'w'))
    
    def test_possiblePawnMove(self):
        p1 = (0,1)
        p2 = (4,3)
            
        sq1 = sorted([(0,2),(0,3)])
        sq2 = sorted([(4,4)])

        self.assertEqual(sq1, self.Board_empty.possiblePawnMove(p1, 'w'))
        self.assertEqual(sq2, self.Board_empty.possiblePawnMove(p2, 'w'))
        #~ self.assertEqual(sq3, self.Board_start.possiblePawnMove(p3))
        #~ self.assertEqual(sq4, self.Board_start.possiblePawnMove(p4))
    
    @unittest.skip('')
    def test_pieceColor(self):
        pass

if __name__ == '__main__':
    unittest.main()
