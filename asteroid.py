import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        self.score = 0
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.score += SCORE
            return
            
        random_angle = random.uniform(20, 50)
        vector1 = pygame.Vector2.rotate(self.velocity, random_angle)
        vector2 = pygame.Vector2.rotate(self.velocity, -random_angle)
        self.radius -= ASTEROID_MIN_RADIUS
        split_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        split_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
        split_asteroid1.velocity = vector1 * 1.5
        split_asteroid2.velocity = vector2 * 1.5

