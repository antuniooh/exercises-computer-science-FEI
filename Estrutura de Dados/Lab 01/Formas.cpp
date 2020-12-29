#include <cmath>
#include <iostream>

using namespace std;

class Forma{
public:
  virtual float area(){return 0.0;}
};

class Quadrado : public Forma {
private:
  float largura;
  float altura;
public:
  Quadrado(float largura, float altura){
    this->altura = altura;
    this->largura = largura;
  }
  float area(){
      return (this->altura * this->largura);
  }
};

class Triangulo : public Forma {
private:
  float largura;
  float altura;
public:
  Triangulo(float largura, float altura){
    this->altura = altura;
    this->largura = largura;
  }
  float area(){
      return ((this->altura * this->largura)/2);
  }
};

class Circulo : public Forma {
private:
  float raio;
public:
  Circulo(float raio){
    this->raio = raio;
  }
  float area(){
      return (M_PI * pow(this->raio, 2));
  }
};

void calculaArea (Forma* f) {
  cout << "Area=" << f->area() << endl;
}

int main () {
  Quadrado q1 (10.2, 20);
  Triangulo t1 (20.6, 3.1);
  Circulo c1 (30.2);

  calculaArea (&q1);
  calculaArea (&t1);
  calculaArea (&c1);

  return 0;
}