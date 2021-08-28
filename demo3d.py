#!/usr/bin/env python3
import math
import pyglet
from pyglet.gl import *

PI = 3.141592653589793

window = pyglet.window.Window()

def example3d(t):
  rad = 5
  height = 14
  f = 4

  x = rad * math.sin(2 * PI * f * t)
  y = height * t
  z = rad * math.cos(2 * PI * f * t)
  return [x, y, z]

path = []
t = 0
timescale = 0.1

@window.event
def on_draw():
  glClearColor(0, 0, 0, 0)
  glClear(GL_COLOR_BUFFER_BIT)

  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(90, 1, 0.1, 100)

  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  glTranslatef(0, 0, -20)
  glRotatef(0, 0, 1, 0)


  glBegin(GL_LINE_STRIP)
  for pos in path:
    glVertex3f(*pos)
  glEnd()

def update(dt):
  global t
  global path

  path.append(example3d(t))
  t += dt * timescale
  if t > 1.0:
    path = []
    t = 0



if __name__ == '__main__':
  pyglet.clock.schedule_interval(update, 1/60.0)
  pyglet.app.run()
