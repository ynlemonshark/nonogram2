import pygame
import sys

pygame.init()
DISPLAY = pygame.display.set_mode((1200, 800))
FPSCLOCK = pygame.time.Clock()


def main():
    DISPLAY.fill((255, 255, 255))
    pygame.draw.rect(DISPLAY, (63, 63, 63), (0, 0, 1200, 800), 5)
    pygame.display.update()

    while True:
        pygame_events = pygame.event.get()
        for pygame_event in pygame_events:
            if pygame_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        FPSCLOCK.tick(10)


if __name__ == '__main__':
    main()