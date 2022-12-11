package br.calebe.ticketmachine.core;

import java.util.Iterator;

/**
 *
 * @author Calebe de Paula Bianchini
 */
public class Troco {

    protected PapelMoeda[] papeisMoeda;
    
    private int getNumeroNotas(int valorOriginal, int valorNota){
        int count = 0;
        while (valorOriginal != 0 && valorNota % valorOriginal != 0 && valorNota < valorOriginal) {
            count++;
            valorOriginal-= valorNota;
        }
        if (valorOriginal == valorNota){
            count++;
            valorOriginal-= valorNota;
        }
        
        return count;
    }

    public Troco(int valor) {
        papeisMoeda = new PapelMoeda[7];
        int[] notas = {200, 100, 50, 20, 10, 5, 2};

        for (int i = 0; i < notas.length; i++) {
            int numeroDeNotas = this.getNumeroNotas(valor, notas[i]);
            papeisMoeda[i] = new PapelMoeda(notas[i], numeroDeNotas);
            valor-= numeroDeNotas * notas[i];
        }
    }

    public Iterator<PapelMoeda> getIterator() {
        return new TrocoIterator(this);
    }

    static public class TrocoIterator implements Iterator<PapelMoeda> {

        protected Troco troco;

        private int currentIndex = 0;

        public TrocoIterator(Troco troco) {
            this.troco = troco;
        }

        @Override
        public boolean hasNext() {
            return currentIndex < troco.papeisMoeda.length && troco.papeisMoeda[currentIndex] != null;
        }

        @Override
        public PapelMoeda next() {
            return troco.papeisMoeda[currentIndex++];
        }

        @Override
        public void remove() {
            int beforeIndex = currentIndex > 0 ? currentIndex - 1 : 0;
            troco.papeisMoeda[beforeIndex] = null;
        }
    }
}
