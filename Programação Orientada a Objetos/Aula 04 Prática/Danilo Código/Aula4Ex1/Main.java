public class Main {

    public static void main(String[] args) {
        Laser l[] = new Laser[10];
        
        for(int i = 0; i< l.length; i++ )
            l[i] = new Laser("Tesla", 10*i, Math.pow(0.1,i), 0);
        
        for(int i = 0; i< l.length; i++ )
            System.out.println(l[i]);
        
        for(int i = 0; i< l.length; i++ )
            System.out.println(l[i].getMedida());
    }   
}