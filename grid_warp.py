import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()
display = (900, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 1000.0)
glTranslatef(0.0, 0.0, -80)

cols, rows = 50, 50
spacing = 1

def draw_grid(time):
    glBegin(GL_LINES)
    for x in range(cols):
        for y in range(rows):
            z = math.sin(x * 0.3 + time) * 2 + math.cos(y * 0.3 + time) * 2

            # Neon color
            glColor3f(0, 1, 0.7)

            if x < cols - 1:
                z2 = math.sin((x+1)*0.3 + time)*2 + math.cos(y*0.3 + time)*2
                glVertex3f(x - cols/2, y - rows/2, z)
                glVertex3f(x+1 - cols/2, y - rows/2, z2)

            if y < rows - 1:
                z2 = math.sin(x*0.3 + time)*2 + math.cos((y+1)*0.3 + time)*2
                glVertex3f(x - cols/2, y - rows/2, z)
                glVertex3f(x - cols/2, y+1 - rows/2, z2)
    glEnd()

clock = pygame.time.Clock()
time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glRotatef(0.3, 1, 1, 0)  # slow rotation

    draw_grid(time)
    time += 0.05

    pygame.display.flip()
    clock.tick(60)