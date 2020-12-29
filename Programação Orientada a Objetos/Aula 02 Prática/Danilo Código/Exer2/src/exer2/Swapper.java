
package exer2;

public class Swapper {
    private float x, y;
    
    void swap(){
        float aux = getX();
        y = aux;
        x = y;
    }

    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public float getY() {
        return y;
    }

    public void setY(float y){
        this.y = y;
    }
}
