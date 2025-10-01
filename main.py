import os
os.environ["SDL_AUDIODRIVER"] = "dummy"
import pygame
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for asset in drawable:
            asset.draw(screen)
        updatable.update(dt)

        asteroid_collisions = []
        for obj in asteroids:
            if obj.collides_with(player):
                print("Game over!")
                return
            for obj2 in asteroids:
                if obj2 != obj and obj2.collides_with(obj) and obj2 not in asteroid_collisions:
                    obj.bounce(obj2)
                    asteroid_collisions.append(obj2)

        for obj in shots:
            for obj2 in asteroids:
                if obj2.collides_with(obj):
                    obj.kill()
                    obj2.split()
                    break
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
