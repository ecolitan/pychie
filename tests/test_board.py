#!/usr/bin/python3
# -*- coding: utf8

import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.empty_board = "8/8/8/8/8/8/8/8 w - - 0 1"
        self.start_board = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.test_board1 = "r1b1k2r/ppp2ppp/2nq4/3n2N1/2BP4/P7/1P1B1PPP/R2Q1K1R b kq - 2 12"
        self.test_board2 = "5r1r/2p3b1/p2p1Bk1/1p2P2p/3nPRb1/2NP4/PPP4K/5R2 w - - 2 21"
        self.test_board3 = "rnbqkbnr/pp2pppp/8/2pP4/8/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 3"

        self.Board_empty = Board()
        self.Board_start = Board()
        self.Board_test1 = Board()
        self.Board_test2 = Board()
        self.Board_test3 = Board()
        self.Board_empty.setupPosition(self.empty_board)
        self.Board_start.setupPosition(self.start_board)
        self.Board_test1.setupPosition(self.test_board1)
        self.Board_test2.setupPosition(self.test_board2)
        self.Board_test3.setupPosition(self.test_board3)

    def test_possibleKingMove(self):
        #complete
        k1 = (4,4)
        k2 = (0,0)
        k3 = (4,0)
        k4 = (5,0)
        sq1 = sorted([(3,3), (3,4), (3,5), (4,3), (4,5), (5,3), (5,4), (5,5)])
        sq2 = sorted([(0,1), (1,1), (1,0)])
        sq3 = sorted([])
        sq4 = sorted([(6,0),(4,0),(4,1)])
        
        self.assertEqual(sq1, self.Board_empty.possibleKingMove(k1, 'w'))        
        self.assertEqual(sq2, self.Board_empty.possibleKingMove(k2, 'w'))
        self.assertEqual(sq3, self.Board_start.possibleKingMove(k3, 'w'))
        self.assertEqual(sq4, self.Board_test1.possibleKingMove(k4, 'w'))

    #~ @unittest.skip('')
    def test_possibleCastling(self):
        #complete
        self.assertTrue(self.Board_test1.possibleCastling()['b-king'])
        self.assertFalse(self.Board_test1.possibleCastling()['w-king'])
        self.assertFalse(self.Board_test1.possibleCastling()['b-queen'])
        self.assertFalse(self.Board_test1.possibleCastling()['w-queen'])
        
    def test_possibleQueenMove(self):
        #complete
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
        #complete
        n1 = (0,0)
        n2 = (4,4)
        n3 = (1,0)
        n4 = (6,4)
        n5 = (2,5)
        sq1 = sorted([(1,2),(2,1)])
        sq2 = sorted([(3,6),(2,5),(2,3),(3,2),(5,6),(6,5),(6,3),(5,2)])
        sq3 = sorted([(0,2),(2,2)])
        sq4 = sorted([(7,6),(5,6),(4,5),(4,3),(5,2),(7,2)])
        sq5 = sorted([(0,4),(1,3),(3,3),(4,4),(4,6),(3,7),(1,7)])

        self.assertEqual(sq1, self.Board_empty.possibleKnightMove(n1,'w'))
        self.assertEqual(sq2, self.Board_empty.possibleKnightMove(n2,'w'))
        self.assertEqual(sq3, self.Board_start.possibleKnightMove(n3,'w'))
        self.assertEqual(sq4, self.Board_test1.possibleKnightMove(n4,'w'))
        self.assertEqual(sq5, self.Board_test1.possibleKnightMove(n5,'b'))
    
    def test_possibleRookMove(self):
        #complete
        r1 = (0,0)
        r2 = (4,4)
        r3 = (0,0)
        r4 = (5,0)
        r5 = (5,3)
        r6 = (5,7)
        r7 = (7,7)

        sq1 = sorted([(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                      (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)])
        sq2 = sorted([(3,4),(2,4),(1,4),(0,4),(5,4),(6,4),(7,4),
                      (4,3),(4,2),(4,1),(4,0),(4,5),(4,6),(4,7)])
        sq3 = sorted([])
        sq4 = sorted([(4,0),(3,0),(2,0),(1,0),(0,0),(6,0),(7,0),(5,1),(5,2)])
        sq5 = sorted([(5,4),(5,2),(5,1),(6,3)])
        sq6 = sorted([(5,6),(5,5),(6,7),(4,7),(3,7),(2,7),(1,7),(0,7)])
        sq7 = sorted([(6,7),(7,6),(7,5)])
        
        self.assertEqual(sq1, self.Board_empty.possibleRookMove(r1, 'w'))
        self.assertEqual(sq2, self.Board_empty.possibleRookMove(r2, 'w'))
        self.assertEqual(sq3, self.Board_start.possibleRookMove(r3, 'w'))
        self.assertEqual(sq4, self.Board_test2.possibleRookMove(r4, 'w'))
        self.assertEqual(sq5, self.Board_test2.possibleRookMove(r5, 'w'))
        self.assertEqual(sq6, self.Board_test2.possibleRookMove(r6, 'b'))
        self.assertEqual(sq7, self.Board_test2.possibleRookMove(r7, 'b'))
    
    def test_possiblePawnMove(self):
        #complete
        p1 = (0,1)
        p2 = (4,3)
        p3 = (4,4)
        p4 = (3,2)
        p5 = (3,4)
            
        sq1 = sorted([(0,2),(0,3)])
        sq2 = sorted([(4,4)])
        sq3 = sorted([(3,5),(4,5)])
        sq4 = sorted([])
        sq5 = sorted([(2,5),(3,5)])

        self.assertEqual(sq1, self.Board_empty.possiblePawnMove(p1, 'w'))
        self.assertEqual(sq2, self.Board_empty.possiblePawnMove(p2, 'w'))
        self.assertEqual(sq3, self.Board_test2.possiblePawnMove(p3, 'w'))
        self.assertEqual(sq4, self.Board_test2.possiblePawnMove(p4, 'w'))
        self.assertEqual(sq5, self.Board_test3.possiblePawnMove(p5, 'w'))
    
    def test_pieceColor(self):
        #complete
        p1 = (3,0)
        p2 = (7,7)
        p3 = (0,4)
        
        color1 = 'w'
        color2 = 'b'
        color3 = None

        self.assertEqual(color1, self.Board_test3.pieceColor(p1))
        self.assertEqual(color2, self.Board_test3.pieceColor(p2))
        self.assertEqual(color3, self.Board_test3.pieceColor(p3))
    
    def test_isCheck(self):
        #complete
        self.assertTrue(self.Board_test1.isCheck((4,4),'w'))
        self.assertTrue(self.Board_test1.isCheck((4,4),'b'))
        self.assertTrue(self.Board_test1.isCheck((1,3),'w'))
        self.assertTrue(self.Board_test1.isCheck((1,3),'b'))
        self.assertFalse(self.Board_test1.isCheck((0,7),'w'))
        
if __name__ == '__main__':
    unittest.main()
