package javaapplication2;

public class Swapper {
    
    //atributes 
    private float x;
    private float y;

    public Swapper(){
        
    }

    public void setX(float newX)
    {
        this.x = newX;
    }
    public float getX()
    {
        return this.x;
    }

    public void setY(float newY)
    {
        this.y = newY;
    }
    public float getY()
    {
        return this.y;
    }

    public void swap()
    {
        float temp = this.x;
        this.x = y;
        this.y = temp;
    }

}
