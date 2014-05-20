#!/usr/bin/python3
# -*- coding: utf8

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def test_possibleKingMove(self):
        k1 = (4,4)
        sq1 = sorted([(3,3), (3,4), (3,5), (4,3), (4,5), (5,3), (5,4), (5,5)])
        self.assertEqual(sq1, Board().possibleKingMove(k1))
        k2 = (0,0)
        sq2 = sorted([(0,1), (1,1), (1,0)])
        self.assertEqual(sq2, Board().possibleKingMove(k2))
    
    def test_possibleQueenMove(self):
        q1 = (4,4)
        sq1 = sorted([(0,0),(1,1),(2,2),(3,3),(5,5),(6,6),(7,7),
                      (5,3),(6,2),(7,1),(3,5),(2,6),(1,7),
                      (3,4),(2,4),(1,4),(0,4),(5,4),(6,4),(7,4),
                      (4,3),(4,2),(4,1),(4,0),(4,5),(4,6),(4,7)])
        self.assertEqual(sq1, Board().possibleQueenMove(q1))
        
    def test_possibleBishopMove(self):
        b1 = (0,0)
        sq1 = sorted([(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)])
        self.assertEqual(sq1, Board().possibleBishopMove(b1))
        b2 = (4,4)
        sq2 = sorted([(0,0),(1,1),(2,2),(3,3),(5,5),(6,6),(7,7),
                      (5,3),(6,2),(7,1),(3,5),(2,6),(1,7)])
        self.assertEqual(sq2, Board().possibleBishopMove(b2))
        
    def test_possibleKnightMove(self):
        pass
        n1 = (0,0)
        sq1 = sorted([(1,2),(2,1)])
        self.assertEqual(sq1, Board().possibleKnightMove(n1))
        n2 = (4,4)
        sq2 = sorted([(3,6),(2,5),(2,3),(3,2),(5,6),(6,5),(6,3),(5,2)])
        self.assertEqual(sq2, Board().possibleKnightMove(n2))
    
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
        pass

if __name__ == '__main__':
    unittest.main()
