import pygame
import random
import sys
from pygame.locals import*
from ship import *
#loading pygame
pygame.init()
#displays info onto screen
screen_info=pygame.display.Info()

#setting up the size of the window
size = (width,height)=(int(screen_info.current_w),
int(screen_info.current_h))

screen= pygame.display.set_mode(size)

#Clock 
clock = pygame.time.Clock()

level_total = 4
current_level= 1
asteroid_count = 3
Player = Ship((20,200))
def main():
  while current_level<=level_total:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT: 
        sys.exit()
      if event.type==pygame.KEYDOWN: #if any key is pressed
        if event.key==pygame.K_RIGHT:
          Player.speed[0]=10
        if event.key==pygame.K_LEFT:
          Player.speed[0]=-10
        if event.key==pygame.K_UP:
          Player.speed[1]=-10
        if event.key==pygame.K_DOWN:
          Player.speed[1]=10
      if event.type == pygame.KEYUP:
        if event.key==pygame.K_RIGHT:
          Player.speed[0]=0
        if event.key==pygame.K_LEFT:
          Player.speed[0]=0
        if event.key==pygame.K_UP:
          Player.speed[1]=0
        if event.key==pygame.K_DOWN:
          Player.speed[1]=0
    screen.fill((0,0,100))  
    screen.blit(Player.image,Player.rect)
    pygame.display.flip()
    Player.update()

if __name__=="__main__":
  main()