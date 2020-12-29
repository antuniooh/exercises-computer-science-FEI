
package Ex02;
import java.lang.Math;

class Circulo extends Formas{
    private double raio;

    public Circulo() {
    }

    public Circulo(double raio)
    {
        this.raio = raio;
    }

    void setRaio(double raio)
    {
        this.raio = raio;
    }

    double getRaio()
    {
        return raio;
    }

    double area()
    {
        return (Math.PI * Math.pow(this.raio, 2));
    }

    public double perimetro(double x, double y)
    {
        return (2 * x * raio);
    }

    public void print()
    {
        System.out.println("Perimetro: " + perimetro(Math.PI, raio));
        System.out.println("Area: " + area());
    }
    
}
