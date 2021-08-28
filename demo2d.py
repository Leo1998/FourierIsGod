#!/usr/bin/env python3
import pygame
import math
import random

from fourier import *

PI = 3.141592653589793

def drawArrow(screen, start, end, color, width=1, head=10):
  pygame.draw.line(screen,color,start,end,width)
  if head > 0:
    rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
    pygame.draw.polygon(screen, color, 
          ((end[0]+head*math.sin(math.radians(rotation)), 
          end[1]+head*math.cos(math.radians(rotation))), 
          (end[0]+head*math.sin(math.radians(rotation-120)), 
          end[1]+head*math.cos(math.radians(rotation-120))), 
          (end[0]+head*math.sin(math.radians(rotation+120)), 
          end[1]+head*math.cos(math.radians(rotation+120)))))


def drawComplex(screen, base, num, color):
  drawArrow(screen, (base.real, base.imag), (base.real+num.real, base.imag+num.imag), color, 2, 4)

WINDOW_SIZE = (720, 720)
TIMESCALE=0.1

def main():
  successes, failures = pygame.init()
  print("{0} successes and {1} failures".format(successes, failures))

  screen = pygame.display.set_mode(WINDOW_SIZE)
  clock = pygame.time.Clock()
  FPS = 60  # Frames per second.

  center = complex(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)

  coefficients = approximateCoefficients(200, example1, 500)

  t = 0.0
  path = []
  while True:
    dt = clock.tick(FPS) / 1000
    t += dt * TIMESCALE

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            path = []
            t = 0
          elif event.key == pygame.K_ESCAPE:
            quit()

    #draw path/arrows
    p = center
    for (freq, coef) in coefficients:
      n = coef * polar(1.0, freq * 2 * PI * t)
      drawComplex(screen, p, n, (0,255,255))
      p += n

    path.append(p)
    if len(path) >= 2:
      for i in range(len(path)-1):
        pygame.draw.line(screen, (0,255,0), (path[i].real, path[i].imag), (path[i+1].real, path[i+1].imag), 3)
    
    pygame.display.update()

  print("Exited!")

if __name__ == '__main__':
  main()
