package Exercicio5;

import Exercicio4.Racional;

public class Complex {
    //atributes 
    private double real;
    private double imaginario;

    public double getReal() {
        return real;
    }

    public double getImaginario() {
        return imaginario;
    }

    public void setReal(double real) {
        this.real = real;
    }

    public void setImaginario(double imaginario) {
        this.imaginario = imaginario;
    }

    public Complex(double real, double imaginario) {
        this.real = real;
        this.imaginario = imaginario;
    }

    public Complex() {
    }

    public Complex somar(Complex r1, Complex r2)
    {
        Complex result1 = new Complex();
        result1.imaginario = r1.imaginario + r2.imaginario;
        result1.real = r1.real + r2.real;

        return result1;

    }
    public Complex subtrair(Complex r1, Complex r2)
    {
        Complex result2 = new Complex();
        result2.imaginario = r1.imaginario - r2.imaginario;
        result2.real = r1.real - r2.real;

        return result2;

    }

    public String retornoString()
    {
        return "(" + this.real + " + " + this.imaginario + "i)";
    }
  

}