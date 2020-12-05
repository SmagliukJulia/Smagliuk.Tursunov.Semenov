import pygame
import random
import copy


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

blocksize=30
dimension=[20,10]
size = [blocksize*(dimension[1]+7), blocksize*(dimension[0]+1)]

list_of_tetris=[
    [[-2,-1],[-1,-1],[0,-1],[0,0]],
    [[1,-1],[0,-1],[-1,-1],[-1,0]],
    [[0,0],[0,-1],[-1,-1],[-1,0]],
    [[0,0],[0,-1],[1,-1],[-1,0]],
    [[0, 0], [-2, -1], [-1, -1], [-1, 0]],
    [[-2, -1], [-1, -1], [0, -1],[1,-1] ],
    [[1,0], [0,0], [-1, 0], [0, -1]]
]

different_shapes=len(list_of_tetris)

def set_to_the_beginning():
    return  int(dimension[1]//2),  0, 0

