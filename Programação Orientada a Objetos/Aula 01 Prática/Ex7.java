package POO;

import java.util.Scanner;

public class Ex7 
{
    private final Scanner input;
    public float salary;
    
    public Ex7()
    {
        input = new Scanner(System.in);
    }
    
    public void Sextou()
    {
        System.out.println("Digite o salário atual: ");
        salary = input.nextFloat();
        float newSalary;
                
        if(salary >= 0 && salary <= 400)
        {
            newSalary = salary*0.15f;
            System.out.printf("Novo salário: R$%.2f\n", newSalary + salary);
            System.out.printf("Valor ganho de reajuste: R$%.2f\n", newSalary);
            System.out.printf("Valor ganho de reajuste: 15%%\n");
        }
        else if(salary > 400 && salary <= 800)
        {
            newSalary = salary*0.12f;
            System.out.printf("Novo salário: R$%.2f\n", newSalary+ salary);
            System.out.printf("Valor ganho de reajuste: R$%.2f\n", newSalary);
            System.out.printf("Valor ganho de reajuste: 12%%\n");
        }
        else if(salary > 800 && salary <= 1200)
        {
            newSalary = salary*0.1f;
            System.out.printf("Novo salário: R$%.2f\n", newSalary+ salary);
            System.out.printf("Valor ganho de reajuste: R$%.2f\n", newSalary);
            System.out.printf("Valor ganho de reajuste: 10%%\n");
        }
        else if(salary > 1200 && salary <= 2000)
        {
            newSalary = salary*0.07f;
            System.out.printf("Novo salário: R$%.2f\n", newSalary+ salary);
            System.out.printf("Valor ganho de reajuste: R$%.2f\n", newSalary);
            System.out.printf("Valor ganho de reajuste: 17%%\n");
        }
        else
        {
            newSalary = salary*0.04f;
            System.out.printf("Novo salário: R$%.2f\n", newSalary+ salary);
            System.out.printf("Valor ganho de reajuste: R$%.2f\n", newSalary);
            System.out.printf("Valor ganho de reajuste: 4%%\n");
        }
        
        System.out.printf("\n");
    }
    
    
}
