import pygame as pg
from constants import *
from player import *

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
  Player.containers = updatable, drawable
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        return
    for game_object in updatable:
      game_object.update(delta_time)
    screen.fill("black")
    for game_object in drawable:
      game_object.draw(screen)
    pg.display.flip()
    delta_time = clock.tick(60) / 1000

if __name__ == "__main__": 
  main()
