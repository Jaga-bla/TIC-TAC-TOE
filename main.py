import pygame
import sys
import random

def create_list(background, y):
    list_rect = []
    for i in range(3):
        for j in range(3):
            rect = pygame.draw.rect(background, (220,220,220), ((y+1)*i,(y+1)*j, y, y))
            list_rect.append(rect)
    return list_rect

def create_map(background, y):
    map = []
    for i in range(3):
        for j in range(3):
            rect = pygame.draw.rect(background, (220,220,220), ((y+1)*i,(y+1)*j, y, y))
            map.append([rect, 0])
    return map

def change_map_value(rect, map):
    for i in map:
        if i[0] == rect:
            i[1] = 1

def is_winning(map):
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

def draw_cross(background, center_point):
    pygame.draw.lines(background, (0,0,0), False, 
    [[center_point[0] -45,center_point[1] -45], 
    center_point, 
    [center_point[0] -45, center_point[1]+45], 
    center_point, 
    [center_point[0] +45, center_point[1]-45],
    center_point, 
    [center_point[0]+45, center_point[1]+45]], 8)

def draw_circle(background, center_point):
    pygame.draw.circle(background, (0,0,0), center_point, 45, 7)

def main():
    pygame.init()
    x = 600
    y = x/3
    screen = pygame.display.set_mode((x, x))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    list_rect = create_list(background, y)
    map = create_map(background, y)
    counter = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if is_winning(map) == True:
                background.fill((220,220,220))
                text = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 42), f'Congratulations, you won!', True, (0,0,0))
                background.blit(text, (x/4, x/4))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    background.fill((0, 0, 0))
                    list_rect = create_list(background, y)
                    map = create_map(background, y)
                    counter = 0
            elif counter == 9:
                background.fill((220,220,220))
                text = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 42), f'Looser', True, (0,0,0))
                background.blit(text, (x/4, x/4))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    background.fill((0, 0, 0))
                    list_rect = create_list(background, y)
                    map = create_map(background, y)
                    counter = 0
            elif counter < 9:
                try:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for rect in list_rect:
                            if pygame.Rect.collidepoint(rect, pygame.mouse.get_pos()):
                                counter += 1
                                center_point = rect.center
                                draw_cross(background, center_point)
                                change_map_value(rect, map)
                                new_list = list_rect
                                new_list.remove(rect)
                                random_rect = random.choice(new_list)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        for rect in new_list:
                            if pygame.Rect.colliderect(rect, random_rect):
                                counter += 1
                                center_point = rect.center
                                draw_circle(background, center_point)
                                new_list.remove(rect)
                except:
                    break
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()