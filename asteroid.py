import random 
import pygame 
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       

    def draw(self, surface):
        pygame.draw.circle(surface, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid_1.velocity = self.velocity.rotate(new_angle)
        asteroid_1.velocity *= 1.2 #speed up
        asteroid_2.velocity = self.velocity.rotate(-new_angle)
        asteroid_2.velocity *= 1.2 #speed up

