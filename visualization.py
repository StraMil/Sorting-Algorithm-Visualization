import pygame
import sys
import random

WIDTH = 800
HEIGHT = 600
BLACK = pygame.Color(0, 0, 0)

num_bars = 50
bar_witdh = 200/num_bars
space = 100/num_bars

BLUE = (0, 0, 255)

# Initialize the pygame
pygame.init()

# Create the screen
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

# Set Background color
SCREEN.fill((255,255,255))
pygame.display.update()

def drawBar(i,height):
    pygame.draw.rect(SCREEN, BLUE, (x, 400, bar_witdh, height), 0, 6)

for i in range(num_bars): 
    height = random.randint(-100, -10)
    print(height)
    x = (i * bar_witdh) + (i * space) + (WIDTH - (num_bars * bar_witdh + num_bars + space))/2
    drawBar(x,height)
   

# for i in range(num_bars):
#     height = random.randint(-100, -10)
#     x = (i * bar_witdh) + (i * space) + (WIDTH - (num_bars * bar_witdh + num_bars + space))/2
#     drawBar(x, height)

# for i in range(10):
#     drawBar(i*(-5),i*(-10))

# Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
