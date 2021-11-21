// 1) Este arquivo contem uma demonstração bem simples de um programa básico em OpenGL
//
// 2) Ele foi feito para iniciantes que desejam aprender o básico.
//
// 3) O programa faz apenas uma projeção 2D de uma figura geométrica básica: um triângulo
//
// 4) Prossui apenas o programa principal, main, e 3 funçòes auxiliares: uma de inicialização
// (Inicializa()), uma função callcak de desenho (Desenha()) e uma função callback de ajuste
// de Janela de Vizualizacao (Ajuste_de_Janela(..))
//
// 5) Ela baseia-se na biblioteca freeglut, uma alternativa à glut que deu continuidade ao
// trabalho da glut.
//
// Author: Prof. Paulo Sérgio Rodrigues, Centro Universitario FEI
// Date: February 15th, 2021
//
#include <stdio.h>

#include <iostream>
 // Freeglut library
#include <GL/freeglut.h>
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
void Inicializa() {
    // Define a cor de fundo da janela de visualizaÃ§Ã£o como preta
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
}
// windows setting
void Ajuste_de_Janela(GLsizei w, GLsizei h) {
    glViewport(0, 0, 400, 400);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-200, 200, -200, 200);
}
// main function
int main(int argc, char ** argv) {
    glutInit( & argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(LAR, ALT);
    glutInitWindowPosition(10, 10);
    glutCreateWindow("Quadrado");
    glutDisplayFunc(Desenha); // call back
    glutReshapeFunc(Ajuste_de_Janela);
    Inicializa();
    glutMainLoop();
}
