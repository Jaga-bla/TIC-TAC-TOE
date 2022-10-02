import pygame
import sys
pygame.init()

x = 600
screen = pygame.display.set_mode((x, x))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
white = (220,220,220)

class XO:
    cross = pygame.image.load('cross.png')
    circle = pygame.image.load('circle.png')
    DEFAULT_IMAGE_SIZE = (50, 50)
    cross = pygame.transform.scale(cross, DEFAULT_IMAGE_SIZE)
    circle = pygame.transform.scale(circle, DEFAULT_IMAGE_SIZE)
    def draw_x(self, screen):
        pos = pygame.mouse.get_pos()
        screen.blit(self.cross, (pos))
        pygame.display.flip()
    def draw_o(self, screen):
        pos = pygame.mouse.get_pos()
        screen.blit(self.circle, (pos))
        pygame.display.flip()

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
        
x = XO
while 1:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect in CrissCross().list_rect:
                    if pygame.Rect.collidepoint(rect, pygame.mouse.get_pos()):
                        x.draw_x(x, background)

    screen.blit(background, (0, 0))
    pygame.display.flip()