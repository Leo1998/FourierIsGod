import pygame
import math

def draw_arrow(screen, start, end, color, width=1, head=10):
  pygame.draw.line(screen,color,start,end,width)
  rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
  pygame.draw.polygon(screen, color, ((end[0]+head*math.sin(math.radians(rotation)), end[1]+head*math.cos(math.radians(rotation))), (end[0]+head*math.sin(math.radians(rotation-120)), end[1]+head*math.cos(math.radians(rotation-120))), (end[0]+head*math.sin(math.radians(rotation+120)), end[1]+head*math.cos(math.radians(rotation+120)))))


def drawComplex(screen, base, num, color):
  draw_arrow(screen, (base.real, base.imag), (base.real+num.real, base.real+num.imag), color, 2, 8)

def fromPolar(r, phi):
  return r * (math.cos(phi) + math.sin(phi)*1j)
  

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PI = 3.141592653589793

t = 0.0
while True:
    dt = clock.tick(FPS) / 1000
    t += dt
    #while t >= 1.0:
    #  t -= 1.0

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          quit()

    c = fromPolar(50, 1 * 2 * PI * t)
    
    drawComplex(screen, complex(100, 100), c, WHITE)
    pygame.display.update()
