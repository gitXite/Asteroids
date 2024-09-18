import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)


    def draw(self, screen):
        pass


    def update(self, dt):
        pass


    def check_for_collisions(self, CircleShape):
        distance = pygame.math.Vector2.distance_to(self.position, CircleShape.position)
        if distance <= self.radius:
            return True
        return False