
package model;

/**
 *
 * @author dperico
 */
public class Divide extends Calculadora{
    @Override
    public double calcula(double x, double y){
        return (Math.round(x/y*100)/100.0);
    }
}
