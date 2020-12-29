/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex03;
import java.util.ArrayList;
import java.util.Scanner;
/**
 *
 * @author unifansilva
 */
public class Main {

    public static void menu()
    {
        System.out.println("Deseja realizar qual operação? \n");
        System.out.println("1 - Criar");
        System.out.println("2 - Listar");
        System.out.println("3 - Transformar");
        System.out.println("0 - Sair");
    }
    public static void menu1()
    {
        System.out.println("Deseja criar qual tipo de pessoa?");
        System.out.println("1 - Empresario");
        System.out.println("2 - Professor");
        System.out.println("3 - Advogado");
    }

    public static void main(String[] args) {
        Scanner entrada = new Scanner( System.in );
        ArrayList<Agente> agentes = new ArrayList<>();
        boolean run = true;

        while(run)
        {
            menu();
            int operacao = Integer.parseInt(entrada.nextLine());

            switch(operacao)
            {
                case 1:
                    //criar
                    menu1();
                    int opcao = Integer.parseInt(entrada.nextLine());
                    System.out.println("Qual o nome?");
                    String nome = (entrada.nextLine());
                    
                    if(opcao == 1)
                    {
                        System.out.println("Qual a empresa?");
                        String empresa = (entrada.nextLine());

                        agentes.add(new Empresario(empresa, nome));
                    }
                    if(opcao == 2)
                    {
                        System.out.println("Qual a escola?");
                        String escola = (entrada.nextLine());

                        agentes.add(new Professor(escola,nome));
                    }
                    if(opcao == 3)
                    {
                        System.out.println("Qual a OAB?");
                        String oab = (entrada.nextLine());

                        agentes.add(new Advogado(oab,nome));
                    }
                    break;
                case 2:
                    //listar
                    for(int i = 0; i < agentes.size(); i++)
                    {
                        agentes.get(i).apresentacao();
                    }
                    break;
                case 3:
                    //transformar
                    System.out.println("Deseja transformar qual tipo de pessoa em agente? ");
                    String tipo = (entrada.nextLine());
                    System.out.println("Qual o numero dessa pessoa?");
                    int indice = Integer.parseInt(entrada.nextLine());

                    if(tipo.equals("Empresario"))
                    {
                        ((Empresario)agentes.get(indice - 1)).modeAgenteOn();
                    }
                    if(tipo.equals("Professor"))
                    {
                        ((Professor)agentes.get(indice - 1)).modeAgenteOn();
                    }
                    if(tipo.equals("Advogado"))
                    {
                        ((Advogado)agentes.get(indice - 1)).modeAgenteOn();
                    }
                    break;
                case 0:
                    //sair
                    run = false;
                    break;
            }
        }
        entrada.close();
    }
}
