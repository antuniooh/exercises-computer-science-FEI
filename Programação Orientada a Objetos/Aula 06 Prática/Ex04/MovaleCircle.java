package Ex04;

import Ex04.MovablePoint;

class MovableCircle extends MovablePoint implements IMoveable{
    private int radius;
    private MovablePoint center;

    public MovableCircle(int x, int y, int xSpeed, int ySpeed, int radius)
    {
        super(x, y, xSpeed, ySpeed);
        this.radius = radius;
    }

    public String toString()
    {
        return ("Position is: (" + (x) + ", " +(y) + ") And Speed is: (" + (xSpeed) + ", " +(ySpeed) + ")");
    }

}