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
map = []


class CrissCross:
    def __init__(self):
        for i in range(3):
            for j in range(3):
                rect = pygame.draw.rect(background, white, ((y+1)*i,(y+1)*j, y, y))
                list_rect.append(rect)
                map.append([rect,0])
    def list_rect():
        return list_rect

tl = CrissCross()

def change_map_value(rect):
    for i in map:
        if i[0] == rect:
            i[1] = 1
    return map

def is_winning():
    if map[0][1] == 1 and map[1][1]==1 and map [2][1] == 1:
        return True
    elif map[3][1] == 1 and map[4][1]==1 and map [5][1] == 1:
        return True
    elif map[6][1] == 1 and map[7][1]==1 and map [8][1] == 1:
        return True
    elif map[0][1] == 1 and map[3][1]==1 and map [6][1] == 1:
        return True
    elif map[1][1] == 1 and map[4][1]==1 and map [7][1] == 1:
        return True
    elif map[2][1] == 1 and map[5][1]==1 and map [8][1] == 1:
        return True
    elif map[0][1] == 1 and map[4][1]==1 and map [8][1] == 1:
        return True
    elif map[2][1] == 1 and map[4][1]==1 and map [6][1] == 1:
        return True

cross = pygame.Rect(200, 100, 161, 100)
circle = pygame.Rect(200, 100, 161, 100)
winner = []
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for rect in CrissCross.list_rect():
                if pygame.Rect.collidepoint(rect, pygame.mouse.get_pos()):
                    cross.center = rect.center
                    pygame.draw.rect(background, (0, 100, 255), cross, 5)
                    change_map_value(rect)
                    new_list = CrissCross.list_rect()
                    new_list.remove(rect)
                    random_rect = random.choice(new_list)
                    if is_winning() == True:
                        sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            for rect in new_list:
                if pygame.Rect.colliderect(rect, random_rect):
                    circle.center = rect.center
                    pygame.draw.rect(background, (0, 0, 0), circle, 5)
                    new_list.remove(rect)
                    break
    screen.blit(background, (0, 0))
    pygame.display.flip()