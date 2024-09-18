import random
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        speed = random.randint(50, 100)
        self.velocity = self.velocity * speed


    def draw(self, screen):
        color = (255, 255, 255) # White color
        position = (self.x, self.y)
        pygame.draw.circle(screen, color, position, self.radius, width=2)


    def update(self, dt):
        delta_position = self.velocity * dt
        self.x += delta_position.x
        self.y += delta_position.y
