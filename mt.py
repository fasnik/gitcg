from __future__ import barry_as_FLUFL
from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
import numpy as np

# MATRICES
def Model():
    #world matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glScale(.5,.5,.5)

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

def draw_vertex_array(mode, count, type, indices:list):
    glEnableClientState(GL_VERTEX_ARRAY)
    glDrawElements( mode , count , type , indices ) 
    glDisableClientState(GL_VERTEX_ARRAY)

# DRAW FUNCTIONS
def drawMTGeometry():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Model()
    glPointSize(5)
    glPointSize(1)
    glColor3f(1.,1.,1.)

    poligono = [ ]
    vertices = [ ]
    x_range = np.arange (-1, 1.1, 0.1)
    y_range = np.arange (-1, 1.1, 0.1)
    for x in x_range:
        for y in y_range:
                vertices.append(x)
                vertices.append(y)

    indices = [ ]
    for i in range(len(x_range)-1):
        for j in range(len(y_range)-1):
            indices.append(j+len(y_range)*i)
            indices.append((j+1)+len(y_range)*i)
            indices.append((j+1)+len(y_range)*(i+1))
            indices.append((j+1)+len(y_range)*(i+1))
            indices.append(j+len(y_range)*(i+1))
            indices.append(j+len(y_range)*i)

    #trianglulos
    for k in range(0, len(indices), 3):
        a = 2*indices[k]
        b = 2*indices[k+1]
        c = 2*indices[k+2]

        p1 = np.array(  [vertices[a],
                        vertices[a+1]])
        p2 = np.array(  [vertices[b],
                        vertices[b+1]])
        p3 = np.array(  [vertices[c],
                        vertices[c+1]])


        r1 = rootFind(p1,p2)
        r2 = rootFind(p1,p3)
        r3 = rootFind(p2,p3)
        if r1:
            if (r2 and r2!=r1):
                poligono.append(r1)
                poligono.append(r2)
               
            elif (r3 and r3!=r1):
                poligono.append(r1)
                poligono.append(r3)
               
        elif (r2 and r3 and r3!=r2):
                poligono.append(r2)
                poligono.append(r3)
               

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glVertexPointer( 2, GL_FLOAT, 0, vertices)
    glIndexPointerf(indices)
    draw_vertex_array(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
    glColor3f(0.5,.5,1.)
    glLineWidth(4)

    glBegin(GL_LINES)
    for i in poligono:
        glVertex2f(i[0],i[1])
    glEnd()
    glLineWidth(1)
    glFlush()

# CALLBACK FUNCTIONS
def keyboard(key, x, y):
    pass

def f(x,y):
    r = y**2 + x**2 - 1.
    return r

def rootFind(p1 :np.array, p2 :np.array):

    a = 0
    b = 1
    xA = (p1 + a*(p2-p1))[0]
    yA = (p1 + a*(p2-p1))[1]
    xB = (p1 + b*(p2-p1))[0]
    yB = (p1 + b*(p2-p1))[1]
        
    for i in range(100):

        if abs(f(xA, yA)) <0.01:
           
            return (xA, yA)

        if abs(f(xB, yB))<0.01:
            
            return (xB, yB)

        if np.sign(f(xA, yA)) == np.sign(f(xB, yB)):
            return None
        else:
            cx = (p1 + 0.5*(a+b)*(p2-p1))[0]
            cy = (p1 +  0.5*(a+b)*(p2-p1))[1]
            if abs(f(cx, cy))<0.01:
                return (cx, cy)
            elif np.sign(f(xA, yA)) == np.sign(f(cx,cy)):
                xA = cx
                yA = cy
                a=0.5*(a+b)
            else:
                xB = cx
                yB = cy
                b=0.5*(a+b)

    return None

def main():
    
    # INIT
    glutInit()
    glutInitWindowSize(600,600)
    glutInitWindowPosition(1500,100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("OpenGl- Ex1")
    glClearColor(0.5, 0.0, 0.0, 1.0)



    #CALLBACK FUNTIONS
    glutDisplayFunc( drawMTGeometry )
    glutReshapeFunc( Screen )
    glutKeyboardFunc( keyboard )
    glutMainLoop()

if __name__ == "__main__":
    main()