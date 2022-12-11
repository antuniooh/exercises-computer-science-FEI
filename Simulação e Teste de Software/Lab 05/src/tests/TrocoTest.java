package tests;

import br.calebe.ticketmachine.core.PapelMoeda;
import br.calebe.ticketmachine.core.Troco;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;


public class TrocoTest {

    @Test
    public void checkSucessTrocoConstructor() {
        int valor = 1237;

        Troco troco = new Troco(valor);

        Assert.assertNotNull(troco);
    }

    @Test
    public void checkSucessIteratorTrocoConstructor() {
        int valor = 1237;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(6); // 6 * 200 = 1200
        quantidadesEsperadas.add(0); // 0 * 100 = 0
        quantidadesEsperadas.add(0); // 0 * 50 = 0
        quantidadesEsperadas.add(1); // 1 * 20 = 20
        quantidadesEsperadas.add(1); // 1 * 10 = 10
        quantidadesEsperadas.add(1); // 1 * 5 = 5
        quantidadesEsperadas.add(1); // 1 * 2 = 2
        // 1200 + 20 + 10 + 5 + 2 = 1237

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorWithAllTrocoConstructor() {
        int valor = 1387;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(6); // 6 * 200 = 1200
        quantidadesEsperadas.add(1); // 0 * 100 = 100
        quantidadesEsperadas.add(1); // 0 * 50 = 50
        quantidadesEsperadas.add(1); // 1 * 20 = 20
        quantidadesEsperadas.add(1); // 1 * 10 = 10
        quantidadesEsperadas.add(1); // 1 * 5 = 5
        quantidadesEsperadas.add(1); // 1 * 2 = 2
        // 1200 + 100 + 50 + 20 + 10 + 5 + 2 = 1387

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorNota200TrocoConstructor() {
        int valor = 200;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(1);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorNota100TrocoConstructor() {
        int valor = 100;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(1);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorNota50TrocoConstructor() {
        int valor = 50;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(1);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorNota20TrocoConstructor() {
        int valor = 20;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(1);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorNota10TrocoConstructor() {
        int valor = 10;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(1);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorNota5TrocoConstructor() {
        int valor = 5;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(1);
        quantidadesEsperadas.add(0);

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorNota2TrocoConstructor() {
        int valor = 2;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(1);

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorNota0TrocoConstructor() {
        int valor = 0;

        Troco troco = new Troco(valor);
        var iterator = troco.getIterator();

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);
        quantidadesEsperadas.add(0);

        Assert.assertEquals(quantidadesEsperadas, quantidades);
    }

    @Test
    public void checkSucessIteratorConstructorRemove() {
        int valor = 1387;

        var iterator = new Troco.TrocoIterator(new Troco(valor));

        ArrayList<Integer> quantidades = new ArrayList<>();

        while (iterator.hasNext()) {
            PapelMoeda papelMoeda = iterator.next();
            quantidades.add(papelMoeda.getQuantidade());
            iterator.remove();
        }

        ArrayList<Integer> quantidadesEsperadas = new ArrayList<>();
        quantidadesEsperadas.add(6); // 6 * 200 = 1200
        quantidadesEsperadas.add(1); // 0 * 100 = 100
        quantidadesEsperadas.add(1); // 0 * 50 = 50
        quantidadesEsperadas.add(1); // 1 * 20 = 20
        quantidadesEsperadas.add(1); // 1 * 10 = 10
        quantidadesEsperadas.add(1); // 1 * 5 = 5
        quantidadesEsperadas.add(1); // 1 * 2 = 2
        // 1200 + 100 + 50 + 20 + 10 + 5 + 2 = 1387


        Assert.assertEquals(quantidadesEsperadas, quantidades);
        Assert.assertEquals(iterator.hasNext(), false);

        try {
            iterator.next();
        } catch (Exception e){
            Assert.assertEquals(e.getClass(), ArrayIndexOutOfBoundsException.class);}
    }

}
