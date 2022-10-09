import pygame
import sys
from ai import choice_ai
from game_items import *

def main():
    pygame.init()
    list_rect, map, counter = initialize_background()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if is_winning(map, 1) == True:
                message_screen("Congratulations, you won!")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    list_rect, map, counter = initialize_background()
            elif is_winning(map, -1) == True:
                message_screen("You can't even beat the simplest AI")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    list_rect, map, counter = initialize_background()
            elif counter == 9:
                message_screen("You can't even beat the simplest AI")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    list_rect, map, counter = initialize_background()
            elif counter < 9:
                try:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if (counter%2)==0:
                            for rect in list_rect:
                                if pygame.Rect.collidepoint(rect, pygame.mouse.get_pos()):
                                    counter += 1
                                    draw_cross(rect.center)
                                    change_field_value(rect, map, 1)
                                    empty_fields_list = list_rect
                                    empty_fields_list.remove(rect)
                                    random_rect = choice_ai(map, empty_fields_list)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if (counter%2)!=0:
                            for rect in empty_fields_list:
                                if pygame.Rect.colliderect(rect, random_rect):
                                    counter += 1
                                    draw_circle(rect.center)
                                    change_field_value(rect, map, -1)
                                    empty_fields_list.remove(rect)
                except:
                    break   
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()