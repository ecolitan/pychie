#!/usr/bin/python3
# -*- coding: utf8

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.empty_board = "8/8/8/8/8/8/8/8 w - - 0 1"
        self.start_board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    def test_possibleKingMove(self):
        k1 = (4,4)
        k2 = (0,0)
        k3 = (4,0)
        sq1 = sorted([(3,3), (3,4), (3,5), (4,3), (4,5), (5,3), (5,4), (5,5)])
        sq2 = sorted([(0,1), (1,1), (1,0)])
        sq3 = sorted([])
        
        Board1 = Board()
        Board2 = Board()
        Board3 = Board()
        Board1.setupPosition(self.empty_board)
        Board2.setupPosition(self.empty_board)
        Board3.setupPosition(self.start_board)
                
        #~ self.assertEqual(sq1, Board1.possibleKingMove(k1, 'w'))        
        #~ self.assertEqual(sq2, Board2.possibleKingMove(k2, 'w'))
        self.assertEqual(sq3, Board3.possibleKingMove(k3, 'w'))
    
    @unittest.skip('')
    def test_possibleQueenMove(self):
        q1 = (4,4)
        sq1 = sorted([(0,0),(1,1),(2,2),(3,3),(5,5),(6,6),(7,7),
                      (5,3),(6,2),(7,1),(3,5),(2,6),(1,7),
                      (3,4),(2,4),(1,4),(0,4),(5,4),(6,4),(7,4),
                      (4,3),(4,2),(4,1),(4,0),(4,5),(4,6),(4,7)])
        self.assertEqual(sq1, Board().possibleQueenMove(q1))
    
    @unittest.skip('')    
    def test_possibleBishopMove(self):
        b1 = (0,0)
        sq1 = sorted([(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
        self.assertEqual(sq1, Board().possibleBishopMove(b1))
        b2 = (4,4)
        sq2 = sorted([(0,0),(1,1),(2,2),(3,3),(5,5),(6,6),(7,7),
                      (5,3),(6,2),(7,1),(3,5),(2,6),(1,7)])
        self.assertEqual(sq2, Board().possibleBishopMove(b2))
        
    @unittest.skip('')
    def test_possibleKnightMove(self):
        pass
        n1 = (0,0)
        sq1 = sorted([(1,2),(2,1)])
        self.assertEqual(sq1, Board().possibleKnightMove(n1))
        n2 = (4,4)
        sq2 = sorted([(3,6),(2,5),(2,3),(3,2),(5,6),(6,5),(6,3),(5,2)])
        self.assertEqual(sq2, Board().possibleKnightMove(n2))
    
    @unittest.skip('')
    def test_possibleRookMove(self):
        pass
        r1 = (0,0)
        sq1 = sorted([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                      (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)])
        self.assertEqual(sq1, Board().possibleRookMove(r1))
        r2 = (4,4)
        sq2 = sorted([(3,4),(2,4),(1,4),(0,4),(5,4),(6,4),(7,4),
                      (4,3),(4,2),(4,1),(4,0),(4,5),(4,6),(4,7)])
    
    @unittest.skip('')
    def test_possiblePawnMove(self):
        p1 = (0,2)
        sq1 = sorted([(0,3),(0,4)])
        p2 = (4,3)
        sq2 = (4,4)
        self.assertEqual(sq1, Board().possiblePawnMove(p1))
        self.assertEqual(sq2, Board().possiblePawnMove(p2))
    
    @unittest.skip('')
    def test_pieceColor(self):
        pass

if __name__ == '__main__':
    unittest.main()
