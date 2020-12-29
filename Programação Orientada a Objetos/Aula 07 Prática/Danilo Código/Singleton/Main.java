class Main {
  public static void main(String[] args) {
    Singleton objeto = Singleton.getInstance();
    objeto.print();

    Singleton obj = Singleton.getInstance();
    obj.print();

    System.out.println(objeto);
    System.out.println(obj);

  }
}