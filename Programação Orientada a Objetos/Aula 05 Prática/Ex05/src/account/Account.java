/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package account;

/**
 *
 * @author unifansilva
 */
public class Account {
    protected double saldo;

    public Account(double saldo) {
        if(saldo < 0){
            this.saldo = 0;
        }
        else
        {
           this.saldo = saldo;
        }
    }
    
    public void credit(double valor)
    {
        this.saldo += valor;
    }
    
    public void debit(double valor)
    {
        if(this.saldo - valor >= 0)
        {
            this.saldo-=valor;
        } else
        {
            System.out.println("Impossível realizar a operação, saldo insuficiente...");
        }
    }
    
    public void getBalance()
    {
        System.out.println("==========================");        
        System.out.println("Saldo atual: " + this.saldo);    
    }
    
    
}
