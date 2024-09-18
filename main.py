import pygame
from constants import *
from player import *
from asteroidfield import *


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Instantiate a player object
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip() # Updates the screen after each iteration
        dt = clock.tick(60) / 1000 # ticks at 60hz, converts delta time from ms to sec
    

if __name__ == "__main__":
    main()