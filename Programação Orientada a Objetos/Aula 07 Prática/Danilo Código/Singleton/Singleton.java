public class Singleton {
 
    private static Singleton objetoUnico;
 
    private Singleton() {
    }
 
    public static Singleton getInstance() {
        if (objetoUnico == null)
          objetoUnico = new Singleton();
        return objetoUnico;
    }

    public void print(){
      System.out.println("teste");
    }
}