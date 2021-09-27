from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import numpy as np

# MATRICES

eyeX = 1. 
eyeY = 0.
eyeZ = 1.

def Model():
    #world matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScale(0.6,0.6,0.6)
    glTranslate(0.8, 0, 0)

def View():
    #cam position
    gluLookAt(  eyeX, eyeY, eyeZ,
                0,    0,    0,
                0,    1,    0)


def Projection():
    #projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

def Screen(w : int,  h :int):
    # screen matrix
    glViewport(0,0, w, h)

#MT functions
def paramFunc(u :float, v :float ):
    R = 1
    x = R*cos(u)
    y = R*sin(u)
    z = v
    f = (x,y,z)
    return f

# DRAW FUNTIONS

def draw_vertex_array(mode, count, type, indices:list):
    glEnableClientState(GL_VERTEX_ARRAY)
    glDrawElements( mode , count , type , indices ) 
    glDisableClientState(GL_VERTEX_ARRAY)

def drawCilinder():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Model()
    View()
    glPointSize(5)
    glColor3f(1.,1.,1.)
    
    vertices = []
    u = np.arange (0, 2*pi+pi/16, pi/16) #[0, pi ,2pi]
    v = np.arange (0, 2+1, 1) #[0, 1 ,2]
    
    indices = [  ]
    for i in range(len(u)-1):
        for j in range(len(v)-1):
            
            indices.append(j+len(v)*i)
            indices.append((j+1)+len(v)*i)
            indices.append((j+1)+len(v)*(i+1))
            
            indices.append((j+1)+len(v)*(i+1))
            indices.append(j+len(v)*(i+1))
            indices.append(j+len(v)*i)
    for i in u:
        for j in v:
            #  
            P = paramFunc(i,j) 
            print(P) 
            vertices.append(P[0])
            vertices.append(P[1])
            vertices.append(P[2])

    glVertexPointer( 3, GL_FLOAT, 0, vertices)
    glIndexPointerf(indices)
  
    glPolygonMode(GL_BACK,GL_LINE)
    
    #triangulos
    draw_vertex_array(  GL_TRIANGLES, 
                        len(indices), 
                        GL_UNSIGNED_INT, 
                        indices)
    
   
    glFlush()

def keyboard(key, x, y):
    if key == 'q':
        global eyeX
        eyeX+=1
        glutPostRedisplay()

def main():
    
    # INIT
    glutInit()
    glutInitWindowSize(600,600)
    glutInitWindowPosition(1500,100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("OpenGl- Ex1")
    glClearColor(0.5, 0.0, 0.0, 1.0)
    
    # CALLBACK FUNTIONS
    glutDisplayFunc( drawCilinder )
    glutReshapeFunc( Screen )
    glutKeyboardFunc( keyboard )
    glutMainLoop()

if __name__ == "__main__":
    main()