import circleshape
import pygame


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, current_screen):
        pygame.draw.circle(current_screen, "white", self.position, self.radius, width=0)

    def update(self, dt):
        self.position += self.velocity * dt






