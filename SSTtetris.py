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

def check_and_delete_bottom_blocks_and_increase_count_and_y_speed(bottom_blocks, count, y_speed):
    for i in range(dimension[0]):
        index = 0
        for j in range(dimension[1]):
            if bottom_blocks.blocks[j][i] == 0:
                index = 1
        if index == 0:
            bottom_blocks.kill(i)
            count += 1
            if count % 3 == 0:
                y_speed += 0.1
    return bottom_blocks, count, y_speed

