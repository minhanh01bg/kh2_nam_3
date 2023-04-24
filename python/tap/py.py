import os
import sys
import pygame
import random
from pygame import *

width = 400
height = 300
"""
pygame.draw.circle(surface, color, center, radius, width) Hàm này dùng để vẽ hình tròn.

surface là nơi để vẽ lên.
color là màu được vẽ.
center là một tuple (hoặc list) thể hiện toạ độ tâm hình tròn.
radius là bán kính hình tròn.
width là độ dày nét vẽ (tương tự hình chữ nhật).

        """

"""
    pygame.draw.polygon(surface, color, points, width) Hàm này dùng để vẽ đa giác.

    surface là nơi để vẽ lên.
    color là màu được vẽ.
    points là tuple (hoặc list) thể hiện các đỉnh của đa giác. Mỗi đỉnh là một tuple (hoặc list) thể hiện toạ độ.
    width là độ dày nét vẽ (tương tự hình chữ nhật).

    """


white = (255,255,255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)
pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()
displaysurf = pygame.display.set_mode((width, height))
pygame.display.set_caption('code game')

class Car():
    def __init__(self):
        self.x = 0 # tọa độ chiếc xe
        self.y = 0
        # surface = bề mặt 
        # self.surface = pygame.Surface((100,50), SRCALPHA)
        # pygame.draw.polygon(self.surface, red, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15))) # vẽ đa giác
        # pygame.draw.circle(self.surface, green, (15, 40), 10)
        # pygame.draw.circle(self.surface, green, (85, 40), 10)
        self.surface = pygame.image.load('car.png')

    def draw(self):
        displaysurf.blit(self.surface,(self.x, self.y))
    
    def update(self, moveLeft,moveRight,moveUp,moveDown):
        if moveLeft == True:
            self.x -= 2
        if moveRight == True:
            self.x += 2
        if moveUp == True:
            self.y -=2
        if moveDown == True:
            self.y +=2
        
        if self.x + 100 > width:
            self.x = width - 100
        
        if self.y + 50 > height:
            self.y = height - 50
        if self.x < 0:
            self.x = 0
        
        if self.y < 0:
            self.y = 0

car = Car()

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # sự kiện bấm nút
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
            elif event.key == pygame.K_RIGHT:
                moveRight = True
            elif event.key == pygame.K_UP:
                moveUp = True
            elif event.key == pygame.K_DOWN:
                moveDown = True
        #sự kiện không bấm nút    
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False


    displaysurf.fill(white)

    car.draw()
    car.update(moveLeft,moveRight,moveUp,moveDown)
    
    pygame.display.update()
    fpsClock.tick(FPS)