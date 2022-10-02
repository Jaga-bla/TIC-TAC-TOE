import pygame
import sys
import random
pygame.init()

x = 600
screen = pygame.display.set_mode((x, x))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
white = (220,220,220)

class CrissCross:
    #each value represents different rectiangle, e.g lt = left top
    lt = pygame.draw.rect(background, white, (0, 0, x/3, x/3))
    mt = pygame.draw.rect(background, white, (x/3 +1, 0, x/3, x/3))
    rt = pygame.draw.rect(background, white, (x/3*2 + 2 ,0, x/3, x/3))
    ml = pygame.draw.rect(background, white, (0,  x/3 +1, x/3, x/3))
    mm = pygame.draw.rect(background, white, (x/3 +1, x/3 +1, x/3, x/3))
    mr = pygame.draw.rect(background, white, (x/3*2 + 2, x/3 +1, x/3, x/3))
    dl = pygame.draw.rect(background, white, (0,  x/3*2 +2, x/3, x/3))
    dm = pygame.draw.rect(background, white, (x/3 +1,  x/3*2 +2, x/3, x/3))
    dr = pygame.draw.rect(background, white, (x/3*2 + 2,  x/3*2 +2, x/3, x/3))
    list_rect = [lt,mt,rt,ml,mm,mr,dl,dm,dr]
    # def draw_item(self, position):

cross = pygame.Rect(200, 100, 161, 100)
circle = pygame.Rect(200, 100, 161, 100)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0,0,0))
            for rect in CrissCross.list_rect:
                if pygame.Rect.collidepoint(rect, pygame.mouse.get_pos()) == True:
                    cross.center = rect.center
                    pygame.draw.rect(background, (0, 100, 255), cross, 2)
                    pygame.display.flip()
                    new_list = CrissCross.list_rect
                    new_list.remove(rect)
            pos = (random.randint(0,x), random.randint(0,x))
            for rect in new_list:
                if pygame.Rect.collidepoint(rect, pos) == True:
                    circle.center = rect.center
                    pygame.draw.rect(background, (0, 0, 0), circle, 2)
                    pygame.display.flip()
                    new_list.remove(rect)
    screen.blit(background, (0, 0))
    pygame.display.flip()