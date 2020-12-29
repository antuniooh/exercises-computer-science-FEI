public class ICMS implements Imposto{
    public double calcula(Orcamento orcamento){
        return orcamento.valor * 0.1;
    }
}