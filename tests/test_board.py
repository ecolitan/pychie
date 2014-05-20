#!/usr/bin/python3
# -*- coding: utf8

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    @unittest.skip('')
    def test_setupPosition(self):
        pass
        
    def test_possibleKingMove(self):
        k1 = (4,4)
        sq1 = sorted([(3,3), (3,4), (3,5), (4,3), (4,5), (5,3), (5,4), (5,5)])
        self.assertEqual(sq1, Board().possibleKingMove(k1))
        k2 = (0,0)
        sq2 = sorted([(0,1), (1,1), (1,0)])
        self.assertEqual(sq2, Board().possibleKingMove(k2))
    
    @unittest.skip('')
    def test_possibleQueenMove(self):
        q1 = (4,4)
        sq1 = sorted([(0,4),(1,4),(2,4),(3,4),(5,4),(6,4),(7,4),(4,0),(4,1),
            (4,2),(4,3),(4,5),(4,6),(4,7),(3,3),(2,2),(1,1),(0,0),(5,5),
            (6,6),(7,7),(5,3),(6,3),(7,1),(3,5),(2,6),(1,7)])
        self.assertEqual(sq1, Board().possibleKingMove(q1))
        
    @unittest.skip('')
    def test_possibleBishopMove(self):
        pass
        
    @unittest.skip('')
    def test_possibleKnightMove(self):
        pass
    
    @unittest.skip('')
    def test_possibleRookMove(self):
        pass
    
    @unittest.skip('')
    def test_possiblePawnMove(self):
        pass

if __name__ == '__main__':
    unittest.main()
