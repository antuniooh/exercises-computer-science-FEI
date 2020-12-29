
package Ex02;

class Retangulo extends Formas{
    private double comprimento;
    private double largura;

    public Retangulo() {
    }

    public Retangulo(double comprimento, double largura)
    {
        this.comprimento = comprimento;
        this.largura = largura;
    }

    void setComprimento(double comprimento)
    {
        this.comprimento = comprimento;
    }
    void setLargura(double largura)
    {
        this.largura = largura;
    }

    double getComprimento()
    {
        return comprimento;
    }

    double getLargura()
    {
        return largura;
    }

    public double perimetro(double x, double y)
    {
        return ((2 * x) + (2 * y));
    }

    public void print()
    {
        System.out.println("Perimetro: " + perimetro(comprimento, largura));
    }
    
}
