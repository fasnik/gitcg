from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
import numpy as np


def Bernstein(n, i ,t):
    J = comb(n,i)*t**i(1-t)**(n-1)
    return J

def Bezier(ControlPoints: list, t):
    n = len(ControlPoints)
    P = 0
    i = 0
    for ControlPoint in ControlPoints:
        P+= ControlPoint*Bernstein(n,i, t)
        i+=1
    return P


## 
# MATRICES
def Model():
    #world matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # glTranslate(-0.5, -0.5, 0)
    glScale(1./2,1./2,1./2)

def View():
    #cam position
    pass

def Projection():
    #projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

def Screen(w : int,  h :int):
    # screen matrix
    glViewport(0,0, w, h)

#MT functions
def paramFunc(t :float):
    x = cos(2*pi*t)
    y = sin(2*pi*t)
    f = np.array([x,y])
    return f

# DRAW FUNTIONS

def drawCircle():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Model()
    glPointSize(1)
    glColor3f(1.,1.,1.)
    
    vertices = [ ]
    t_range = np.arange (-1, 1.1, 0.01)
    for t in t_range:
        f = paramFunc(t)
        vertices.append(f[0])
        vertices.append(f[1])
        vertices.append(0)

    glBegin(GL_LINE_STRIP)
    for i in range(0,len(vertices)-1,3):
        glColor3f(1.,1.,1.)
        glVertex3f( vertices[i], 
                    vertices[i+1],
                    vertices[i+2])
    glEnd()

    glFlush()

def keyboard(key, x, y):
    pass

def main():
    
    # INIT
    glutInit()
    glutInitWindowSize(600,600)
    glutInitWindowPosition(1500,100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("OpenGl- Ex1")
    glClearColor(0.5, 0.0, 0.0, 1.0)
    
    # CALLBACK FUNTIONS
    glutDisplayFunc( drawCircle )
    glutReshapeFunc( Screen )
    glutKeyboardFunc( keyboard )
    glutMainLoop()

if __name__ == "__main__":
    main()