from piece import Piece
import pygame

BLACK = 1

class Rook(Piece):
	def __init__(self,row,col,color):
		Piece.__init__(self,row,col,color)
		if color == BLACK:
			self.img = pygame.image.load ('images/rookB.png')
		else:
			self.img = pygame.image.load ('images/rookW.png')
			
	def movimentsValids(self,board):
		self.validsMoviments = []
		top,bot,rig,lef = True,True,True,True
		n = 1
		while top or bot or rig or lef:
			r = self.row + n
			c = self.col
			if top:
				if r > 7:
					top = False
				elif board[r][c] != 0:
					if board[r][c].color != self.color:
						self.validsMoviments.append([r,c,True])
					top = False
				else:
					self.validsMoviments.append([r,c,True])

			r = self.row - n
			c = self.col
			if bot:
				if r < 0:
					bot = False
				elif board[r][c] != 0:
					if board[r][c].color != self.color:
						self.validsMoviments.append([r,c,True])
					bot = False
				else:
					self.validsMoviments.append([r,c,True])

			r = self.row
			c = self.col + n
			if rig:
				if c > 7:
					rig = False
				elif board[r][c] != 0:
					if board[r][c].color != self.color:
						self.validsMoviments.append([r,c,True])
					rig = False
				else:
					self.validsMoviments.append([r,c,True])

			r = self.row
			c = self.col - n
			if lef:
				if c < 0:
					lef = False
				elif board[r][c] != 0:
					if board[r][c].color != self.color:
						self.validsMoviments.append([r,c,True])
					lef = False
				else:
					self.validsMoviments.append([r,c,True])
			n+= 1