#!/usr/bin/python3
# -*- coding: utf8

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    @unittest.skip('')
    def test_setupPosition(self):
        pass
        
    def test_possibleKingMove(self):
        king1 = (4,4)
        squares1 = sorted([(3,3), (3,4), (3,5), (4,3), (4,5), (5,3), (5,4), (5,5)])
        self.assertEqual(squares1, Board().possibleKingMove(king1))
        king2 = (0,0)
        squares2 = sorted([(0,1), (1,1), (1,0)])
        self.assertEqual(squares2, Board().possibleKingMove(king2))
    
    @unittest.skip('')    
    def test_possibleQueenMove(self):
        pass
        
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
