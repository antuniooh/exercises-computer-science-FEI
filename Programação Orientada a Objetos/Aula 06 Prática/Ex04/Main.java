
package Ex04;

public class Main {

    public static void main(String[] args) {        
     MovableCircle c = new MovableCircle(10, 10, 5, 5, 1);

     c.moveDown();
     System.out.println(c.toString());
     c.moveLeft();
     System.out.println(c.toString());
     c.moveUp();
     System.out.println(c.toString());
     c.moveRight();
     System.out.println(c.toString());
    }
    
}
