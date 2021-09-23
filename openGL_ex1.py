from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

# MATRICES
def Model():
    #world matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(-0.5, -0.5, 0)

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

# DRAW FUNTIONS
def line(x0:float, y0:float, x1:float, y1:float, lineWidth:float = 2.):
    glLineWidth(lineWidth)
    glBegin(GL_LINES)
    glVertex2f(x0,y0)
    glVertex2f(x1,y1)
    glEnd()

def draw_vertex_array(mode, count, type, indices:list):
    glEnableClientState(GL_VERTEX_ARRAY)
    glDrawElements( mode , count , type , indices ) 
    glDisableClientState(GL_VERTEX_ARRAY)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Model()
    #View()

    vertices =[
        0.0,    0.0,
        0.5,    0.0,
        1.0,    0.0,

        0.0,    0.5,
        0.5,    0.5,
        1.0,    0.5,

        0.0,    1.0,
        0.5,    1.0,
        1.0,    1.0,
    ]

    indices = [
        0,1,3,
        1,4,3,
        1,2,4,
        2,5,4
    ]
    glColor3f(1.,1.,1.)
    glPointSize(10)
    glVertexPointer( 2, GL_FLOAT, 0, vertices)
    glIndexPointerf(indices)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    draw_vertex_array(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glBegin(GL_LINES)
    
    glVertex2f(-1,0)
    glVertex2f(1,0)

    glVertex2f(0,1)
    glVertex2f(0,-1)

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
    glutDisplayFunc( draw )
    glutReshapeFunc( Screen )
    glutKeyboardFunc( keyboard )
    glutMainLoop()

if __name__ == "__main__":
    main()