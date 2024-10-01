import pygame
from constants import *
from player import *

def main():
  # print(sys.prefix != sys.base_prefix, sys.prefix, sys.base_prefix)
  # print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
  pygame.init()
  is_pygame_init = pygame.get_init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  running = True
  clock = pygame.time.Clock()
  delta_time = 0
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    player.update(delta_time)
    player.draw(screen)
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000
    # print(delta_time)

if __name__ == "__main__": 
  main()
