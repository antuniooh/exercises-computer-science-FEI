package javaapplication6;

import java.util.Scanner;

public class Main {

    public static Funcionario setFuncionario(String name, String sobrenome, double salario)
    {
        Funcionario func = new Funcionario();

        func.setName(name);
        func.setSobrenome(sobrenome);
        func.setSalario(salario);

        return func;
    }

    public static void retorno(Funcionario f)
    {
        System.out.println("=================================");
        System.out.printf("Nome: %s %s\n", f.getName(), f.getSobrenome());
        System.out.printf("Salário Mensal: R$ %f\n", f.getSalario());
        System.out.printf("Salário Anual: R$ %f\n", f.salarioAnual());
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner( System.in );

        Funcionario func1 = new Funcionario();
        Funcionario func2 = new Funcionario(); 
        
        for(int i = 1; i < 3; i++){
            System.out.println("=================================");

            System.out.printf("Digite o nome do funcionário %d: ", i);
            String name = input.nextLine();

            System.out.printf("Digite o sobrenome do funcionário %d :", i);
            String sobrenome = input.nextLine();

            System.out.printf("Digite o salário mensal do funcionário %d: ", i);
            double salario =  Double.parseDouble(input.nextLine());

            switch (i) {
                case 1:
                    func1 = setFuncionario(name, sobrenome, salario);
                    break;
                case 2:
                    func2 = setFuncionario(name, sobrenome, salario);

            }
        }
        retorno(func1);
        retorno(func2);

        System.out.println("=================================");
        System.out.println("APÓS O AUMENTO DE 10%");
        System.out.println("=================================");

        func1.aumento(10);
        func2.aumento(10);

        retorno(func1);
        retorno(func2);

    }
    
}
