package Ex01;

public class Main {
    public static void main(String[] args) {
        Laser l[] = new Laser[10];

        for(int i = 0; i < 10; i++)
        {
            l[i] = new Laser("LaserI", i, i,i);
        }
        for(int i = 0; i < 10; i++)
        { 
            System.out.println("===================\n");
            System.out.println(l[i].getAlcance());
            System.out.println(l[i].getFabricante());
            System.out.println(l[i].getMedida());
            System.out.println(l[i].getPrecisao());
        }
    }
}
