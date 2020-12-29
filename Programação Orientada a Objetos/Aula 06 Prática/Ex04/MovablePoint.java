package Ex04;

class MovablePoint implements IMoveable{
    protected int x;
    protected int y;
    protected int xSpeed;
    protected int ySpeed;

    public MovablePoint(int x, int y, int xSpeed, int ySpeed)
    {
        this.x = x;
        this.y = y;
        this.xSpeed = xSpeed;
        this.ySpeed = ySpeed;
    }

    public void moveUp()
    {
        this.y += 1 * ySpeed;
    }
    
    public void moveDown()
    {
        this.y -=1 *xSpeed;
    }

    public void moveLeft()
    {
        this.x -= 1 * xSpeed;
    }
    public void moveRight()
    {
        this.x += 1 * xSpeed;
    }
}