package aula03ex1;

public class Aula03Ex1 {
    public static void main(String[] args) {
        Funcionario f1 = new Funcionario();
        Funcionario f2 = new Funcionario(50, 123456, "Fulano", "M");
        Funcionario f3 = new Funcionario("Beltrano", 654321, 40, "M");
    
        System.out.println(f1.getClass());

        System.out.println(f1.getNome() + " " + f1.getIdade());
        System.out.println(f2.getNome() + " " + f2.getIdade());
        System.out.println(f3.getNome() + " " + f3.getIdade());
    }
    
}
