class Pessoa
{
    private String nome;
    private String endereco;
    private double renda;
    public ContaComum conta;
    
    public void setConta(ContaComum conta)
    {
        this.conta = conta;
    }

    public void alteraNumConta(){
      conta.numero = 555555;
    }
}
