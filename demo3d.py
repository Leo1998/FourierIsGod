import math
import pyglet
from pyglet.gl import *

from fourier import *

window = pyglet.window.Window()


path = []
t = 0
timescale = 0.5

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

  #print(t)
  path.append(example3d(t))
  t += dt * timescale
  if t > 1.0:
    path = []
    t = 0



if __name__ == '__main__':
  pyglet.clock.schedule_interval(update, 1/60.0)
  pyglet.app.run()
