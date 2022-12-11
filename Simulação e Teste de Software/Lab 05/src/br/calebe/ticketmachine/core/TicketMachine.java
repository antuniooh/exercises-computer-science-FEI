package br.calebe.ticketmachine.core;

import br.calebe.ticketmachine.exception.PapelMoedaInvalidaException;
import br.calebe.ticketmachine.exception.SaldoInsuficienteException;
import br.calebe.ticketmachine.core.Troco.TrocoIterator;

/**
 *
 * @author Calebe de Paula Bianchini
 */
public class TicketMachine {

    private int precoDoBilhete;
    private int saldo;
    private int[] papelMoeda = {2, 5, 10, 20, 50, 100, 200};

    public TicketMachine(int precoDoBilhete) {
        this.precoDoBilhete = precoDoBilhete;
        this.saldo = 0;
    }

    public void inserir(int quantia) throws PapelMoedaInvalidaException {
        boolean achou = false;
        for (int i = 0; i < papelMoeda.length && !achou; i++) {
            if (papelMoeda[i] == quantia) {
                achou = true;
            }
        }
        if (!achou) {
            throw new PapelMoedaInvalidaException();
        }
        this.saldo += quantia;
    }

    public int getSaldo() {
        return saldo;
    }

    public TrocoIterator getTroco() {
        TrocoIterator trocoIterator = new TrocoIterator(new Troco(this.getSaldo()));
        this.saldo = 0;
        return trocoIterator;
    }

    public String imprimir() throws SaldoInsuficienteException {
        if (saldo < precoDoBilhete) {
            throw new SaldoInsuficienteException();
        }
        saldo-= precoDoBilhete;
        String result = "*****************\n";
        result += "*** R$ " + saldo + ",00 ****\n";
        result += "*****************\n";
        return result;
    }
}