package javaapplication3;

public class Rectangle {
    
    //atributes 
    private int lado1;
    private int lado2;

    public Rectangle(){
        
    }

    public void setLado1(int newLado1)
    {
        this.lado1 = newLado1;
    }
    public int getLado1()
    {
        return this.lado1;
    }

    public void setLado2(int newLado2)
    {
        this.lado2 = newLado2;
    }
    public int getlado2()
    {
        return this.lado2;
    }

    public int area()
    {
        return this.lado1*this.lado2;
    }

    public int perimetro()
    {
        return this.lado1+this.lado2;
    }

}
