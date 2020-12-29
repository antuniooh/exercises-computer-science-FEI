package Exercicio4;

public class Racional {
    //atributes 
    private int numerador;
    private int denominador;

    public Racional(int numerador, int denominador) {
        this.numerador = numerador;
        this.denominador = denominador;
    }
    
    public Racional(){};

    public int mdc(int a, int b)
    {
        if (a % b == 0) {
            return b;
        }
        return mdc(b, a % b);
    }

    public Racional somar(Racional r1, Racional r2)
    {
        Racional result1 = new Racional();
        int mmc = (r1.denominador*r2.denominador)/mdc(r1.denominador, r2.denominador);
        result1.numerador = ((r1.numerador * mmc)/r1.denominador) + (r2.numerador * mmc)/r2.denominador;
        result1.denominador = mmc;

        return result1;

    }
    public Racional subtrair(Racional r1, Racional r2)
    {
        Racional result2 = new Racional();
        int mmc = (r1.denominador*r2.denominador)/mdc(r1.denominador, r2.denominador);
        result2.numerador = ((r1.numerador * mmc)/r1.denominador) - (r2.numerador * mmc)/r2.denominador;
        result2.denominador = mmc;

        return result2;
    }
    public Racional multiplicar(Racional r1, Racional r2)
    {
        Racional result3 = new Racional();
        result3.numerador = (r1.numerador * r2.numerador);
        result3.denominador = (r1.denominador * r2.denominador);

        return result3;
    }
    public Racional dividir(Racional r1, Racional r2)
    {
        Racional result4 = new Racional();
        result4.numerador = (r1.numerador * r2.denominador);
        result4.denominador = (r1.denominador * r2.numerador);

        return result4;
    }

    public String retornoString()
    {
        return this.numerador + "/" + this.denominador;
    }
    public double retornoDouble()
    {
        return (this.numerador*1.0/this.denominador*1.0);
    }


}