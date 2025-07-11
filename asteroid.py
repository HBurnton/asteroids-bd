from circleshape import *
from constants import *
from random import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
       super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
           
    def update(self, dt):
           self.position += self.velocity * dt

    def split(self):
         self.kill()
         if self.radius <= ASTEROID_MIN_RADIUS:
              return
         random_angle = uniform(20,50)
         positive_angle = self.velocity.rotate(random_angle)
         negative_angle = self.velocity.rotate(-random_angle)

         new_radius = self.radius - ASTEROID_MIN_RADIUS

         asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
         asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
         asteroid1.velocity = positive_angle * 1.2
         asteroid2.velocity = negative_angle * 1.2
