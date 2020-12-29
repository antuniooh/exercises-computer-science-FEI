package POO;

public class Ex9 
{   
    public Ex9()
    {
        
    }
    
    public void SAIU_DA_JAULA_O_MONSTRO()
    {
        System.out.println("Triangulos Pitagoricos\n");
        for(int i = 1; i <= 500; i++)
        {
            for(int j = i + 1; j <= 500; j++)
            {
                for(int k = j + 1; k <= 500; k++)
                {
                    if(Math.pow(k, 2) == Math.pow(i, 2) + Math.pow(j, 2)){
                        System.out.printf("(%d, %d, %d)\n", k, i, j);
                    }
                }
            }
        }
        
        System.out.printf("\n");
    }
}