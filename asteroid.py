import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, color=None):
        super().__init__(x, y, radius)
        asteroid_colors = [(255,128,128),(255,255,128),(128,128,255)]
        if color != None:
            self.color = color
        else:
            self.color = random.choice(asteroid_colors)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 0)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_vect = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
        new_vect2 = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
        offset = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x + offset, self.position.y + offset, self.radius - ASTEROID_MIN_RADIUS, self.color)
        child1.velocity = new_vect

        child2 = Asteroid(self.position.x - offset, self.position.y - offset, self.radius - ASTEROID_MIN_RADIUS, self.color)
        child2.velocity = new_vect2

    def bounce(self, asteroid2):
        #breakpoint()
        init_velo = self.velocity

        if pygame.math.Vector2.distance_to(self.position,asteroid2.position) < asteroid2.radius:
            self.split()
            return

        self.velocity = pygame.math.Vector2.reflect(init_velo, asteroid2.velocity) 
        asteroid2.velocity = pygame.math.Vector2.reflect(asteroid2.velocity, init_velo) 
        
        