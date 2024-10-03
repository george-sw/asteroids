from constants import *
from circleshape import *

class Shot(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    # self.velocity = pg.Vector2()
  
  def draw(self, screen):
    pg.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt