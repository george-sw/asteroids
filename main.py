import sys
import pygame
from constants import *

def main():
  print(sys.prefix != sys.base_prefix, sys.prefix, sys.base_prefix)
  print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
  pygame.init()
  is_pygame_init = pygame.get_init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  running = True
  clock = pygame.time.Clock()
  delta_time = 0
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("black")
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000

if __name__ == "__main__": 
  main()
