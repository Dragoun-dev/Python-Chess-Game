# Main driver file. It will be responsible for handling users input and displaying he current game states object.

import pygame as p
from engin import *

WIDTH = HEIGHT = 512 
DIMENSION = 8 # CHess board 8*8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation laters on
IMAGES = {}

'''
 Initialize a global directory of image. This willl be call exactly once in the main
'''

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES['wp'] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
 
 
 #The main driver our code. this will handle the input and update the graph
 

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.ick(MAX_FPS)
        p.display.flip()


if __name__ == "__main__":
    main()