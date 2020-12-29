public class Main{
    public static void main(String args[]){
        Orcamento orcamento = new Orcamento(500.0);
        
        CalculadoraImpostos calc = new CalculadoraImpostos();
        
        Imposto imposto;
        imposto = new ISS();
        calc.realizaCalculo(orcamento, imposto);
        
        imposto = new ICMS();
        calc.realizaCalculo(orcamento, imposto);
    }
}

