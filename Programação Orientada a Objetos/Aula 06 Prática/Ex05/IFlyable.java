package Ex05;

interface IFlyable{
    default void voar(){
        System.out.println("Voando...");
    }
}