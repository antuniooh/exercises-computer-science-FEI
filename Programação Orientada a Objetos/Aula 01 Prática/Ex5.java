package POO;

import java.util.Scanner;

public class Ex5 {
    private final Scanner input;
    private int soldProducts;
    private float totalValue;
    
    private final float prod1 = 2.98f;
    private final float prod2 = 4.50f;
    private final float prod3 = 3.98f;
    private final float prod4 = 4.49f;
    private final float prod5 = 6.87f;
    
    
    
    public Ex5(){
        input = new Scanner(System.in);
    }
    
    public void showResults(){
        System.out.printf(""
                + "\nNum de produtos vendidos: %d"
                + "\nQuantia total = R$%.2f\n\n",
                soldProducts, totalValue);
    }
    
    public void MainLoop(){
        
        int productNum;
        int qtdSold;
        
        soldProducts = 0;
        totalValue = 0;
        
        System.out.printf("Digite 0 para sair.\n");
        
        boolean run = true;
        while(run){
            System.out.printf("DIgite o codigo e a quantia vendida do produto: ");
            productNum = input.nextInt();
            qtdSold = input.nextInt();
            
            soldProducts += qtdSold;
            
            switch(productNum){
                case 0:
                    run = false;
                case 1:
                    totalValue += prod1 * qtdSold;
                    break;
                case 2:
                    totalValue += prod2 * qtdSold;
                    break;
                case 3:
                    totalValue += prod3 * qtdSold;
                    break;
                case 4:
                    totalValue += prod4 * qtdSold;
                    break;
                case 5:
                    totalValue += prod5 * qtdSold;
                    break;
                          
            }
        }
    }
    
}
