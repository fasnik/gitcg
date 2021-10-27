from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import numpy as np


def main():
    M = np.array([[1,-1],[1,0]], dtype=np.float64)
    Minv =np.linalg.inv(M)
    I = np.array([[round(i,2) for i in j] for j in np.dot(M, Minv)])
    N = np.transpose(Minv)
    print(I)
    print(N)

if __name__ == "__main__":
    main()