from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import numpy as np

# MATRICES
def Model():
    #world matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def View():
    #cam position
    gluLookAt(  0.,0.,5.,
                0.,0.,0.,
                0.,1.,0.)

def Projection():
    #projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1., 1., -1., 1., 1., 10.)

def Screen(w : int,  h :int):
    # screen matrix
    glViewport(0,0, w, h)

def ReflectionY():
    glLoadIdentity()
    glScale(-1.,1.,1.)

def ReflectionX():
    glLoadIdentity()
    glScale(1.,-1.,1.)

def Cisalhamento():
    glLoadIdentity()
    glRotate(135,0,0,1)
    glScale(radians(tan(30)),1,1)

def Cisalhamento2():
    glLoadIdentity()
    a = radians(tan(30))
    glMultMatrixf(( 1., a , 0., 0.,
                    0 , 1., 0., 0.,
                    0., 0., 1., 0.,
                    0., 0., 0., 1.))

# DRAW FUNCTIONS
def Square():
    points =(
            (0.,  0., 0.),
            (0.,  0.5,  0.),
            (0.5,  0.5,  0.),
            (0.5,  0.,  0.)
    )
    return points

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Model()
    glPointSize(5)
    glLineWidth(2)

    s1 = Square()
    
    # PLOT SQUARE 1
    c= 0
    
    glBegin(GL_QUADS)
    for p in s1:
        glColor3f(1.,c,c)
        glVertex3f( p[0],
                    p[1],
                    p[2])
        c+=.4
    glEnd()
    
    
    glFlush()

# CALLBACK FUNCTIONS
def keyboard(key, x, y):
    pass


def main():
    
    # INIT
    glutInit()
    glutInitWindowSize(600,600)
    glutInitWindowPosition(1500,100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("Aula 8 - Ex2")
    glClearColor(0.5, 0.0, 0.0, 1.0)

    #CALLBACK FUNTIONS
    glutDisplayFunc( draw )
    glutReshapeFunc( Screen )
    glutKeyboardFunc( keyboard )
    glutMainLoop()

if __name__ == "__main__":
    main()