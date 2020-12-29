/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Ex06;

/**
 *
 * @author unifansilva
 */
public class ContaCorrente {
    private double saldo;

    public ContaCorrente(double saldo) {
        this.saldo = saldo;
    }

    public ContaCorrente() {
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    
    public void sacar(double valor)
    {
        this.saldo -= valor;
    }
    
    public void depositar(double valor)
    {
        this.saldo += valor;
    }
    
}
