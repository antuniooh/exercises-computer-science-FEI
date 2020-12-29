import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
      ArrayList<String> cor1 = new ArrayList<>(); 
      ArrayList<String> cor2 = new ArrayList<>(); 
      
      cor1.add("Vermelho");
      cor1.add("Azul");
      cor1.add("Verde");
      
      cor2.add("Amarelo");
      cor2.add("Verde");
      cor2.add("Azul");
      cor2.add("Vermelho");
      
      System.out.println(cor1.containsAll(cor2));
      System.out.println(cor2.containsAll(cor1));
      System.out.println(cor1.contains("Azul"));
    }    
}  