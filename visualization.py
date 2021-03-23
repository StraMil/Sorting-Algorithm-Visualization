import pygame
import sys
import random
import time

WIDTH = 1280
HEIGHT = 720
BLACK = pygame.Color(0, 0, 0)

num_bars = 10
bar_witdh = 4
space = 2
sorting = False
bars = []

BLUE = (0, 0, 255)

# Initialize the pygame
pygame.init()

font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

# Create the screen
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

# Set Background color
SCREEN.fill((255,255,255))
pygame.display.update()

def bubbleSort(array):
    elapsed = clock.tick(1)

    n = len(array)
    for i in range(n):
        for j in range(0, n-1-i):
            for k in range(num_bars):
                x = (k * bar_witdh) + (k * space) + (WIDTH - (num_bars * bar_witdh + num_bars + space))/7
                height = bars[k]
                drawBar(x, height)
            pygame.display.update()
            time.sleep(1)

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            SCREEN.fill((255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    global sorting

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(SCREEN, ac, (x,y,w,h), 0)

        if click[0] == 1:
            sorting = True
    
    else:
        pygame.draw.rect(SCREEN, ic, (x, y, w, h), 0)
    
    text = font.render(msg, True, (0, 0, 0))
    SCREEN.blit(text, (x + 10, y + 10))

def drawBar(i,height):
    pygame.draw.rect(SCREEN, BLUE, (x, 690, bar_witdh, height), 0, 6)
    bars.append(height)

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
    button("Sort", 200-75/2, 200-25, 75, 50, (230, 230, 230), (200, 200, 200))
    pygame.display.update()

    if sorting:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


bubbleSort(bars)