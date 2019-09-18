import pygame
import math

PI = 3.141592653589793

def draw_arrow(screen, start, end, color, width=1, head=10):
  pygame.draw.line(screen,color,start,end,width)
  rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
  pygame.draw.polygon(screen, color, ((end[0]+head*math.sin(math.radians(rotation)), end[1]+head*math.cos(math.radians(rotation))), (end[0]+head*math.sin(math.radians(rotation-120)), end[1]+head*math.cos(math.radians(rotation-120))), (end[0]+head*math.sin(math.radians(rotation+120)), end[1]+head*math.cos(math.radians(rotation+120)))))


def drawComplex(screen, base, num, color):
  draw_arrow(screen, (base.real, base.imag), (base.real+num.real, base.imag+num.imag), color, 2, 4)

def fromPolar(r, phi):
  return r * (math.cos(phi) + math.sin(phi)*1j)
  

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

WINDOW_SIZE = (720, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

root = complex(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)

t = 0.0
while True:
    dt = clock.tick(FPS) / 1000
    t += dt*0.1

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit()

    p = root
    for i in range(-3, 3):
      c = fromPolar(25.0, i * 2 * PI * t)
      #print(c)
      drawComplex(screen, p, c, WHITE)
      p += c
    
    pygame.display.update()

print("Exited!")