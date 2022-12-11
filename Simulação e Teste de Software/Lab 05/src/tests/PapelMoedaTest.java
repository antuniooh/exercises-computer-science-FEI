package tests;

import br.calebe.ticketmachine.core.PapelMoeda;
import org.junit.Assert;
import org.junit.Test;


public class PapelMoedaTest {

    @Test
    public void checkSucessConstructor() {
        int valor = 10;
        int quantidade = 1;

        PapelMoeda papelMoeda = new PapelMoeda(valor, quantidade);
        Assert.assertEquals(papelMoeda.getValor(), valor);
        Assert.assertEquals(papelMoeda.getQuantidade(), quantidade);
    }


    @Test
    public void checkgetQuantidadeConstructor() {
        int quantidade = 12;

        PapelMoeda papelMoeda = new PapelMoeda(10, quantidade);
        Assert.assertEquals(papelMoeda.getQuantidade(), quantidade);
    }

    @Test
    public void checkgetValorConstructor() {
        int valor = 12;

        PapelMoeda papelMoeda = new PapelMoeda(valor, 10);
        Assert.assertEquals(papelMoeda.getValor(), valor);
    }

}
