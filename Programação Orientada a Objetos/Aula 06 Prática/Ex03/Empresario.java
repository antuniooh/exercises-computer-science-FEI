package Ex03;

class Empresario extends Agente{
    private String empresa;

    public Empresario(String empresa, String nome)
    {
        this.empresa = empresa;
        setNome(nome);
    }
    public Empresario()
    {
    }

    void setEmpresa(String empresa)
    {
        this.empresa = empresa;
    }
    String getEmpresa()
    {
        return empresa;
    }

    public void apresentacao()
    {
        System.out.println("Nome: " + getNome());
        System.out.println("Profissao: " + "Empresário");
        System.out.println("Empresa: " + getEmpresa());

        if(getModeOnAgente() == true)
            System.out.println("MODE AGENTE SMITH");
    }

    public void modeAgenteOn()
    {
        setModeOnAgente(true);
    }
}