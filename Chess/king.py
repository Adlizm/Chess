from piece import Piece
from rook import Rook
import pygame

BLACK = 1
ROOK = 3


class King(Piece):
	def __init__(self,row,col,color):
		Piece.__init__(self,row,col,color)
		if color == BLACK:
			self.img = pygame.image.load ('images/kingB.png')
		else:
			self.img = pygame.image.load ('images/kingW.png')

	def movimentsValids(self,board):
		self.validsMoviments = []
		if not self.moved:
			if board[self.row][7].__class__ is Rook and not board[self.row][7].moved:
				rook = True
				for x in range(5,7):
					if board[self.row][x] != 0:
						rook = False
				if rook:
					self.validsMoviments.append([self.row,self.col+2,ROOK])
			if board[self.row][7].__class__ is Rook and not board[self.row][7].moved:
				rook = True
				for x in range(1,4):
					if board[self.row][x] != 0:
						rook = False
				if rook:
					self.validsMoviments.append([self.row,self.col-2,ROOK])
		for r in range(-1,2):
			for c in range(-1,2):
					row = self.row + r
					col = self.col + c
					if row >= 0 and row < 8 and col >= 0 and col < 8 :
						if board[row][col] == 0 or board[row][col].color != self.color:
							self.validsMoviments.append([row,col,True])
