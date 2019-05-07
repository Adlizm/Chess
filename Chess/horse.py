from piece import Piece
import pygame

BLACK = 1

class Horse(Piece):
	def __init__(self,row,col,color):
		Piece.__init__(self,row,col,color)
		if color == BLACK:
			self.img = pygame.image.load ('images/horseB.png')
		else:
			self.img = pygame.image.load ('images/horseW.png')

	def movimentsValids(self,board):
		self.validsMoviments = []
		r = self.row + 2
		c = self.col
		if r < 8:
			if c + 1 < 8 and (board[r][c + 1] == 0 or board[r][c + 1].color != self.color):
				self.validsMoviments.append([r,c + 1,True])
			if c - 1 >= 0 and (board[r][c - 1] == 0 or board[r][c - 1].color != self.color):
				self.validsMoviments.append([r,c - 1,True])
	
		r = self.row - 2
		c = self.col
		if r >= 0:
			if c + 1 < 8 and (board[r][c + 1] == 0 or board[r][c + 1].color != self.color):
				self.validsMoviments.append([r,c + 1,True])
			if c - 1 >= 0 and (board[r][c - 1] == 0 or board[r][c - 1].color != self.color):
				self.validsMoviments.append([r,c - 1,True])
		
		r = self.row
		c = self.col + 2
		if c < 8:
			if r + 1 < 8 and (board[r + 1][c] == 0 or board[r + 1][c].color != self.color):
				self.validsMoviments.append([r + 1,c,True])
			if r - 1 >= 0 and (board[r - 1][c] == 0 or board[r - 1][c].color != self.color):
				self.validsMoviments.append([r - 1,c,True])
		
		r = self.row
		c = self.col - 2
		if c >= 0:
			if r + 1 < 8 and (board[r + 1][c] == 0 or board[r + 1][c].color != self.color):
				self.validsMoviments.append([r + 1,c,True])
			if r - 1 >= 0 and (board[r - 1][c] == 0 or board[r - 1][c].color != self.color):
				self.validsMoviments.append([r - 1,c,True])
		