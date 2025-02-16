import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        angle_1 = self.velocity.rotate(angle)
        angle_2 = self.velocity.rotate((-1) * angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

        ast_1.velocity += angle_1 * 1.2
        ast_2.velocity += angle_2 * 1.2
