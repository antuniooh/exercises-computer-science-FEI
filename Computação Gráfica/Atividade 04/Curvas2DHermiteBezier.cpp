
/*
Esse codigo serve para vc plotar 3 curvas:

1) uma parabola (que ja plota automatico), apenas para voce estudar o codigo e ver como plota-se uma curva no OpenGL

2) Uma Curva de Hermite, cujas tangentes de entrada e saida sao fixos com #define. Os pontos devem ser
fornecidos pelo usuário na interface. E a sua tarefa é plotar a curva com esses pontos


2) Uma Curva de Bezier de grau 2, cujos pontos de controle devem ser
fornecidos pelo usuário na interface. E a sua tarefa é plotar a curva com esses pontos

Esse codigo foi explicado na aula do dia 04/09/2020.
*/

//#include <stdlib.h>
//#include <stdio.h>
#include <iostream>
#include <math.h>

// Freeglut library
#include <GL/freeglut.h>

//#define PI_ 3.1416

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <GL/glut.h>

// Numero PI
#define myPI 3.14159265

// Domínio e Contra-Dominio Carteziano para o Exercicio de Tranformações
#define MAIORX 200.0f
#define MENORX -200.0f
#define MAIORY 200.0f
#define MENORY -200.0f

// Domínio e Contra-Dominio Carteziano para o Exercicio de Curvas e Superficies
#define MAIORX_BEZIER 400.0f
#define MENORX_BEZIER 0.0f
#define MAIORY_BEZIER 400.0f
#define MENORY_BEZIER 0.0f

// largua e altura das dimenções da Janela do Windows
#define LARGURA_WINDOW 400
#define ALTURA_WINDOW 400

// posição inicial (canto esquerdo superior) da janela Windoes
#define POSWX 250
#define POSWY 150

// tangentes iniciais e finais dos dois pontos da curva de Hermite
#define tang1x 10.0f
#define tang1y -145.0f
#define tang2x 10.0f
#define tang2y -185.0f

// Polinomio de Bezier e Hermite
GLfloat B[4][2]; // para Bezier
GLfloat P[2][4]; // para Hermite

// variaveis de controle
GLboolean GET_POINTS = 0; // GET_POINTS = 0 não está pegando pontos; GET_POINTS = 1, está pegando pontos
GLint TOTAL_POINTS = 0;	  // total de pontos das curvas de Bezier e Hermite

GLfloat bx, by; // pontos inseridos para as curvas

// estrutura para um ponto no espaço 3D
struct Ponto
{
	GLfloat x;
	GLfloat y;
	GLfloat z;
};

void Inicializa(void);												// função de inicialização
void AlteraTamanhoJanela(GLsizei w, GLsizei h);						// função calback de ajuste da janela de visualização
void Teclado(unsigned char key, int x, int y);						// função callback de teclado
void Desenha(void);													// funcção callback principal de desenho (chama todas asa outras)
void myMousefunc(int button, int state, int x, int y);				// função callback de mouse para o exercicio de Tranformações
void myMousefuncBezierIterate(int button, int state, int x, int y); //função callback de mouse para a curva de bezier

GLfloat multiplyHermite(GLfloat T[], GLfloat H[][4], GLfloat M[]); // função que multiplica as matrizes de hermite
void DesenhaParabola();											   // desenha uma parabola simples
void DesenhaHermiteGrau3();										   // desenha uma curva de hermite de grau3
void DesenhaBezierGrau3_v3();
void DesenhaEixos();

Ponto P1, P2, P3, P4;

int main(int argc, char **argv)
{
	glutInit(&argc, argv);

	// Define do modo de operação da GLUT
	// GLUT_SINGLE significa que vai usar 1 buffer só (se for usar animação ou 3D use GLUT_DOUBLE)
	// aqui, como o código é 2D usamos 1 buffer
	// GLUT_RGB significa que cada pixel é RGB
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);

	// Especifica a posição inicial da janela GLUT
	glutInitWindowPosition(POSWX, POSWY);

	// Especifica o tamanho inicial em pixels da janela GLUT
	glutInitWindowSize(LARGURA_WINDOW, ALTURA_WINDOW);

	// Cria a janela passando como argumento o título da mesma
	glutCreateWindow("Uma Bela Curva de Bezier de Grau 3");

	// Registra a função callback de redesenho da janela de visualização
	glutDisplayFunc(Desenha);

	// Registra a função callback de redimensionamento da janela de visualização
	glutReshapeFunc(AlteraTamanhoJanela);

	// Registra a função callback para tratamento das teclas ASCII
	glutKeyboardFunc(Teclado);

	// Registra a função callback mouse
	glutMouseFunc(myMousefuncBezierIterate);

	// Chama a função responsável por fazer as inicializações
	Inicializa();

	// Inicia o processamento e aguarda interações do usuário
	glutMainLoop();

	return 0;
}

// Função callback de redesenho da janela de visualização
void Desenha(void)
{

	// Limpa a janela de visualização com a cor
	// de fundo definida previamente
	glClear(GL_COLOR_BUFFER_BIT);

	// funcao que desenha eixos cartesianos.
	// Note que esses eixos são apenas uma normalização que vc desenha, não é o tamanho da janela windows
	//DesenhaEixos();

	//DesenhaParabola();
	DesenhaBezierGrau3_v3(); // usar
	//DesenhaHermiteGrau3(); /// usar

	// Executa os comandos OpenGL
	glFlush();
	//glutPostRedisplay();
}

// Esta função não é CallBack de desenho
//ela é chamada pela callback Desenha apenas para separar a tarefa de desenhar das outras tarefas;
// A tarefa aqui é desenhar os eixos cartesianos
//Importante notar que as dimenções dos eixos cartezianos nao são em pixels, como definido no main em glutInitWindowSize
//A escala desses eixos é definida na função void AlteraTamanhoJanela, nas linhas gluOrtho2D...
//é uma questão de organização de codigo
//O programa pode funcionar sem ela
void DesenhaEixos()
{
	// Desenha a linha vertical
	glColor3f(0.0, 0.0f, 0.0f);
	glBegin(GL_LINES);
	glVertex2f(0.0f, MENORY);
	glVertex2f(0.0f, MAIORY);
	glEnd();

	/// EIXOS
	// Desenha a linha horizontal
	glColor3f(0.0, 0.0f, 0.0f);
	glBegin(GL_LINES);
	glVertex2f(MENORX, 0.0f);
	glVertex2f(MAIORX, 0.0f);
	glEnd();
}

// Essa função desenha a curva de Hermite de Grau 3. A matriz de Hermite já está colocada
// no código pra vc, é a variável H. Os e pontos de Hermite são fornecidos pela interface
// clicando com o mouse.
void DesenhaHermiteGrau3()
{

	// Matriz de Hermite de Grau 3
	GLfloat H[4][4] = {{2.0f, -2.0f, 1.0f, 1.0f},
					   {-3.0f, 3.0f, -2.0f, -1.0f},
					   {0.0f, 0.0f, 1.0f, 0.0f},
					   {1.0f, 0.0f, 0.0f, 0.0f}};

	// se o numero de pontos fornecidos for zero, esse trecho de código inicializa só
	// o primeito ponto, para indicar que o usuário clicou em algum lugar, mas
	// ainda bão clicou no segundo ponto
	// GET_POINTSD = Status de atribuição de pontos pelo mouse
	if ((TOTAL_POINTS == 0) && (GET_POINTS))
	{
		P[0][0] = bx;	  // guarda coordenada x
		P[0][1] = by;	  // guarda coordenada y
		P[0][2] = tang1x; // tangente x do angulo de incidência de entrada
		P[0][3] = tang1y; // tangente y do angulo de incidência de entrada
		TOTAL_POINTS = TOTAL_POINTS + 1;
	}

	// se o total de pontos ainda for menor do que 2 e maior do que zero
	// os pontos são guardados, juntamente com os ângulos e tangentes,
	// que devem ser fornecidos diretamente no código
	if ((TOTAL_POINTS > 0) && (GET_POINTS) && (TOTAL_POINTS < 2))
	{
		// testa se o ponto aqul clicado é diferente do anterior
		if ((P[TOTAL_POINTS - 1][0] != bx) && (P[TOTAL_POINTS - 1][1] != by))
		{
			P[TOTAL_POINTS][0] = bx;	 // guarda coordenada de netrada x
			P[TOTAL_POINTS][1] = by;	 // guarda coordenada de entrada y
			P[TOTAL_POINTS][2] = tang2x; // tangente x do aângulo de incidência de saída
			P[TOTAL_POINTS][3] = tang2y; // tangente y do ângulo de inciência de saída
			TOTAL_POINTS = TOTAL_POINTS + 1;
			if (TOTAL_POINTS > 2)
				TOTAL_POINTS = 2;
		}
	}

	// exibe os 2  pontos de controle
	glColor3f(1.0, 0.0f, 0.0f);
	glPointSize(5.0f);
	for (int i = 0; i < TOTAL_POINTS; i++)
	{
		//printf("\n%f %f", B[i][0], B[i][1]);
		glBegin(GL_POINTS);
		glVertex2f(P[i][0], P[i][1]);
		glEnd();
	}

	// agora que vc tem os dois pontos e as duas tangentes, que estão em P
	// basta só utilizar a teoria vista nos vídeos para montar o polinomio de Hermote
	// e plotar a curva. Não se esqueça de variar a variável t de 0 a 1, indo de
	// 0.1 em 0.1, pelo menos, ou 0.01 em 0.01.

	if (TOTAL_POINTS == 2)
	{
		// calcule aqui sua curva de hermite

		GLfloat t = 0;
		GLfloat M[2][4] = {
			{P[0][0],
			 P[1][0],
			 P[0][2],
			 P[1][2]},
			{P[0][1],
			 P[1][1],
			 P[0][3],
			 P[1][3]}};

		GLfloat curvePoints[100][2];

		for (int i = 0; t < 1.0; t += 0.01, i++)
		{
			GLfloat T[4] = {t * t * t, t * t, t, 1};

			curvePoints[i][0] = multiplyHermite(T, H, M[0]);
			curvePoints[i][1] = multiplyHermite(T, H, M[1]);
		}

		// com todos os pontos calculados, agora vc plota a curva toda
		// se tiver dúvida como fazer isso, observe o código da Função
		// DesenhaParabola(), nele vcja como a parábola foi plotada e
		// faça o mesmo para a curva de hermite
		for (int i = 1; i < 100; i++)
		{
			glBegin(GL_LINE_STRIP);
			glVertex2f(curvePoints[i - 1][0], curvePoints[i - 1][1]);
			glVertex2f(curvePoints[i][0], curvePoints[i][1]);
			glEnd();
		}
	}
}

void DesenhaBezierGrau3_v3()
{
	const GLint DIMX = MENORX_BEZIER + MAIORX_BEZIER + 1;
	const GLint DIMY = MENORY_BEZIER + MAIORY_BEZIER + 1;

	GLfloat H[4][4] = {{-1.0f, 3.0f, -3.0f, 1.0f},
					   {3.0f, -6.0f, 3.0f, 0.0f},
					   {-3.0f, 3.0f, 0.0f, 0.0f},
					   {1.0f, 0.0f, 0.0f, 0.0f}};

	// esse trecho de código salva só o primeiro pontos
	// clicado na interface
	// se o numero de pontos fornecidos for zero
	// GET_POINTSD = Status de atribuição de pontos pelo mouse
	if ((TOTAL_POINTS == 0) && (GET_POINTS))
	{
		B[0][0] = bx; // coordenada x do primeiro ponto
		B[0][1] = by; // ordenada y do primeiro ponto
		TOTAL_POINTS = TOTAL_POINTS + 1;
	}

	// esse segundo trecho salva os demais pontos clicados
	// da curva de Bezier
	// se o total de pontos ainda for menor do que 4 e maior do que zero
	if ((TOTAL_POINTS > 0) && (GET_POINTS) && (TOTAL_POINTS < 4))
	{
		// testa se o ponto aqul clicado é diferente do anterior
		if ((B[TOTAL_POINTS - 1][0] != bx) && (B[TOTAL_POINTS - 1][1] != by))
		{
			B[TOTAL_POINTS][0] = bx;
			B[TOTAL_POINTS][1] = by;
			TOTAL_POINTS = TOTAL_POINTS + 1;
			if (TOTAL_POINTS > 4)
				TOTAL_POINTS = 4;
		}
	}

	// exibe apenas os 4  pontos de controle
	glColor3f(1.0, 0.0f, 0.0f);
	glPointSize(5.0f);
	//printf("\n\n");
	for (int i = 0; i < TOTAL_POINTS; i++)
	{
		//printf("\n%f %f", B[i][0], B[i][1]);
		glBegin(GL_POINTS);
		glVertex2f(B[i][0], B[i][1]);
		glEnd();
	}

	// nesse trecho de codigo, vc deve calcular todos os pontos (nao de controles)
	// por onde passa a curva de Bezier. Para isso, tem que saber a teoria
	if (TOTAL_POINTS == 4)
	{
		// calcule aqui um ponto da curva de Bezier e salve-o em um vetor P
		GLfloat t = 0.00f;
		GLfloat M[4][4] = {
			{
			 B[0][0],
			 B[1][0],
			 B[2][0],
			 B[3][0]},
			{
			 B[0][1],
			 B[1][1],
			 B[2][1],
			 B[3][1]}};

		GLfloat P[100][2];

		for (int i = 0; t < 1.0; t += 0.01, i++)
		{
			GLfloat T[4] = {t * t * t, t * t, t, 1};

			P[i][0] = multiplyHermite(T, H, M[0]);
			P[i][1] = multiplyHermite(T, H, M[1]);
		}

		// com todos os pontos calculados, agora vc plota a curva toda
		// se tiver dúvida como fazer isso, observe o código da Função
		// DesenhaParabola(), nele vcja como a parábola foi plotada e
		// faça o mesmo para a curva de hermite
		for (int i = 1; i < 100; i++)
		{
			glBegin(GL_LINE_STRIP);
			glVertex2f(P[i - 1][0], P[i - 1][1]);
			glVertex2f(P[i][0], P[i][1]);
			glEnd();
		}
	}

	// com todos os pontos calculados no trecho anterior, agora vc plota a curva toda
	// se tiver dúvida como fazer isso, observe o código da Função
	// DesenhaParabola(), nele vcja como a parábola foi plotada e
	// faça o mesmo para a curva de hermite
}

void DesenhaParabola()
{

	//y = ax^2 + bx + c
	const GLint DIMX = (-1) * MENORX + MAIORX + 1;
	const GLint DIMY = (-1) * MENORY + MAIORY + 1;

	// valores de coordenadas e ordenadas
	GLfloat X[DIMX];
	GLfloat Y[DIMY];

	// parÂmetros
	GLfloat n = 2;		 // grau
	GLfloat passo = 0.2; // discretização
	GLfloat a = 0.03;	 // constante de x^2
	GLfloat b = 0;		 // constante de x
	GLfloat c = -20;	 // constante isolada
	GLfloat xini, yini, xfin, yfin;
	GLfloat x, y;

	glColor3f(1.0, 0.0f, 0.0f);
	x = -50;
	y = a * pow(x, n) + b * x + c;
	xini = x;
	yini = y;

	// plota o primeiro ponto
	glBegin(GL_POINTS);
	glVertex2f(xini, yini);
	glEnd();

	// plota os demais pontos
	for (x = -50 + passo; x < 50; x = x + passo)
	{
		// aqui calcula cada ponto da parábola
		y = a * pow(x, 2) + b * x + c;
		xfin = x;
		yfin = y;

		// esse trecho plota cada pedaço da parábola
		// entre seus pontos
		glBegin(GL_LINE_STRIP);
		glVertex2f(xini, yini);
		glVertex2f(xfin, yfin);
		glEnd();
		xini = xfin;
		yini = yfin;
	}
}

// Função callback chamada quando o tamanho da janela é alterado
void AlteraTamanhoJanela(GLsizei w, GLsizei h)
{
	//GLsizei largura, altura;
	GLfloat largura, altura;

	// Evita a divisao por zero
	if (h == 0)
		h = 1;

	// Atualiza as variáveis
	largura = w;
	altura = h;

	// Especifica as dimensões da Viewport
	glViewport(0, 0, largura, altura);

	// Inicializa o sistema de coordenadas
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	// Estabelece a janela de seleção (esquerda, direita, inferior,
	// superior) mantendo a proporção com a janela de visualização
	if (largura <= altura)
		//gluOrtho2D(MENORX, MAIORX, MENORY*altura / largura, MAIORY*altura / largura);
		gluOrtho2D(MENORX_BEZIER, MAIORX_BEZIER, MENORY_BEZIER * altura / largura, MAIORY_BEZIER * altura / largura);
	else
		//gluOrtho2D(MENORX*largura / altura, MAIORX*largura / altura, MENORY, MAIORY);
		gluOrtho2D(MENORX_BEZIER * largura / altura, MAIORX_BEZIER * largura / altura, MENORY_BEZIER, MAIORY_BEZIER);
}

// Função callback chamada para gerenciar eventos de teclas
void Teclado(unsigned char key, int x, int y)
{
	if (key == 27) // sai comm ESC
		exit(0);
}

// Função responsável por inicializar parâmetros e variáveis
void Inicializa(void)
{
	// Define a cor de fundo da janela de visualização como branca
	glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
}

void myMousefuncBezierIterate(int button, int state, int x, int y)
{
	switch (button)
	{
	case GLUT_LEFT_BUTTON:
	{
		bx = x;
		by = 400 - y;
		GET_POINTS = 1;
		//if (TOTAL_POINTS == 4) TOTAL_POINTS = 0;
		//printf("\n %f %f\n", bx, by);
		break;
	}
	case GLUT_RIGHT_BUTTON:
	{

		GET_POINTS = 0;
		TOTAL_POINTS = 0;
		//glutPostRedisplay();
		break;
	}
	case GLUT_MIDDLE_BUTTON:
	{

		break;
	}
	};

	glutPostRedisplay();
}

void myMousefunc(int button, int state, int x, int y)
{
	//printf("\nmouse na posicao x = %d e y = %d",x,y);

	switch (button)
	{
	case GLUT_LEFT_BUTTON && (state == GLUT_DOWN):
	{
		printf("\nvoce pressiona o botao esquerdo do mouse");
		break;
	}
	case GLUT_RIGHT_BUTTON:
	{
		printf("\nvoce pressiona o botao direito do mouse");
		break;
	}
	case GLUT_MIDDLE_BUTTON:
	{
		printf("\nvoce pressiona o botao do meio do mouse");
		break;
	}
	};

	switch (state)
	{
	case GLUT_DOWN:
	{
		printf("\nvoce esta pressionando o botao do mouse");
		break;
	}
	case GLUT_UP:
	{
		printf("\nvoce soltou o botao do mouse");
		break;
	}
	};

	glutPostRedisplay();
}

// função que multiplica as 3 matrizes de Hermite T * H * M, onde M = {X,Y}
GLfloat multiplyHermite(GLfloat T[], GLfloat H[][4], GLfloat M[])
{

	GLfloat HM[4];

	// m ultiplica primeiro H por M
	for (int i = 0; i < 4; i++)
	{
		HM[i] = 0;
		for (int j = 0; j < 4; j++)
		{
			HM[i] = HM[i] + H[i][j] * M[j];
		}
	}

	// multiplica T * HM
	GLfloat R = 0;
	for (int i = 0; i < 4; i++)
	{
		R = R + T[i] * HM[i];
	}

	return R;
}
