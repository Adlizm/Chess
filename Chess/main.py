import pygame
import math
from board import *

width,height = 400,400
wh = 50
run = True
b = Board()

pieceSelected = None
mouseD = False

WHITE = 0
BLACK = 1

pygame.init()
icone = pygame.image.load('images/icon.jpg')
pygame.display.set_icon(icone)
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((width,height))
screen.fill((0,0,0))

color  = pygame.Color(150,255,150)
clock = pygame.time.Clock();

def mouseDown(pos):
	global pieceSelected
	mouseD = True
	x = pos[0]
	if b.player == BLACK:
		y = height - pos[1]
	else:
		y = pos[1]
		
	if b.promotion == False:
		col = math.ceil(x/wh) - 1
		row = math.ceil(y/wh) - 1

		if b.board[row][col] != 0:
			pieceSelected = b.board[row][col]
			b.colorSelected = pieceSelected.color
			b.board[row][col].select()
	else:
		if pos[1] >= 175 and pos[1] <= 225:
			if pos[0] > 100 and pos[0] < 150:
				b.promotionFor("queen")
			elif pos[0] < 200:
				b.promotionFor("bishop")
			elif pos[0] < 250:
				b.promotionFor("horse")
			elif pos[0] < 300:
				b.promotionFor("rook")

def mouseUp(pos):
	global pieceSelected
	mouseD = False
	x = pos[0]
	if b.player == BLACK:
		y = height - pos[1]
	else:
		y = pos[1]

	col = math.ceil(x/wh) - 1
	row = math.ceil(y/wh) - 1
	if pieceSelected != None:
		b.pieceMove(pieceSelected.row,pieceSelected.col,row,col)
		pieceSelected.isSelected = False
	pieceSelected = None
			
def mouseMove(pos):
	global pieceSelected
	if pieceSelected != None:
		x = pos[0]
		y = pos[1]
		pieceSelected.x = x - wh/2
		pieceSelected.y = y	- wh/2

while run: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouseDown(event.pos)
		if event.type == pygame.MOUSEBUTTONUP:
			mouseUp(event.pos)
		if event.type == pygame.MOUSEMOTION:
			mouseMove(event.pos)
	
	b.drawBoard(screen)
	if pieceSelected != None:
		if b.player == WHITE:
			for y in pieceSelected.validsMoviments:
				screen.fill(color,(y[1]*wh,y[0]*wh,wh,wh))
		else:		
			for y in pieceSelected.validsMoviments:
				screen.fill(color,(y[1]*wh,screen.get_height() - y[0]*wh - wh,wh,wh))
	b.drawPieces(screen)
	pygame.display.flip()
	clock.tick(10)	