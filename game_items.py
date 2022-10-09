import pygame

x = 600 #side lenght of the screen square
y = x/3 #side lenght of the field square

#create the background for all the components
screen = pygame.display.set_mode((x, x))
background = pygame.Surface(screen.get_size())
background = background.convert()

def draw_rect(i:int,j:int)->pygame.Rect:
    color = (220,220,220)
    position = ((y+5)*i,(y+5)*j)
    size = (y,y)
    rect = pygame.draw.rect(background, color, (position,size))
    return rect

def fields_list() -> list:
    list_rect = []
    for i in range(3):
        for j in range(3):
            rect = draw_rect(i,j)
            list_rect.append(rect)
    return list_rect

def add_field_value() -> list:
    map = []
    for i in range(3):
        for j in range(3):
            rect = draw_rect(i,j)
            map.append([rect, 0])
    return map

def change_field_value(rect:pygame.Rect, map:list, n:int):
    for i in map:
        if i[0] == rect:
            i[1] = n

def is_winning(map:list, n:int)->bool:
    #vertical win possibilities
    for j in range(0,7,3):
        if map[0+j][1] ==2 and map[1+j][1]==2 and map[2+j][1] ==2:
            return True
    #horizontal win possibilities
    for j in range(3):
        if map[0+j][1] ==n and map[3+j][1]==n and map[6+j][1] ==n:
            return True
    #diagonal win possibilities
    for j in range(0,3,2):
        if map[0+j][1] ==n and map[4][1]==n and map[8-j][1] ==n:
            return True
        
def draw_cross(center_point:tuple)-> pygame.Rect:
    list_of_points = [[center_point[0]-45,center_point[1]-45], 
    center_point, 
    [center_point[0]-45, center_point[1]+45], 
    center_point, 
    [center_point[0]+45, center_point[1]-45],
    center_point, 
    [center_point[0]+45, center_point[1]+45]]
    color = (0,0,0)
    joint_end_points = False
    line_thickness = 8
    cross = pygame.draw.lines(background, color, joint_end_points, list_of_points, line_thickness)
    return cross

def draw_circle(center_point:tuple)->pygame.Rect:
    pygame.draw.circle(background, (0,0,0), center_point, 45, 7)

def initialize_background()->[list,list, int]:
    background.fill((0, 0, 0))
    list_rect = fields_list()
    map = add_field_value()
    counter = 0
    return list_rect, map, counter 

def message_screen(text:str) -> pygame:
    background.fill((220,220,220))
    color = (0,0,0)
    text = pygame.font.Font.render(pygame.font.SysFont("Dyuthi", 42), text, True, color)
    background.blit(text, (50, x/2))