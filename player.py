
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0

  # in the player class
  def triangle(self):
    forward = pg.Vector2(0, 1).rotate(self.rotation)
    right = pg.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  
  def draw(self, screen):
    pg.draw.polygon(screen, "white", self.triangle(), 2)

  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt):
    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
      self.rotation -= PLAYER_TURN_SPEED * dt
    if keys[pg.K_d]:
      self.rotate(dt)
    if keys[pg.K_w]:
      self.move(dt)
    if keys[pg.K_s]:
      self.move(-dt)
    if keys[pg.K_SPACE]:
      self.shoot(dt)
  def move(self, dt):
    forward = pg.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def shoot(self, dt):
    shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
    # shot.velocity = pg.Vector2(0, 1).rotate(self.rotation)
    # shot.position += shot.velocity * PLAYER_SHOT_SPEED * dt
    # velocity = pg.Vector2(0, 1).rotate(self.rotation)
    # shot.position += velocity * PLAYER_SHOT_SPEED * dt
    velocity = pg.Vector2(0, 1).rotate(self.rotation)
    shot.velocity += velocity * PLAYER_SHOT_SPEED