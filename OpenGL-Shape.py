import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.raw.GLU import gluLookAt, gluPerspective

rotation = 0.0  # Current rotation angle

def draw_sphere():
    glutWireSphere(1.0, 20, 20)  # Draw a wireframe sphere

def display():
    global rotation

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 3, 0, 0, 0, 0, 1, 0)  # Set up the camera

    glRotatef(rotation, 0, 1, 0)  # Rotate the sphere around the y-axis

    glColor3f(1.0, 1.0, 1.0)  # Set sphere color to white
    draw_sphere()

    glFlush()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width)/height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def idle():
    global rotation
    rotation += 0.1  # Increment rotation angle
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Rotating Sphere")
    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)

    glutMainLoop()

if __name__ == '__main__':
    main()