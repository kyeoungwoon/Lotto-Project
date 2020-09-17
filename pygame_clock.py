import pygame
import datetime
import time

pygame.init()

WIDTH, HEIGHT = 500, 200
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("AppleSDGothicNeoL00", 60)
pygame.display.set_caption('TEST')

def printText(msg, color = BLACK, pos = (50,50)):
    text = font.render(msg, True, color)
    WINDOW.blit(text, pos)

def currentTime():
    ct = datetime.datetime.now()
    return str(f"{ct.year}. {ct.month}. {ct.day}. | {ct.hour} : {ct.minute} : {ct.second}")

def showTime():
    WINDOW.fill((0,0,0))
    printText(currentTime())
    pygame.display.update()

def iTime():
    tm = time.time()
    text = font.render(str(tm), 1, (255,255,255))
    WINDOW.blit(text, (50,50))
    pygame.display.update()

run = True
MOUSEDOWN = None
MOUSEUP = None

while run:
    clock = pygame.time.Clock()
    clock.tick(60)
    WINDOW.fill(WHITE)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            MOUSEDOWN = True
        if event.type == pygame.MOUSEBUTTONUP:
            MOUSEUP = True
            
    if MOUSEDOWN == True:
        start_time = time.time()
        if MOUSEUP == True:
            end_time = time.time()
            printText(str(end_time - start_time))
            MOUSEUP = None
            MOUSEDOWN = None


pygame.quit()