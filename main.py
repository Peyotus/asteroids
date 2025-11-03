import pygame
import player
import asteroid
import asteroidfield
import shot
from constants import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    plyr_obj = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    roids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (roids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    big_roids = asteroidfield.AsteroidField()

    shooties = pygame.sprite.Group()
    shot.Shot.containers = (shooties, updatable, drawable)

    state = 1
    while state > 0:
        updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect=None, special_flags=0)
        for draws in drawable:
            draws.draw(screen)
        for roid in roids:
            for bullet in shooties:
                if roid.check_collision(bullet):
                    bullet.kill()
                    roid.split()
            if roid.check_collision(plyr_obj):
                print("Game over!")
                return
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
