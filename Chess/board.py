import pygame
import math

from pawn import Pawn
from bishop import Bishop
from horse import Horse
from rook import Rook
from queen import Queen
from king import King

from copy import copy


WHITE = 0
BLACK = 1
ONPASSAN = 2
ROOK = 3
LITTER = 4
BIG = 5
PROMOTION = 6
CREATEPASSAN = 7

class Board():
	def __init__ (self):
		self.rows = 8
		self.cols = 8
		self.board = [[ 0 for y in range(self.cols)] for x in range(self.rows)]

		self.whitePieces = []
		self.blackPieces = []

		##Black Pieces
		self.board[0][0] = Rook(0,0,BLACK)
		self.board[0][1] = Horse(0,1,BLACK)
		self.board[0][2] = Bishop(0,2,BLACK)
		self.board[0][3] = Queen(0,3,BLACK)
		## King in self.kings
		self.board[0][5] = Bishop(0,5,BLACK)
		self.board[0][6] = Horse(0,6,BLACK)
		self.board[0][7] = Rook(0,7,BLACK)
		
		self.board[1][0] = Pawn(1,0,BLACK)
		self.board[1][1] = Pawn(1,1,BLACK)
		self.board[1][2] = Pawn(1,2,BLACK)
		self.board[1][3] = Pawn(1,3,BLACK)
		self.board[1][4] = Pawn(1,4,BLACK)
		self.board[1][5] = Pawn(1,5,BLACK)
		self.board[1][6] = Pawn(1,6,BLACK)
		self.board[1][7] = Pawn(1,7,BLACK)
 		
 		##White Pieces
		self.board[7][0] = Rook(7,0,WHITE)
		self.board[7][1] = Horse(7,1,WHITE)
		self.board[7][2] = Bishop(7,2,WHITE)
		self.board[7][3] = Queen(7,3,WHITE)
		## King in self.kings
		self.board[7][5] = Bishop(7,5,WHITE)
		self.board[7][6] = Horse(7,6,WHITE)
		self.board[7][7] = Rook(7,7,WHITE)

		self.board[6][0] = Pawn(6,0,WHITE)
		self.board[6][1] = Pawn(6,1,WHITE)
		self.board[6][2] = Pawn(6,2,WHITE)
		self.board[6][3] = Pawn(6,3,WHITE)
		self.board[6][4] = Pawn(6,4,WHITE)
		self.board[6][5] = Pawn(6,5,WHITE)
		self.board[6][6] = Pawn(6,6,WHITE)
		self.board[6][7] = Pawn(6,7,WHITE)

		self.player = WHITE
		self.timeOf = WHITE
		self.onpassan = False
		self.promotion = False
		self.kings = [King(7,4,WHITE),King(0,4,BLACK)]

		self.colorSelected = BLACK

		#add kings in board
		self.board[7][4] = self.kings[WHITE]
		self.board[0][4] = self.kings[BLACK]

		self.setArrayOfPieces()
		self.defineValidsMoviments(WHITE)

	def drawPieces(self,display):
		if self.player == WHITE:
			for w in self.whitePieces:
				w.draw(display,False)
			for b in self.blackPieces:
				b.draw(display,False)
		else:
			for w in self.whitePieces:
				w.draw(display,True)
			for b in self.blackPieces:
				b.draw(display,True)

		if self.promotion != False:
			self.choices(display)

	def drawBoard(self,display):
		wh = 50
		if self.player == WHITE:
			for x in range(self.rows):
				for y in range(self.cols):
					if (x + y)%2 == 0: 
						display.fill((255,255,255),(x*wh,y*wh,wh,wh))	
					else:
						display.fill((55,155,55),(x*wh,y*wh,wh,wh))
		else:
			for x in range(self.rows):
				for y in range(self.cols):
					if (x + y)%2 == 1: 
						display.fill((255,255,255),(x*wh,y*wh,wh,wh))	
					else:
						display.fill((55,155,55),(x*wh,y*wh,wh,wh))

	def setArrayOfPieces(self):
		for r in range(8):
			for c in range(8):
				p = self.board[r][c]
				if p != 0:
					if p.color == WHITE:
						self.whitePieces.append(p)
					else:
						self.blackPieces.append(p)

	def moveValid(self,piece,newR,newC,player):
		if piece.color == player:
			for p in piece.validsMoviments:
				if p[0] == newR and p[1] == newC:
					if p[2] == PROMOTION and self.timeOf == p[3]:
						self.promotion = p
					elif p[2] == PROMOTION and self.timeOf != p[3]:
						return True
					elif p[2] == CREATEPASSAN:
						self.onpassan = p
					return p[2]
			return False
		else:
			return False
 
	def checkRook(self,color,type_rook):
 		if type_rook == LITTER:
 			test = [4,5,6]
 		else:
 			test = [2,3,4]
 		if color == WHITE:
 			pieceForAttack = self.blackPieces
 		else:
 			pieceForAttack = self.whitePieces
 		for p in pieceForAttack:
 			for t in test:
 				if color == WHITE and self.moveValid(p,7,t,BLACK):
 					return False
 				elif color == BLACK and self.moveValid(p,0,t,WHITE):
 					return False
 		return True

	def pieceMove(self,row,col,newR,newC):
		piece = self.board[row][col]
		if self.onpassan != False and self.onpassan[2] == self.timeOf:
			self.onpassan = False
		ok = self.moveValid(piece,newR,newC,self.timeOf) 
		
		if ok != False:
			if ok == ROOK:
				if newC == 6 and self.checkRook(piece.color,LITTER):
					rook = self.board[piece.row][7]
					rook.move(piece.row,5)
					self.board[piece.row][7] = 0
					self.board[piece.row][5] = rook
				elif newC == 2 and self.checkRook(piece.color,BIG):
					rook = self.board[piece.row][0]
					rook.move(piece.row,3)
					self.board[piece.row][0] = 0
					self.board[piece.row][3] = rook
				else:
					return False
							
			piece.move(newR,newC)
			if self.board[newR][newC] != 0 or ok == ONPASSAN:
				if ok == ONPASSAN:
					color = self.board[row][newC].color
					self.board[row][newC] = 0
					index = self.getIndex(color,row,newC)
				else:	
					color = self.board[newR][newC].color
					index = self.getIndex(color,newR,newC)

				if color == WHITE:
					self.whitePieces.pop(index)
				else:
					self.blackPieces.pop(index)
			self.board[newR][newC] = piece
			self.board[row][col] = 0

			if not ok == PROMOTION:
				if self.timeOf == WHITE:
					self.timeOf = BLACK
				else:
					self.timeOf = WHITE
				self.End()


			return True
		else:
			return False
	
	def choices(self,display):
		if self.promotion != False:
			display.fill((0,80,0),(75,150,250,100))
			display.fill((0,110,0),(80,155,240,90))
			if self.promotion[3] == WHITE:
				imgChoices = pygame.image.load("images/choices_white.png")
				display.blit(imgChoices,(100,175))
			else:
				imgChoices = pygame.image.load("images/choices_black.png")
				display.blit(imgChoices,(100,175))

	def getIndex(self,color,row,col):
		if color == WHITE:
			index = 0
			for piece in self.whitePieces:
				if piece.row == row and piece.col == col:
					return index
				index += 1
		else:
			index = 0
			for piece in self.blackPieces:
				if piece.row == row and piece.col == col:
					return index
				index += 1

	def promotionFor(self,typePiece):
		row = self.promotion[0]
		col = self.promotion[1]
		color = self.promotion[3]
		index = self.getIndex(color,row,col)

		if typePiece == 'queen':
			self.board[row][col] = Queen(row,col,color)
		elif typePiece == 'rook':
			self.board[row][col] = Rook(row,col,color)
		elif typePiece == 'bishop':
			self.board[row][col] = Bishop(row,col,color)
		elif typePiece == 'horse':
			self.board[row][col] = Horse(row,col,color)

		self.promotion = False
		if color == BLACK:
			self.timeOf = WHITE
			self.blackPieces[index] = self.board[row][col]
		else:
			self.timeOf = BLACK
			self.whitePieces[index] = self.board[row][col]
		
		self.End()

	def numberOfValidMoviment(self,color):
		numberOfValidMoviment = 0
		if color == WHITE:
			for p in self.whitePieces:
				numberOfValidMoviment += len(p.validsMoviments)
		else:
			for p in self.blackPieces:
				numberOfValidMoviment += len(p.validsMoviments)
		return numberOfValidMoviment

	def calcAttackKing(self,cKing):
		if cKing == WHITE:
			king = self.kings[WHITE]
			for p in self.blackPieces:
				if self.moveValid(p,king.row,king.col,BLACK):
					return True
			return False
		else:
			king = self.kings[BLACK]
			for p in self.whitePieces:
				if self.moveValid(p,king.row,king.col,WHITE):
					return True
			return False

	def End(self):
		self.defineValidsMoviments(self.timeOf)
		nWhite = self.numberOfValidMoviment(WHITE)
		nBlack = self.numberOfValidMoviment(BLACK)
		if nWhite == 0:
			if self.calcAttackKing(WHITE):
				print("THE BLACK WIN")
			else:
				print("SHAMELESS")
		elif nBlack == 0:
			if self.calcAttackKing(BLACK):
				print("THE WHITE WIN")
			else:
				print("SHAMELESS")
		return False

	def defineValidsMoviments(self,color):
		if color == WHITE:
			for piece in self.whitePieces:
				if piece.__class__ is Pawn:
					piece.movimentsValids(self.board,self.onpassan)
				else:
					piece.movimentsValids(self.board)
				move = 0 
				while move < len(piece.validsMoviments):
					b = [[self.board[r][c] for c in range(8)] for r in range(8)]

					r = piece.validsMoviments[move][0]
					c = piece.validsMoviments[move][1]
					b[r][c] = piece
					b[piece.row][piece.col] = 0

					bPiece = [x for x in self.blackPieces]
					for blackP in bPiece:
						if blackP.__class__ is Pawn:
							blackP.movimentsValids(b,self.onpassan)
						else:
							blackP.movimentsValids(b)

					index = 0
					while index < len(bPiece):
						if bPiece[index].row == r and bPiece[index].col == c:
							bPiece.pop(index)
							index -= 1
						elif piece.__class__ is King:
							if self.moveValid(bPiece[index],r,c,BLACK):
								piece.validsMoviments.pop(move)
								move -= 1
						elif self.moveValid(bPiece[index],self.kings[WHITE].row,self.kings[WHITE].col,BLACK):
							piece.validsMoviments.pop(move)
							move -= 1
						index += 1
					move += 1

		elif color == BLACK:
			for piece in self.blackPieces:
				if piece.__class__ is Pawn:
					piece.movimentsValids(self.board,self.onpassan)
				else:
					piece.movimentsValids(self.board)
				move = 0 
				while move < len(piece.validsMoviments):
					b = [[self.board[r][c] for c in range(8)] for r in range(8)]

					r = piece.validsMoviments[move][0]
					c = piece.validsMoviments[move][1]
					b[r][c] = piece
					b[piece.row][piece.col] = 0

					wPiece = [x for x in self.whitePieces]
					for whiteP in wPiece:
						if whiteP.__class__ is Pawn:
							whiteP.movimentsValids(b,self.onpassan)
						else:
							whiteP.movimentsValids(b)

					index = 0
					while index < len(wPiece):
						if wPiece[index].row == r and wPiece[index].col == c:
							wPiece.pop(index)
							index -= 1
						elif piece.__class__ is King:
							if self.moveValid(wPiece[index],r,c,WHITE):
								piece.validsMoviments.pop(move)
								move -= 1
						elif self.moveValid(wPiece[index],self.kings[BLACK].row,self.kings[BLACK].col,WHITE):
							piece.validsMoviments.pop(move)
							move -= 1
						index += 1
					move += 1