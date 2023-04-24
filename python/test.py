import pygame
import sys
import os
import random
from pygame import *

red = (255, 0, 0)
white = (255,255,255)
black = (0, 0, 0)

WIDTH = 400
HEIGHT = 600

DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('RACING')

FPS = 60
fpsgame = pygame.time.Clock()

pygame.init()

BGSPEED = 2

class BackGround():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = BGSPEED
        


class Car():
    pass

def gameStart():
    pass

def gamePlay():
    pass

def gameOver():
    pass
def main():

    gameStart()
    while True():
        gamePlay()
        gameOver()
    
if __name__ == "__main__":
    main()