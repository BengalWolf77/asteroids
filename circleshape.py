import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, obj2):
        #if pygame.math.Vector2.distance_to(self.position,obj2.position) <= self.radius + obj2.radius and pygame.math.Vector2.distance_to(self.position,obj2.position) > 0:
        #    breakpoint()
        return pygame.math.Vector2.distance_to(self.position,obj2.position) <= self.radius + obj2.radius
