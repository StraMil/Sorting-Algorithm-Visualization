import pygame
import sys
import random
import time

WIDTH = 1280
HEIGHT = 400
BLACK = pygame.Color(0, 0, 0)

num_bars = 50
bar_witdh = 800/num_bars
space = 400/num_bars
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

def test(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-1-i):
            SCREEN.fill((255,255,255))
            for k in range(num_bars):
                x = (k * bar_witdh) + (k * space) + (WIDTH - (num_bars * bar_witdh + num_bars * space))/7
                height = bars[k]
                drawBar(x, height)
            pygame.display.update()
            time.sleep(1)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def bubbleSort(bars):
    sorting = False
    for i in range(len(bars)-1):
        for j in range(0, len(bars)-1-i):
            #SCREEN.fill((255,255,255))
            #for k in range(len(bars)):
                #x = (k * bar_witdh) + (k * space) + (WIDTH - (num_bars * bar_witdh + num_bars * space))/2
                #pygame.draw.rect(SCREEN, ((0, 255, 255)), (x, 690, bar_witdh, bars[k]/(k+1)), 0, 6)
            #pygame.display.update()
            #time.sleep(1)
            if bars[j] < bars[j + 1]:
                bars[j], bars[j + 1] = bars[j + 1], bars[j]
                print(bars)
                SCREEN.fill((255,255,255))
                for k in range(len(bars)):
                    x = (k * bar_witdh) + (k * space) + (WIDTH - (num_bars * bar_witdh + num_bars * space))/2
                    if bars[k] is bars[j+1]:
                        red = 255
                        green = 130
                        blue = 80
                        last = k
                    else:
                        red = 0
                        blue = bars[k] * (-1)
                        green = 255 - blue
                    pygame.draw.rect(SCREEN, ((red, green, blue)), (x, 370, bar_witdh, bars[k]), 0, 6)
                    #op(x, bars[k], green, blue)
                pygame.display.update()
                time.sleep(0.05)

    red = 0
    blue = bars[last] * (-1)
    green = 255 - blue
    x = (last * bar_witdh) + (last * space) + (WIDTH - (num_bars * bar_witdh + num_bars * space))/2
    pygame.draw.rect(SCREEN, ((red, green, blue)), (x, 370, bar_witdh, bars[last]), 0, 6)
    pygame.display.update()
    print(last)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def op(x, height, g, b):
    pygame.draw.rect(SCREEN, ((0, g, b)), (x, 370, bar_witdh, height), 0, 6)

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
            #pygame.display.update()

    else:
        pygame.draw.rect(SCREEN, ic, (x, y, w, h), 0)

    text = font.render(msg, True, (0, 0, 0))
    SCREEN.blit(text, (x + 10, y + 10))

def drawBar(x,height):
    blue = height * (-1)
    green = 255-blue
    pygame.draw.rect(SCREEN, (0,green,blue), (x, 370, bar_witdh, height), 0, 6)
    #pygame.draw.rect(SCREEN, BLUE, (x, 690, bar_witdh, height), 2)
    if not sorting:
        bars.append(height)

# for i in range(num_bars):
#     height = random.randint(-num_bars+5, -5)
#     print(height)
#     x = (i * bar_witdh) + (i * space) + (WIDTH - (num_bars * bar_witdh + num_bars * space))/2
#     drawBar(x,height)


# for i in range(num_bars):
#     height = random.randint(-100, -10)
#     x = (i * bar_witdh) + (i * space) + (WIDTH - (num_bars * bar_witdh + num_bars + space))/2
#     drawBar(x, height)

# for i in range(10):
#     drawBar(i*(-5),i*(-10))

# Game Loop
while True:
    buttonSort("Sort", 100 + 30, 30, 75, 50, (230, 230, 230), (200, 200, 200))
    buttonNewArray("New", 30, 30, 75, 50, (230, 230, 230), (200, 200, 200))
    pygame.display.update()

    if sorting:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


#bubbleSort(bars)
bubbleSort(bars)