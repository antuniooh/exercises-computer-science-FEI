class Main
{
    public static void main (String args[])
    {
        Pessoa p1 = new Pessoa();
        ContaComum c = new ContaComum();
        p1.setConta(c);

        
        c.numero = 99;
        System.out.println("Objeto conta dentro de p1: " + p1.conta.numero);
        
  
        p1.conta.numero = 11;
        System.out.println("Objeto conta dentro de p1: " + p1.conta.numero);
        
        System.out.println("Objeto conta fora de p1: " + c.numero); 

        p1.alteraNumConta();

        System.out.println("Objeto conta fora de p1: " + c.numero);
 
    }
}














