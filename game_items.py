import pygame

x = 600 #side lenght of the screen square
y = x/3 #side lenght of the field square
screen = pygame.display.set_mode((x, x))
background = pygame.Surface(screen.get_size())
background = background.convert()

def fields_list() -> list:
    list_rect = []
    for i in range(3):
        for j in range(3):
            rect = pygame.draw.rect(background, (220,220,220), ((y+5)*i,(y+5)*j, y, y))
            list_rect.append(rect)
    return list_rect

def add_field_value() -> list:
    map = []
    for i in range(3):
        for j in range(3):
            rect = pygame.draw.rect(background, (220,220,220), ((y+5)*i,(y+5)*j, y, y))
            map.append([rect, 0])
    return map

def change_field_value(rect, map, n):
    for i in map:
        if i[0] == rect:
            i[1] = n

def is_winning(map, n):
    for j in range(0,7,3):
        if map[0+j][1] ==n and map[1+j][1]==n and map[2+j][1] ==n:
            return True
    for j in range(3):
        if map[0+j][1] ==n and map[3+j][1]==n and map[6+j][1] ==n:
            return True
    for j in range(0,3,2):
        if map[0+j][1] ==n and map[4][1]==n and map[8-j][1] ==n:
            return True
        
def draw_cross(center_point):
    pygame.draw.lines(background, (0,0,0), False, 
    [[center_point[0]-45,center_point[1]-45], 
    center_point, 
    [center_point[0]-45, center_point[1]+45], 
    center_point, 
    [center_point[0]+45, center_point[1]-45],
    center_point, 
    [center_point[0]+45, center_point[1]+45]], 8)

def draw_circle(center_point):
    pygame.draw.circle(background, (0,0,0), center_point, 45, 7)

def initialize_background():
    background.fill((0, 0, 0))
    list_rect = fields_list()
    map = add_field_value()
    counter = 0
    return list_rect, map, counter 

def message_screen(text):
    background.fill((220,220,220))
    text = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 42), text, True, (0,0,0))
    background.blit(text, (50, x/2))