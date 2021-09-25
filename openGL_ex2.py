from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
import numpy as np

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
def implicitFunc(X :np.array):
    f = X[0]**2 + X[1]**2 + X[2]**2- 1.
    return f

# DRAW FUNTIONS

def drawSphere():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Model()
    glPointSize(1)
    glColor3f(1.,1.,1.)
    
    vertices = [ ]
    x_range = np.arange (-1, 1.1, 0.1)
    y_range = np.arange (-1, 1.1, 0.1)
    z_range = np.arange (-1, 1.1, 0.1)
    for x in x_range:
        for y in y_range:
            for z in z_range:
                if abs(implicitFunc(np.array([x,y,z]))) < 0.1:
                    vertices.append(x)
                    vertices.append(y)
                    vertices.append(z)

    glBegin(GL_POINTS)
    for i in range(0,len(vertices)-1,3):
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
    glutDisplayFunc( drawSphere )
    glutReshapeFunc( Screen )
    glutKeyboardFunc( keyboard )
    glutMainLoop()

if __name__ == "__main__":
    main()