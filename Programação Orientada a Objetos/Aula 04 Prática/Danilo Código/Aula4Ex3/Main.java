import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
      ArrayList<String> nomes1 = new ArrayList<>(10); 
     
      nomes1.add("Fulano");
      nomes1.add("Sicrano");
      nomes1.add("Beltrano");
      
      System.out.println(nomes1.size());
      
      ArrayList<String> nomes2 = new ArrayList<>(nomes1); 
    
      nomes2.set(1, "Novo!");
      
      for(String nome: nomes1)
        System.out.println(nome);
      
      System.out.println();
      for(String nome: nomes2)
        System.out.println(nome);
    }        
}