import pygame
import circleshape
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, current_screen):
        pygame.draw.circle(current_screen, "white", self.position, self.radius, width=0)

    def update(self, dt):
        self.position += self.velocity * dt
