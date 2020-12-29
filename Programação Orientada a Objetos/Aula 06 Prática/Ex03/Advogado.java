package Ex03;

class Advogado extends Agente{
    private String OAB;

    public Advogado(String OAB, String nome)
    {
        this.OAB = OAB;
        setNome(nome);
    }
    public Advogado()
    {
    }

    void setOAB(String OAB)
    {
        this.OAB = OAB;
    }
    String getOAB()
    {
        return OAB;
    }

    public void apresentacao()
    {
        System.out.println("Nome: " + getNome() );
        System.out.println("Profissao: " + "Advogado");
        System.out.println("OAB: " + getOAB());

        if(getModeOnAgente() == true)
            System.out.println("MODE AGENTE SMITH");
    }

    public void modeAgenteOn()
    {
        setModeOnAgente(true);
    }
}