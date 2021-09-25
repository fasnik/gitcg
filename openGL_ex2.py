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

def distance(pointA :np.array, pointB :np.array):
    d_AB = np.linalg.norm(pointA-pointB)
    return d_AB

def nearest(x :float, y :float, z :float):
    pass

def delaunayContrainTest():
    pass

def evaluteNormalVector(vec1 :np.array, vec2 :np.array):
    n = np.cross(vec1,vec2)
    norm = np.linalg.norm(n)
    n = n/norm
    return n

def evaluteMidPoint(pointA :np.array, pointB :np.array):
    mid_point = 0.5*(pointA + pointB)
    return mid_point

def evaluteProjection(vec: np.array, normal :np.array, mid_point :np.array):
    l_proj = 0.1
    dir = np.cross(vec,normal)/np.linalg.norm(np.cross(vec,normal))
    x_proj = l_proj*(dir) + mid_point
    return x_proj

# DRAW FUNTIONS

def drawMTGeometry():
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
        glColor3f(1.,1.,1.)
        glVertex3f( vertices[i], 
                    vertices[i+1],
                    vertices[i+2])
        # try:
        #     glColor3f(1.,1.,0.)
            
        #     pA = np.array([ vertices[i], 
        #                     vertices[i+1],
        #                     vertices[i+2]])

        #     pB = np.array([ vertices[i+3], 
        #                         vertices[i+4],
        #                         vertices[i+5]])

        #     pC = np.array([ vertices[i+6], 
        #                         vertices[i+7],
        #                         vertices[i+8]])
        #     edge = pB-pA
        #     other_edge = pC-pA
        #     normal = evaluteNormalVector(edge, other_edge)
        #     mp = evaluteMidPoint(pA, pB)
        #     mp = evaluteProjection(edge, normal, mp)
        #     glVertex3f(mp[0],mp[1], mp[2])
        # except:
        #     pass
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
    glutDisplayFunc( drawMTGeometry )
    glutReshapeFunc( Screen )
    glutKeyboardFunc( keyboard )
    glutMainLoop()

if __name__ == "__main__":
    main()