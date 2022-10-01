import pygame
import sys 

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    bg = pygame.image.load('background.png')
    cross = pygame.image.load('cross.png')
    screen.blit(bg, (0, 0))
    pygame.display.flip()
    while 1:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(cross, (pos))
                pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONUP:
                pass


if __name__ == "__main__":
    main()