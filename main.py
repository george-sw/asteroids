# nvim lesson 2.5
import sys
import pygame as pg
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
  # print(sys.prefix != sys.base_prefix, sys.prefix, sys.base_prefix)
  # print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
  pg.init()
  is_pygame_init = pg.get_init()
  screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  running = True
  clock = pg.time.Clock()
  delta_time = 0

  updatable = pg.sprite.Group()
  drawable = pg.sprite.Group()
  asteroids = pg.sprite.Group()
  shots = pg.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  Shot.containers = (shots, updatable, drawable)


  # Shot.containers = (updatable, drawable)

  # notes on typical game loop structure from Boots

  # while running:
    # Handle events
    # Update game logic
    # Clear the screen
    # Draw all game objects
    # Update the display


  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        return
    for game_object in updatable:
      game_object.update(delta_time)
    screen.fill("black")
    for game_object in asteroids:
      if game_object.is_colliding(player):
        sys.exit("Game Over!")
      for shot_object in shots:
        if game_object.is_colliding(shot_object):
          game_object.kill()
          shot_object.kill()
    for game_object in drawable:
      game_object.draw(screen)
    pg.display.flip()
    delta_time = clock.tick(60) / 1000

if __name__ == "__main__": 
  main()
