
package exer1;

import java.util.Scanner;

public class Exer1 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        
        Pessoa p1 = new Pessoa();
        Pessoa p2 = new Pessoa();
        Pessoa p3 = new Pessoa();
        
        p1.setNome(entrada.nextLine());
        System.out.println(p1.getNome());
        
        p1.setCpf(entrada.nextLine());
        System.out.println(p1.getCpf());
                
        p1.setIdade( Integer.parseInt(entrada.nextLine()) );
        System.out.println(p1.getIdade());
        
        p2.setNome(entrada.nextLine());
        System.out.println(p2.getNome());
        
        p2.setCpf(entrada.nextLine());
        System.out.println(p2.getCpf());
                
        p2.setIdade(Integer.parseInt(entrada.nextLine()));
        System.out.println(p2.getIdade());
        
        p3.setNome(entrada.nextLine());
        System.out.println(p3.getNome());
        
        p3.setCpf(entrada.nextLine());
        System.out.println(p3.getCpf());
                
        p3.setIdade(Integer.parseInt(entrada.nextLine()));
        System.out.println(p3.getIdade());
        
        
        
    }
}
