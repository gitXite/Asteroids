import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Instantiate a player object
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("\nGame over!")
                print("----------------------------")
                print(f"Your score: {asteroid.score}")
                print("----------------------------")
                sys.exit()
                
            for shot in shots:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.split()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip() # Updates the screen after each iteration
        
        dt = clock.tick(60) / 1000 # ticks at 60hz, converts delta time from ms to sec
    

if __name__ == "__main__":
    main()
