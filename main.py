import pygame
import sys
from ai import choice_ai

# + za typowanie, polecam używać go wszędzie
def fields_list(background, y) -> list:
    # w pythonie możesz inicjalizować listy w specjalny sposób (https://www.w3schools.com/python/python_lists_comprehension.asp)
    # ten jest też jak najbardziej poprawny
    list_rect = []
    for i in range(3):
        for j in range(3):
            # wszystkie funkcje z pygame mogłabyś zastąpić własnymi funkcjami, 
            # dzięki temu nie będziesz musiała się powtarzać przy przekazywaniu zmiennych, 
            # które się nie zmieniają w gruncie rzeczy (jak, `(220,220,220)` czy to wymnażanie współrzędnych)
            # np. 
            # def draw_rect(background, x, y):
            #   return pygame.draw.rect(background, (220,220,220), ((y+5)*i,(y+5)*j, y, y))
            rect = pygame.draw.rect(background, (220,220,220), ((y+5)*i,(y+5)*j, y, y))
            list_rect.append(rect)
    return list_rect

# zmieniłbym nazwę metody, żeby lepiej oddawała to, co robi
def add_field_value(background, y) -> list:
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
        
def draw_cross(background, center_point):
    # jeśli masz aż tak skomplikowane wywołanie funkcji, przypisz poszczególne argumenty do zmiennych
    # aby łatwiej się czytało
    pygame.draw.lines(background, (0,0,0), False, 
    [[center_point[0]-45,center_point[1]-45], 
    center_point, 
    [center_point[0]-45, center_point[1]+45], 
    center_point, 
    [center_point[0]+45, center_point[1]-45],
    center_point, 
    [center_point[0]+45, center_point[1]+45]], 8)

# + za zastąpienie funkcji z pygame własną - dużo prostszą, o to chodzi
def draw_circle(background, center_point):
    pygame.draw.circle(background, (0,0,0), center_point, 45, 7)

# y to w zasadzie height, prawda? zmieniłbym nazwę
# jeśli y się nie zmienia, to nawet zaryzykowałbym zmienną globalną, albo klasę ze zmienną statyczną,
# ponieważ 3 razy używasz parametru y, który wynosi tyle samo - bo musi. Ogólnie to prawidłowo, ale zamknąłbym te 3 funkcje w jednej klasie
# albo w jednym pliku, żeby mogły dzielić ze sobą informację o wysokości
def initialize_background(background, y):
    background.fill((0, 0, 0))
    list_rect = fields_list(background, y)
    map = add_field_value(background, y)
    counter = 0
    return list_rect, map, counter 

# ta funkcja jest zdecydowanie za duża, podzieliłbym ją na mniejsze
def main():
    pygame.init()
    x = 600
    y = x/3
    screen = pygame.display.set_mode((x, x))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    list_rect, map, counter = initialize_background(background, y)
    # jako ciekawostkę polecam dodać ograniczenie FPS, żeby pętla nie zużywała 100% procesora
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if is_winning(map, 1) == True:
                # ciało tych ifów się powtarza, a więc to idealny kandydat na funkcję
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

# w plikach `main.py` polecam trzymać tylko te dwie linijki niżej. 
# Każdy plik ma swoją rolę, a rolą tego jest odpalić program, cała reszta mogłaby być gdzie indziej
if __name__ == '__main__':
    main()