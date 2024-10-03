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

  # Extending the project
    # You've done all the required steps, but if you'd like to make the project your own, here are some ideas:

    # Add a scoring system
    # Implement multiple lives and respawning
    # Add an explosion effect for the asteroids
    # Add acceleration to the player movement
    # Make the objects wrap around the screen instead of disappearing
    # Add a background image
    # Create different weapon types
    # Make the asteroids lumpy instead of perfectly round
    # Make the ship have a triangular hit box instead of a circular one
    # Add a shield power-up
    # Add a speed power-up
    # Add bombs that can be dropped


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
          game_object.split()
          shot_object.kill()
    for game_object in drawable:
      game_object.draw(screen)
    pg.display.flip()
    delta_time = clock.tick(60) / 1000

if __name__ == "__main__": 
  main()
