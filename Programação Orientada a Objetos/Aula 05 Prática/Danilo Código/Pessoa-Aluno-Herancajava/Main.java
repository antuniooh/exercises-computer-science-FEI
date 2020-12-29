import java.util.Scanner;

class Main{
    public static void main (String args[]){
        String nome, sobrenome, curso;
        int idade;
        
        Scanner input = new Scanner(System.in);
        nome = input.nextLine();
        sobrenome = input.nextLine();
        idade = Integer.parseInt(input.nextLine());
        curso = input.nextLine();
        
        Aluno p1 = new Aluno();
        
        Aluno p2 = new Aluno(nome, sobrenome, idade, curso);
        
        p2.print();
    }
}