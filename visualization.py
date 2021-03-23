import pygame
import sys
import random

WIDTH = 1280
HEIGHT = 720
BLACK = pygame.Color(0, 0, 0)

num_bars = 200
bar_witdh = 4
space = 2

BLUE = (0, 0, 255)

# Initialize the pygame
pygame.init()

#num_bars = int(input("Enter the number of samples: "))

# Create the screen
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

# Set Background color
SCREEN.fill((255,255,255))
pygame.display.update()

def drawBar(i,height):
    pygame.draw.rect(SCREEN, BLUE, (x, 690, bar_witdh, height), 0, 6)

for i in range(num_bars): 
    height = random.randint(-num_bars*2, -2)
    print(height)
    x = (i * bar_witdh) + (i * space) + (WIDTH - (num_bars * bar_witdh + num_bars + space))/7
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
