import pygame
import player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    plyr_obj = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    state = 1
    clock = pygame.time.Clock()
    dt = 0
    while state > 0:
        plyr_obj.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("red", rect=None, special_flags=0)
        plyr_obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
