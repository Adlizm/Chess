from piece import Piece
import pygame

BLACK = 1

class Queen(Piece):
	def __init__(self,row,col,color):
		Piece.__init__(self,row,col,color)
		if color == BLACK:
			self.img = pygame.image.load ('images/queenB.png')
		else:
			self.img = pygame.image.load ('images/queenW.png')

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