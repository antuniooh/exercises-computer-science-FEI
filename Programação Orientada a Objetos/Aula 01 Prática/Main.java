package POO;

import java.util.Scanner;

public class Main 
{

    public static Scanner input;
    
    public static Ex1 ex1;
    public static Ex2 ex2;
    public static Ex3 ex3;
    public static Ex4 ex4;
    public static Ex5 ex5;
    public static Ex6 ex6;
    public static Ex7 ex7;
    public static Ex8 ex8;
    public static Ex9 ex9;
    
    public static void main(String[] args)
    {
        input = new Scanner(System.in);
        
        ex1 = new Ex1();
        ex2 = new Ex2();
        ex3 = new Ex3();
        ex4 = new Ex4();
        ex5 = new Ex5();
        ex6 = new Ex6();
        ex7 = new Ex7();
        ex8 = new Ex8();
        ex9 = new Ex9();
        
        MainLoop();
    }
    
    public static void Gui()
    {
        System.out.printf(""
                + "\n=========================================================="
                + "\n 0. Sair"
                + "\n 1. Exercicio 1"
                + "\n 2. Exercicio 2"
                + "\n 3. Exercicio 3"
                + "\n 4. Exercicio 4"
                + "\n 5. Exercicio 5"
                + "\n 6. Exercicio 6"
                + "\n 7. Exercicio 7"
                + "\n 8. Exercicio 8"
                + "\n 9. Exercicio 9"
                + "\n==========================================================");
    }
    
    public static void MainLoop()
    {
        boolean run = true;
        
        while(run)
        {
            Gui();
            
            System.out.printf("\nDigite a opção: ");
            int choice = input.nextInt();
            
            switch (choice) {
                case 0:
                    run = false;
                    break;
                case 1:
                    ex1.Solution();
                    break;
                case 2:
                    ex2.getNum();
                    ex2.getOrder();
                    ex2.printList();
                    break;
                case 3:
                    ex3.showOdd();
                    break;
                case 4:
                    ex4.getNumbers();
                    break;
                case 5:
                    ex5.MainLoop();
                    ex5.showResults();
                    break;
                case 6:
                    ex6.CaiCaiBalao();
                    break;
                case 7:
                    ex7.Sextou();
                    break;
                case 8:
                    ex8.BohemianRhapsody();
                    break;
                case 9:
                    ex9.SAIU_DA_JAULA_O_MONSTRO();
                    break;                                   
                default:
                    break;
            }
            
        }
    }
    
}
