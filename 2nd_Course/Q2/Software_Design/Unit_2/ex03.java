public class Square implements GeometricArea {

     private Double side; 

     private Double area; 

     public Square() { 

          this(0.0); 

     } 

     public Square(Double side) { 

          super(); 

          this.side = side; 

          this.area = new ContextAreaStrategy(

new SquareAreaStrategy()).

                               calculaArea(this.side);

     } 

     public Double getSide() { 

          return side; 

     } 

     public Double getArea() { 

          return this.area; 

     } 

     @Override

     public String toString() { 

          return "Square[side("+this.side+"),area("+this.area+")]"; 

     } 

}

import com.utad.inso.diso.strategy.area.CircleAreaStrategy;

import com.utad.inso.diso.strategy.area.ContextAreaStrategy;

 

public class Circle implements GeometricArea { 

     private Double radius; 

     private Double area; 

     public Circle() { 

          this(0.0); 

     } 

     public Circle(double radius) {

          super(); 

          this.radius = radius; 

          this.area = new ContextAreaStrategy ( 

new CircleAreaStrategy()).

                                     calculaArea(this.radius);

     } 

     public Double getRadius() { 

          return this.radius; 

     } 

     public Double getArea() { 

          return this.area; 

     } 

 
	
     @Override 

     public String toString() { 

          return "Circle [ radius ( "+ this.radius + "), 

area (" + this.area +")]"; 

     } 

     public static void main(String[] args) {  

          Circle circleExample = new Circle(1); 

          System.out.println(circleExample); 

     } 

}