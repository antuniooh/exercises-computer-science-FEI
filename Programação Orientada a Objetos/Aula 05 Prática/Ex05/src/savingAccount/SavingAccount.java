/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package savingAccount;
import account.Account;
/**
 *
 * @author unifansilva
 */
public class SavingAccount extends Account{
    protected double taxaJuros;

    public SavingAccount(double taxaJuros, double saldo) {
        super(saldo);
        this.taxaJuros = taxaJuros;
    }
    
    public double calculateInterest()
    {
        return this.taxaJuros * this.saldo;
    }
}
