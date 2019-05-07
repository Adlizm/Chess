import pygame

class Piece:
	def __init__(self,row,col,color):
		self.row = row
		self.col = col
		self.color = color
		self.isSelected = False
		self.x = None
		self.y = None
		self.img = None
		self.validsMoviments = []
		self.moved = False

	def move(self,r,c):
		self.row = r
		self.col = c
		self.moved = True

	def select(self):
		self.isSelected = True

	def draw(self,display,inverse):
		wh = display.get_width()/8
		if not inverse:
			if not self.isSelected:
				self.x = self.col*wh
				self.y = self.row*wh
			display.blit(self.img,(self.x,self.y))
		else:
			if not self.isSelected:
				self.x = self.col*wh
				self.y = display.get_height() - self.row*wh - wh
			display.blit(self.img,(self.x,self.y))
	
	def calcCheckKing(self,board,king):
		for r in range(self.rows):
 			for c in range(self.cols):
	 			if board[r][c] != 0 and board[r][c].color != king.color:
	 				if self.moveValid(board[r][c],king.row,king.col,ColorPlayerAttack):
	 					return True
		return False