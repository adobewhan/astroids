from circleshape import CircleShape
import pygame
import random
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        randomAngle = random.uniform(20,50)
        rotatedVelocoty = self.velocity.rotate(randomAngle)
        oppRotatedVelocity = self.velocity.rotate(-randomAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        split1 = Asteroid(self.position[0],self.position[1],newRadius)
        split2 = Asteroid(self.position[0],self.position[1],newRadius)
        split1.velocity = rotatedVelocoty * 1.2
        split2.velocity = oppRotatedVelocity * 1.2