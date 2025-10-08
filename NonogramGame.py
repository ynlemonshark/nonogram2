import pygame
import sys

pygame.init()
DISPLAY = pygame.display.set_mode((1200, 800))
FPSCLOCK = pygame.time.Clock()

title_background = pygame.Surface((1200, 800))
title_background.fill((255, 255, 255))
pygame.draw.rect(title_background, (63, 63, 63), (0, 0, 1200, 800), 5)
title_font = pygame.font.SysFont(None, 140, False, False)
title_text = title_font.render("Nonogram", True, (0, 0, 0))
title_background.blit(title_text, (600 - title_text.get_rect().width / 2, 100))


def main():
    channel = 0

    DISPLAY.fill((255, 255, 255))
    pygame.display.update()

    DISPLAY.blit(title_background, (0, 0))
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