import pygame
import sys
import random
pygame.init()

x = 600
y = x/3
screen = pygame.display.set_mode((x, x))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
white = (220,220,220)
list_rect=[]

class CrissCross:
    def __init__(self):
        for i in range(3):
            for j in range(3):
                rect = pygame.draw.rect(background, white, ((y+1)*i,(y+1)*j, y, y))
                list_rect.append(rect)
    def list_rect():
        return list_rect
tl = CrissCross()

cross = pygame.Rect(200, 100, 161, 100)
circle = pygame.Rect(200, 100, 161, 100)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for rect in CrissCross.list_rect():
                if pygame.Rect.collidepoint(rect, pygame.mouse.get_pos()):
                    cross.center = rect.center
                    pygame.draw.rect(background, (0, 100, 255), cross, 5)
                    new_list = CrissCross.list_rect()
                    new_list.remove(rect)
                    random_rect = random.choice(new_list)
            for rect in new_list:
                if pygame.Rect.colliderect(rect, random_rect):
                    circle.center = rect.center
                    pygame.draw.rect(background, (0, 0, 0), circle, 5)
                    new_list.remove(rect)
                    break
    screen.blit(background, (0, 0))
    pygame.display.flip()