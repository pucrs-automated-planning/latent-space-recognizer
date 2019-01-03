# Lights Out!
# FROM: http://inventwithpython.com/extra/lightsout.py

# Slide Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import pygame, sys, random, pprint, string, math
from pygame.locals import *

import time
# import generate_domain as gd
import subprocess

# Interprocess communication Python/Java
# JAVAPROC = subprocess.Popen(["java", "javaProc"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

BOARD_COLUMNS = 5  # number of columns in the board
BOARD_ROWS = 5 # number of rows in the board

TILESIZE = 60
BOARD_XMARGIN = 75
BOARD_YMARGIN = 75

BOARD_WIDTH = BOARD_COLUMNS * TILESIZE
BOARD_HEIGHT = BOARD_ROWS * TILESIZE

GOALS_IMAGE_WIDTH = 120
GOALS_IMAGE_HEIGHT = 120
NUM_GOALS = 6

WINDOWWIDTH = BOARD_WIDTH + (BOARD_XMARGIN*2) + (GOALS_IMAGE_WIDTH*2)
WINDOWHEIGHT = BOARD_HEIGHT + (BOARD_YMARGIN) + (GOALS_IMAGE_HEIGHT*NUM_GOALS)

FPS = 240

# Colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
MIDGRAY = (178, 190, 195)
LIGHTGRAY = (223, 230, 233)
DARKGRAY = (45, 52, 54)

BGCOLOR = (65, 72, 74)
TILECOLOR = LIGHTGRAY
TEXTCOLOR = WHITE
BORDERCOLOR = MIDGRAY
BASICFONTSIZE = 20

BUTTONCOLOR = LIGHTGRAY
BUTTONTEXTCOLOR = DARKGRAY
MESSAGECOLOR = LIGHTGRAY




def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Lights Out!')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    # Store the option buttons and their rectangles in OPTIONS.
    RESET_SURF, RESET_RECT = makeText('Reset',    BUTTONTEXTCOLOR, BUTTONCOLOR, BOARD_XMARGIN, (BOARD_YMARGIN + TILESIZE*BOARD_ROWS + 80))
    NEW_SURF,   NEW_RECT   = makeText('New Game', BUTTONTEXTCOLOR, BUTTONCOLOR, BOARD_XMARGIN, (BOARD_YMARGIN + TILESIZE*BOARD_ROWS + 50))
    
    mainBoard = getNewBoard()
    originalBoard = getBoardCopy(mainBoard) # for when the player wants to reset the board

    movesTaken = 0

    while True: # main game loop

        msg = 'Click a tile!' # contains the message to show in the upper left corner.

        if isBoardOff(mainBoard): # Player has won the game
            msg = 'Solved!'

        drawBoard(mainBoard, msg)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):
                    # check if the user clicked on an option button
                    if RESET_RECT.collidepoint(event.pos): # clicked on Reset button
                        mainBoard = getBoardCopy(originalBoard)
                        movesTaken = 0
                    elif NEW_RECT.collidepoint(event.pos): # clicked on New Game button
                        mainBoard = getNewBoard()
                        movesTaken = 0
                else:
                    movesTaken += 1
                    makeMove(mainBoard, spotx, spoty)
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def getLeftTopOfTile(tileX, tileY):
    left = BOARD_XMARGIN + (tileX * TILESIZE) + (tileX - 1)
    top = BOARD_YMARGIN + (tileY * TILESIZE) + (tileY - 1)
    return (left, top)


def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


def drawTile(tilex, tiley, light, adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    left, top = getLeftTopOfTile(tilex, tiley)
    if light == False:
        pygame.draw.rect(DISPLAYSURF, DARKGRAY, (left + adjx, top + adjy, TILESIZE, TILESIZE))
    else:
        pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))


def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)


def drawGoals():
    for board_num in range(6):
        # Get image
        board_image = pygame.image.load('mnist_sample_image.png')
        board_image = pygame.transform.scale(board_image, (GOALS_IMAGE_WIDTH, GOALS_IMAGE_HEIGHT))

        # Display image
        left = BOARD_XMARGIN + TILESIZE*BOARD_COLUMNS + BOARD_XMARGIN
        top = BOARD_YMARGIN + (board_num * (GOALS_IMAGE_HEIGHT + 25))
        DISPLAYSURF.blit(board_image, (left, top))

        # Set probability
        probability = 0.16

        # Show text with probability
        text_left = (BOARD_XMARGIN*2) + BOARD_WIDTH + GOALS_IMAGE_HEIGHT + 25
        text_top = BOARD_YMARGIN + (board_num * (GOALS_IMAGE_HEIGHT + 25)) + (GOALS_IMAGE_HEIGHT/2 - 10)
        textSurf, textRect = makeText(str(probability), MESSAGECOLOR, BGCOLOR, text_left, text_top)
        DISPLAYSURF.blit(textSurf, textRect)


def drawBoard(board, message):
    DISPLAYSURF.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
        DISPLAYSURF.blit(textSurf, textRect)

    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            drawTile(tilex, tiley, board[tilex][tiley])

    left, top = getLeftTopOfTile(0, 0)
    width = BOARD_COLUMNS * TILESIZE
    height = BOARD_ROWS * TILESIZE
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

    ################################################

    # JAVAPROC.stdin.write(b"haha\n")
    # JAVAPROC.stdin.flush()
    # out = JAVAPROC.stdout.readline()
    # print("Java output:", out)

    # Draw goals
    drawGoals()

    ################################################

    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)


def getNewBoard():
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(BOARD_COLUMNS):
        board.append([False] * BOARD_ROWS)
    return board


def getBoardCopy(board):
    dupeBoard = getNewBoard()
    for x in range(BOARD_COLUMNS):
        for y in range(BOARD_ROWS):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard


def isOnBoard(board, x, y):
    return x >= 0 and x < BOARD_COLUMNS and y >= 0 and y < BOARD_ROWS


def makeMove(board, x, y):
    if isOnBoard(board, x, y): # flip space
        board[x][y] = not board[x][y]
    if isOnBoard(board, x, y-1): # flip space above
        board[x][y-1] = not board[x][y-1]
    if isOnBoard(board, x, y+1): # flip space below
        board[x][y+1] = not board[x][y+1]
    if isOnBoard(board, x-1, y): # flip space to the left
        board[x-1][y] = not board[x-1][y]
    if isOnBoard(board, x+1, y): # flip space to the right
        board[x+1][y] = not board[x+1][y]


def isBoardOff(board):
    for x in range(BOARD_COLUMNS):
        for y in range(BOARD_ROWS):
            if board[x][y]:
                return False
    return True


if __name__ == '__main__':
    main()