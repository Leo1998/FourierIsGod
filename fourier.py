import pygame
import math
import random

PI = 3.141592653589793

def draw_arrow(screen, start, end, color, width=1, head=10):
  pygame.draw.line(screen,color,start,end,width)
  rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
  pygame.draw.polygon(screen, color, ((end[0]+head*math.sin(math.radians(rotation)), end[1]+head*math.cos(math.radians(rotation))), (end[0]+head*math.sin(math.radians(rotation-120)), end[1]+head*math.cos(math.radians(rotation-120))), (end[0]+head*math.sin(math.radians(rotation+120)), end[1]+head*math.cos(math.radians(rotation+120)))))


def drawComplex(screen, base, num, color):
  draw_arrow(screen, (base.real, base.imag), (base.real+num.real, base.imag+num.imag), color, 2, 4)

def polar(r, phi):
  return r * (math.cos(phi) + math.sin(phi)*1j)
  
def approximateCs(count, func, integration_steps=100):
  cs = []
  halfcount = int(count/2)

  for i in range(-halfcount, halfcount+1):
    integ = complex(0.0, 0.0)
    deltaT = 1.0 / integration_steps
    for j in range(integration_steps):
      integ += deltaT * func(j * deltaT) * polar(1.0, -i * 2 * PI * (j * deltaT))
    cs.append((i, integ))
  return cs

def example1(t):
  return polar(40*math.sin(2*PI*t)+50, 2 * PI * t)

def main():
  successes, failures = pygame.init()
  print("{0} successes and {1} failures".format(successes, failures))

  WINDOW_SIZE = (720, 720)
  screen = pygame.display.set_mode(WINDOW_SIZE)
  clock = pygame.time.Clock()
  FPS = 60  # Frames per second.

  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)

  root = complex(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)

  cs = approximateCs(30, example1)

  timescale=0.1
  t = 0.0
  while True:
    dt = clock.tick(FPS) / 1000
    if t < 1.0:
      t += dt*timescale

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            t = 0
          elif event.key == pygame.K_ESCAPE:
            quit()

    p = root
    for (i, c) in cs:
      n = c * polar(1.0, i * 2 * PI * t)
      drawComplex(screen, p, n, WHITE)
      p += n
    
    pygame.display.update()

  print("Exited!")

if __name__ == '__main__':
  main()
