/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package checkingAccount;
import account.Account;
/**
 *
 * @author unifansilva
 */
public class CheckingAccount extends Account{
    protected double taxaTransacao;

    public CheckingAccount(double taxaTransacao, double saldo) {
        super(saldo);
        this.taxaTransacao = taxaTransacao;
    }
    
    @Override
    public void credit(double valor)
    {
        this.saldo -= this.saldo * (this.taxaTransacao/100);
        this.saldo+=valor;
    }
    
    @Override
    public void debit(double valor)
    {
        if(this.saldo - (valor + (this.saldo * (this.taxaTransacao/100))) >= 0)
        {
            this.saldo-=(valor + (this.saldo * (this.taxaTransacao/100)));
        } else
        {
            System.out.println("Impossível realizar a operação, saldo insuficiente...");
        }
    }
    
    
}
