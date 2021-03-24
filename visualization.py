import pygame
import sys
import random
import time

WIDTH = 1280
HEIGHT = 400
BLACK = pygame.Color(0, 0, 0)

num_bars = 200
bar_witdh = 800/num_bars
space = 400/num_bars
sorting = False
bars = []
cycles = 0

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

def bubbleSort(bars):
    sorting = False
    cycles = 0
    for i in range(len(bars)-1):
        for j in range(0, len(bars)-1-i):
            if bars[j] < bars[j + 1]:
                bars[j], bars[j + 1] = bars[j + 1], bars[j]
                print(bars)
                SCREEN.fill((255,255,255))
                for k in range(len(bars)):
                    x = (k * bar_witdh) + (k * space) + (WIDTH - (num_bars * bar_witdh + num_bars * space))/2
                    if bars[k] is bars[j]:
                        red = 255
                        green = 130
                        blue = 80
                        last = k
                    else:
                        red = 0
                        blue = bars[k] * (-1)
                        green = 255 - blue
                    pygame.draw.rect(SCREEN, ((red, green, blue)), (x, 365, bar_witdh, bars[k]), 0, 6)
                buttonSort("Sort", 105 + 30, 30, 75, 50, (230, 230, 230), (200, 200, 200))
                buttonNewArray("New", 30, 30, 75, 50, (230, 230, 230), (200, 200, 200))
                showNumOfCycles(cycles)
                pygame.display.update()
                #time.sleep(0.0001)
            cycles = cycles + 1

    red = 0
    blue = bars[last] * (-1)
    green = 255 - blue
    x = (last * bar_witdh) + (last * space) + (WIDTH - (num_bars * bar_witdh + num_bars * space))/2
    pygame.draw.rect(SCREEN, ((red, green, blue)), (x, 365, bar_witdh, bars[last]), 0, 6)
    pygame.display.update()
    print(last)

def getHeight(num_bars):
    if num_bars <= 50:
        return 5
    if num_bars <= 100:
        return 2.5
    if num_bars <= 200:
        return 1.25
    else:
        return 1

def buttonSort(msg, x, y, w, h, ic, ac):
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

def buttonNewArray(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(SCREEN, ac, (x,y,w,h), 0)

        if click[0] == 1:
            cycles = 0
            SCREEN.fill((255,255,255))
            bars.clear()
            mulitplayer = getHeight(num_bars)
            print(mulitplayer)
            for i in range(num_bars):
                height = random.randint(-num_bars*mulitplayer, -5)
                print(height)
                x = (i * bar_witdh) + (i * space) + (WIDTH - (num_bars * bar_witdh + num_bars * space))/2
                drawBar(x,height)
            print(bars)

    else:
        pygame.draw.rect(SCREEN, ic, (x, y, w, h), 0)

    text = font.render(msg, True, (0, 0, 0))
    SCREEN.blit(text, (x + 10, y + 10))

def showNumOfCycles(cicles):
    cicle = font.render("Cycles: " + str(cicles), True, (0,0,0))
    SCREEN.blit(cicle, (1100, 30))

def drawBar(x,height):
    blue = height * (-1)
    green = 255-blue
    pygame.draw.rect(SCREEN, (0,green,blue), (x, 365, bar_witdh, height), 0, 6)
    if not sorting:
        bars.append(height)

# Game Loop
while True:
    buttonSort("Sort", 105 + 30, 30, 75, 50, (230, 230, 230), (200, 200, 200))
    buttonNewArray("New", 30, 30, 75, 50, (230, 230, 230), (200, 200, 200))
    pygame.display.update()

    if sorting:
        bubbleSort(bars)
        sorting = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

