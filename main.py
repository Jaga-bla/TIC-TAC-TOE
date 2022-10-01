import pygame
import sys 

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

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    bg = pygame.image.load('background.png')
    x = XO
    o = XO
    screen.blit(bg, (0, 0))
    pygame.display.flip()
    counter = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if counter == 9:
                    counter = 0
                    screen.blit(bg, (0, 0))
                    pygame.display.flip()
                if (counter % 2) == 0:
                    counter += 1
                    o.draw_o(o, screen)
                else:
                    counter +=1
                    x.draw_x(x, screen)

if __name__ == "__main__":
    main()