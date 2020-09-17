import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 500, 200
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

normal_font = pygame.font.SysFont("comicsans", 60)
pygame.display.set_caption("Lottery Machine")

WHITE = (255,255,255)
BLACK = (0,0,0)

winner = random.sample(range(1, 46), 7)
winner_bonus = winner[-1]
winner_num = winner[:-1]
winner_num.sort()
winner_num = winner_num
winner_bonus = winner_bonus

def printText(msg, color=BLACK, pos=(50, 50)):
    text = normal_font.render(msg, 1, color)
    WINDOW.blit(text, pos)

def ranking(cust, winner_num, winner_bonus):
    cust = set(cust)
    winner_num = set(winner_num)
    if len(cust&winner_num)==6:
        return '1st Place'
    elif len(cust&winner_num)==5 and (winner_bonus in cust):
        return '2nd Place'
    elif len(cust&winner_num)==5:
        return '3rd Place'
    elif len(cust&winner_num)==4:
        return '4th Place'
    elif len(cust&winner_num)==3:
        return '5th Place'

def fullAuto():
    cust_fullAuto = random.sample(range(1,46), 6)
    cust_fullAuto.sort()
    printText(str(cust_fullAuto), BLACK)
    printText(ranking(cust_fullAuto, winner_num, winner_bonus), BLACK, (50, 70))
        


def main():
    run = True
    FPS = 60
    MOUSECLICK = None

    while run:
        clock = pygame.time.Clock()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                MOUSECLICK = True

        if MOUSECLICK == True:
            fullAuto()
            pygame.display.update()

        WINDOW.fill(WHITE)

        pygame.display.flip()

    pygame.quit()

main()
