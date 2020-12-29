public class Main {

   public static void main(String[] args) {
      
      ShapeFactory shapeFactory = new ShapeFactory();
     
      //get an object of Circle and call its draw method.
      Shape shape = shapeFactory.getShape("CIRCLE");
      //call draw method of Circle
      shape.draw();

      //get an object of Rectangle and call its draw method.
      shape = shapeFactory.getShape("RECTANGLE");
      //call draw method of Rectangle
      shape.draw();
   }
}