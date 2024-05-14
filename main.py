import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from terrain_gen import generate_perlin_noise

def init_pygame_opengl(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    gluPerspective(60, (width / height), 0.1, 100.0)
    glTranslatef(0.0, -1.5, -10)
    glRotatef(25, 1, 0, 0)

def get_color(height):
    if height < 0.3:
        return 0.0, 0.5, 0.0  # gruen
    elif height < 0.6:
        return 0.4, 0.26, 0.13  # braun
    else:
        return 1.0, 1.0, 1.0  # weiss (for peaks)

def draw_terrain(terrain):
    glBegin(GL_QUADS)
    size = terrain.shape[0]
    for x in range(size - 1):
        for y in range(size - 1):
            h1 = terrain[x][y]
            h2 = terrain[x][y + 1]
            h3 = terrain[x + 1][y + 1]
            h4 = terrain[x + 1][y]
            glColor3fv(get_color(h1))
            glVertex3f(x / 10, y / 10, h1)
            glColor3fv(get_color(h2))
            glVertex3f(x / 10, (y + 1) / 10, h2)
            glColor3fv(get_color(h3))
            glVertex3f((x + 1) / 10, (y + 1) / 10, h3)
            glColor3fv(get_color(h4))
            glVertex3f((x + 1) / 10, y / 10, h4)
    glEnd()

def main():
    width, height = 800, 600
    init_pygame_opengl(width, height)
    
    size = 100
    scale = 50.0
    octaves = 6
    seed = np.random.randint(0, 100)
    
    terrain = generate_perlin_noise(size, scale, octaves, seed)
    
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_terrain(terrain)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
