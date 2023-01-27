import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

# Colores RGB almacenados en variables
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)
GREEN = (0,255,0)

pygame.font.init()
MY_FONT = pygame.font.SysFont("monospace", 75) 

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
def drop_piece(board, row, col, piece):
    board[row][col] = piece

def print_board(board):
    print(np.flipud(board))

def winning_move(board, piece):
    #revisando las posiciones horizontales
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # verificando las posiciones verticales
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # verificando diagonales positivas
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True 

    # verificando diagonales negativas
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True 

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), (heigth+SQUARESIZE)-int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), (heigth+SQUARESIZE)-int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0 # variable para definir usuario 1 y 2

pygame.init()

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
heigth = (ROW_COUNT+1) * SQUARESIZE

size = (width, heigth)
RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        #Configurando el cierre de la ventana para que el programa no cierre inesperadamente
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        #solicitando la movida al jugador 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            # print(event.pos)
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                # col = int(input("Jugador 1 haz tu movida (0,6):"))
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    
                    if winning_move(board, 1):
                        # print("Player 1 wins!!!")
                        label = MY_FONT.render("Player 1 wins!!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True
            
            #solicitando la movida al jugador 2
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                # col = int(input("Jugador 2 haz tu movida(0,6):"))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        # print("Player 2 wins!!!")
                        label = MY_FONT.render("Player 2 wins!!!", 1, GREEN)
                        screen.blit(label, (40,10))
                        game_over = True

            print_board(board)
            draw_board(board)
            
            turn += 1 #se incrementa en uno el turno
            turn = turn % 2 #alternando entre cero y uno

            if game_over:
                pygame.time.wait(3000)