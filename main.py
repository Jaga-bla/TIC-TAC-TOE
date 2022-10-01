import pygame
import sys 

class XO:
    cross = pygame.image.load('cross.png')
    circle = pygame.image.load('circle.png')
    DEFAULT_IMAGE_SIZE = (50, 50)
    cross = pygame.transform.scale(cross, DEFAULT_IMAGE_SIZE)
    circle = pygame.transform.scale(circle, DEFAULT_IMAGE_SIZE)

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    bg = pygame.image.load('background.png')
    x = XO.cross
    o = XO.circle
    screen.blit(bg, (0, 0))
    pygame.display.flip()
    counter = 0
    while 1:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (counter % 2) == 0:
                    counter += 1
                    screen.blit(o, (pos))
                    pygame.display.flip()
                else:
                    counter +=1
                    screen.blit(x, (pos))
                    pygame.display.flip()

if __name__ == "__main__":
    main()