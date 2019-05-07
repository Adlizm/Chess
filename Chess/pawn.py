from piece import Piece
import pygame

WHITE = 0
BLACK = 1
ONPASSAN = 2
PROMOTION = 6
CREATEPASSAN = 7

class Pawn(Piece):
	def __init__(self,row,col,color):
		Piece.__init__(self,row,col,color)
		if color == BLACK:
			self.img = pygame.image.load ('images/pawnB.png')
		else:
			self.img = pygame.image.load ('images/pawnW.png')
		
	def movimentsValids(self,board,onpassan):
		self.validsMoviments = []
		if self.color == WHITE:
			ddV = -1
		else:
			ddV = 1
		r = self.row + ddV
		c = self.col

		if not self.moved:
			if r > 0 and r < 7 and board[r][c] == 0:
				self.validsMoviments.append([r,c,True])
				if r + ddV > 0 and r + ddV < 7 and board[r + ddV][c] == 0:
					self.validsMoviments.append([r + ddV,c,CREATEPASSAN,self.color])
				if c + 1 < 8 and board[r][c + 1] != 0 and board[r][c + 1].color != self.color:
					self.validsMoviments.append([r,c+1,True])
				if c - 1 >= 0  and board[r][c - 1] != 0 and board[r][c - 1].color != self.color:
					self.validsMoviments.append([r,c - 1,True])
		else:
			if r > 0 and r < 7:
				if board[r][c] == 0:
					self.validsMoviments.append([r,c,True])
				if c + 1 < 8 and board[r][c + 1] != 0 and board[r][c + 1].color != self.color:
					self.validsMoviments.append([r,c+1,True])
				if c - 1 >= 0 and board[r][c - 1] != 0 and board[r][c - 1].color != self.color:
					self.validsMoviments.append([r,c - 1,True])
				if onpassan != False and onpassan[0] == self.row:
					if onpassan[1] == c + 1:
						self.validsMoviments.append([r,c+1,ONPASSAN])
					elif onpassan[1] == c - 1:
						self.validsMoviments.append([r,c-1,ONPASSAN])
			elif r == 0 or r == 7:
				if board[r][c] == 0:
					self.validsMoviments.append([r, c ,PROMOTION,self.color])

				if c + 1 < 8 and board[r][c + 1] != 0 and board[r][c + 1].color != self.color:
					self.validsMoviments.append([r, c+ 1,PROMOTION,self.color])

				if c - 1 >= 0 and board[r][c - 1] != 0 and board[r][c - 1].color != self.color:
					self.validsMoviments.append([r,c - 1,PROMOTION,self.color])
