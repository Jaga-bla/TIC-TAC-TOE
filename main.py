import pygame
import sys
from ai import choice_ai
from game_items import *

def main():
    pygame.init()
    x = 600
    y = x/3
    screen = pygame.display.set_mode((x, x))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    list_rect, map, counter = initialize_background(background, y)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if is_winning(map, 1) == True:
                background.fill((220,220,220))
                text = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 42), 'Congratulations, you won!', True, (0,0,0))
                background.blit(text, (x/6, x/2))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    list_rect, map, counter = initialize_background(background, y)
            elif is_winning(map, -1) == True:
                background.fill((220,220,220))
                text = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 42), 'Your enemy won the game!', True, (0,0,0))
                background.blit(text, (x/6, x/2))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    list_rect, map, counter = initialize_background(background, y)
            elif counter == 9:
                background.fill((220,220,220))
                text = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 42), f'Looser', True, (0,0,0))
                background.blit(text, (x/6, x/2))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    list_rect, map, counter = initialize_background(background, y)
            elif counter < 9:
                try:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (counter%2)==0:
                            for rect in list_rect:
                                if pygame.Rect.collidepoint(rect, pygame.mouse.get_pos()):
                                    counter += 1
                                    draw_cross(background, rect.center)
                                    change_field_value(rect, map, 1)
                                    new_list = list_rect
                                    new_list.remove(rect)
                                    random_rect = choice_ai(map, new_list)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if (counter%2)!=0:
                            for rect in new_list:
                                if pygame.Rect.colliderect(rect, random_rect):
                                    counter += 1
                                    draw_circle(background, rect.center)
                                    change_field_value(rect, map, -1)
                                    new_list.remove(rect)
                except:
                    break   
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()