// Square.java
public class Square implements GeometricArea {

     private Double side;
     private Double area;

     public Square() {
          this(0.0);
     }

     public Square(Double side) {
          this.side = side;
          this.area = calculateArea();
     }

     private Double calculateArea() {
          return new ContextAreaStrategy(new SquareAreaStrategy()).calculaArea(this.side);
     }

     public Double getSide() {
          return side;
     }

     public Double getArea() {
          return area;
     }

     @Override
     public String toString() {
          return String.format("Square[side(%.2f), area(%.2f)]", side, area);
     }
}
