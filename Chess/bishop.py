from piece import Piece
import pygame

BLACK = 1

class Bishop(Piece):
	def __init__(self,row,col,color):
		Piece.__init__(self,row,col,color)
		if color == BLACK:
			self.img = pygame.image.load ('images/bishopB.png')
		else:
			self.img = pygame.image.load ('images/bishopW.png')

	def movimentsValids(self,board):
		self.validsMoviments = []
		tr,tl,br,bl = True,True,True,True
		n = 1
		while tr or tl or br or bl:
			x = self.row + n
			y = self.col + n
			if tr:
				if (y > 7 or x > 7):
					tr = False
				elif board[x][y] != 0:
					if board[x][y].color != self.color:
						self.validsMoviments.append([x,y,True])
					tr = False
				else:
					self.validsMoviments.append([x,y,True])

			x = self.row - n
			y = self.col + n
			if br:
				if (y > 7 or x < 0):
					br = False
				elif board[x][y] != 0:
					if board[x][y].color != self.color:
						self.validsMoviments.append([x,y,True])
					br = False
				else:
					self.validsMoviments.append([x,y,True])

			x = self.row + n
			y = self.col - n
			if tl:
				if (y < 0 or x > 7):
					tl = False
				elif board[x][y] != 0:
					if board[x][y].color != self.color:
						self.validsMoviments.append([x,y,True])
					tl = False
				else:
					self.validsMoviments.append([x,y,True])

			x = self.row - n
			y = self.col - n
			if bl:
				if (y < 0 or x < 0):
					bl = False
				elif board[x][y] != 0:
					if board[x][y].color != self.color:
						self.validsMoviments.append([x,y,True])
					bl = False
				else:
					self.validsMoviments.append([x,y,True])
			n+= 1