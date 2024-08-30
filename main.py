import pygame
from constants import *
from player import *
from circleshape import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    timer = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(('white'))
        player.draw(screen)
        pygame.display.flip
        dt = timer.tick(60) / 1000
        


if __name__ == "__main__":
    main()