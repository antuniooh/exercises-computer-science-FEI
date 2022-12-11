package tests;

import br.calebe.ticketmachine.core.PapelMoeda;
import br.calebe.ticketmachine.core.TicketMachine;
import br.calebe.ticketmachine.core.Troco;
import br.calebe.ticketmachine.exception.PapelMoedaInvalidaException;
import br.calebe.ticketmachine.exception.SaldoInsuficienteException;
import org.junit.Assert;
import org.junit.Test;


public class TicketMachineTest {

    @Test
    public void checkSucessConstructorAndGetSaldo() {
        int precoDoBilhete = 10;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        Assert.assertEquals(ticketMachine.getSaldo(), 0);
    }

    @Test
    public void checkSucessInserirDinheiroNota2() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 2;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);
        Assert.assertEquals(ticketMachine.getSaldo(), novoSaldo);
    }

    @Test
    public void checkSucessInserirDinheiroNota5() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 5;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);
        Assert.assertEquals(ticketMachine.getSaldo(), novoSaldo);
    }

    @Test
    public void checkSucessInserirDinheiroNota10() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 10;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);
        Assert.assertEquals(ticketMachine.getSaldo(), novoSaldo);
    }

    @Test
    public void checkSucessInserirDinheiroNota20() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 20;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);
        Assert.assertEquals(ticketMachine.getSaldo(), novoSaldo);
    }

    @Test
    public void checkSucessInserirDinheiroNota50() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 50;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);
        Assert.assertEquals(ticketMachine.getSaldo(), novoSaldo);
    }

    @Test
    public void checkSucessInserirDinheiroNota100() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 100;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);
        Assert.assertEquals(ticketMachine.getSaldo(), novoSaldo);
    }

    @Test
    public void checkSucessInserirDinheiroNota200() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 200;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);
        Assert.assertEquals(ticketMachine.getSaldo(), novoSaldo);
    }

    @Test
    public void checkSucessInserirDinheiroNota7Invalida() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 7;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);

        try {
            ticketMachine.inserir(novoSaldo);
        } catch (Exception e){
            Assert.assertEquals(e.getClass(), PapelMoedaInvalidaException.class);
        }
    }

    @Test
    public void checkSucessTroco() throws PapelMoedaInvalidaException, SaldoInsuficienteException {
        int precoDoBilhete = 5;
        int novoSaldo = 100;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);
        ticketMachine.imprimir();

        int saldoAntesTroco = ticketMachine.getSaldo();
        int expectedTroco = novoSaldo - precoDoBilhete;

        Troco.TrocoIterator receivedTroco = ticketMachine.getTroco();

        int trocoTotal = 0;
        while (receivedTroco.hasNext()) {
            PapelMoeda papelMoeda = receivedTroco.next();
            trocoTotal+= papelMoeda.getQuantidade() * papelMoeda.getValor();
        }

        Assert.assertEquals(expectedTroco, saldoAntesTroco);
        Assert.assertEquals(expectedTroco, trocoTotal);
        Assert.assertEquals(0, ticketMachine.getSaldo());

    }

    @Test
    public void checkSucessTrocoSaldo0() throws PapelMoedaInvalidaException, SaldoInsuficienteException {
        int precoDoBilhete = 5;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);

        int saldoAntesTroco = ticketMachine.getSaldo();
        int expectedTroco = 0;

        Troco.TrocoIterator receivedTroco = ticketMachine.getTroco();

        int trocoTotal = 0;
        while (receivedTroco.hasNext()) {
            PapelMoeda papelMoeda = receivedTroco.next();
            trocoTotal+= papelMoeda.getQuantidade() * papelMoeda.getValor();
        }

        Assert.assertEquals(expectedTroco, saldoAntesTroco);
        Assert.assertEquals(expectedTroco, trocoTotal);
        Assert.assertEquals(0, ticketMachine.getSaldo());
    }

    @Test
    public void checkSucessInserirDinheiroNota10Imprimne() throws PapelMoedaInvalidaException, SaldoInsuficienteException {
        int precoDoBilhete = 5;
        int novoSaldo = 10;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);
        ticketMachine.inserir(novoSaldo);

        String bilheteNovoSaldo = ticketMachine.imprimir();
        String expectedPrint = "*****************\n" +
                "*** R$ 5,00 ****\n" +
                "*****************\n";

        Assert.assertEquals(expectedPrint, bilheteNovoSaldo);
        Assert.assertEquals(5, ticketMachine.getSaldo());
    }

    @Test
    public void checkSucessInserirDinheiroSaldoInvalido() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;
        int novoSaldo = 2;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);

        ticketMachine.inserir(novoSaldo);

        try {
            ticketMachine.imprimir();
        } catch (Exception e){
            Assert.assertEquals(e.getClass(), SaldoInsuficienteException.class);
        }
    }

    @Test
    public void checkSucessPedeTrocoDepoisSolicitaImprimirBilhete() throws PapelMoedaInvalidaException {
        int precoDoBilhete = 5;

        TicketMachine ticketMachine = new TicketMachine(precoDoBilhete);

        try {
            ticketMachine.getTroco();
            ticketMachine.imprimir();
        } catch (Exception e){
            Assert.assertEquals(e.getClass(), SaldoInsuficienteException.class);
        }
    }

}
