/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package main;
import savingAccount.SavingAccount;
import checkingAccount.CheckingAccount;
/**
 *
 * @author unifansilva
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        SavingAccount save = new SavingAccount(1.22, 5000);
        CheckingAccount check = new CheckingAccount(1,1000);
        
        save.credit(1000);
        save.getBalance();
        save.debit(6000);
        save.getBalance();

        check.credit(1000);
        check.getBalance();
        check.debit(5000);
        check.getBalance();
   
    }
    
}
