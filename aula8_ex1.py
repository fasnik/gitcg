from OpenGL.GL import *
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
    pass

def Projection():
    #projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

def Screen(w : int,  h :int):
    # screen matrix
    glViewport(0,0, w, h)

# DRAW FUNCTIONS
def ControlPoints():
    points =(
            (0.,  0.,  0.),
            (0.,  0.5,  0.),
            (0.5,  0.5,  0.),
            (0.2,  -0.8,  0.),
            (-0.2,  0.8,  0.)
    )
    return points

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Model()
    glPointSize(5)
    glLineWidth(2)
    glColor3f(1.,1.,1.)

    u = np.arange (0, 1.01, 0.01) # parametro u no intevalo [0,1] com passo 0.1
    points = ControlPoints()

    # glMap1f: gera objetos unidimensionais
    
    # PARAMETROS
    # glEnum target: GL_MAP1_VERTEX_3 (ou GL_MAP1_VERTEX_4 para coord homogeneas) 
    # GLfloat u1: inicio do intervalo de u : 0
    # GLfloat u2: final do intervalo de u  : 1
    # GLint stride: quantidade de coordenadas geradas xxx
    # GLint order: quantidade de pontos de controle xxx
    # const * GLfloat points: array com os pontos de controle
    
    glMap1f(GL_MAP1_VERTEX_3, 0., 1., points)
    glEnable(GL_MAP1_VERTEX_3)
    
    glBegin(GL_LINE_STRIP)
    for i in u:
        # glEval1f: gera objetos unidimensionais
    
        # PARAMETROS
        # GLfloat u 
        glEvalCoord1f(i)
    glEnd()

    glColor3f(1.,1.,0.)
    glBegin(GL_POINTS)
    for p in points:
        glVertex3f( p[0],
                    p[1],
                    p[2])
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
    glutCreateWindow("Aula 8 - Ex1")
    glClearColor(0.5, 0.0, 0.0, 1.0)

    #CALLBACK FUNTIONS
    glutDisplayFunc( draw )
    glutReshapeFunc( Screen )
    glutKeyboardFunc( keyboard )
    glutMainLoop()

if __name__ == "__main__":
    main()