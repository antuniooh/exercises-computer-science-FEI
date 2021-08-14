#include<stdio.h>
#include<iostream>
// Freeglut library

#include<GL/freeglut.h>

// conatantes para definir o tamanho da viewport

int LAR = 400;
int ALT = 400;

// calback of projection
void Desenha() // call back
{
    // Limpa a janela de visualizaÃ§Ã£o com a cor de fundo especificada
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-200, 200, -200, 200);
    glTranslatef(1, 0, 0);
    glColor3d(1, 0, 0);
    glBegin(GL_TRIANGLES);
    glVertex2d(0, 100);
    glVertex2d(-100, -100);
    glVertex2d(100, -100);
    glEnd();

    // Executa os comandos OpenGL
    glutSwapBuffers();
    //glFlush();
}

// iniciatization function
void Inicializa()
{
    // Define a cor de fundo da janela de visualizaÃ§Ã£o como preta
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
}

// windows setting
void Ajuste_de_Janela(GLsizei w, GLsizei h)
{
    glViewport(0, 0, 400, 400);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-200, 200, -200, 200);
}

// main function
int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(LAR, ALT);
    glutInitWindowPosition(10, 10);
    glutCreateWindow("Quadrado");
    glutDisplayFunc(Desenha); // call back
    glutReshapeFunc(Ajuste_de_Janela);
    Inicializa();
    glutMainLoop();
}