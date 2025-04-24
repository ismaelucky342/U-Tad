import java.util.ArrayList;

// Abstract class Shape with an abstract method to calculate area
abstract class Shape {
    abstract double calculateArea();
}

// Rectangle class, a subclass of Shape
class Rectangle extends Shape {
    double base; // Base of the rectangle
    double height; // Height of the rectangle

    // Constructor for the Rectangle class
    Rectangle(double base, double height) {
        this.base = base;
        this.height = height;
    }

    // Method to calculate area (base * height)
    double calculateArea() {
        return base * height;
    }
}

// Circle class, another subclass of Shape
class Circle extends Shape {
    double radius; // Radius of the circle

    // Constructor for the Circle class
    Circle(double radius) {
        this.radius = radius;
    }

    // Method to calculate area (π * r²)
    double calculateArea() {
        return Math.PI * radius * radius;
    }
}

// Main class containing the main method
public class Exercise1 {
    public static void main(String[] args) {
        ArrayList<Shape> shapes = new ArrayList<>(); // List of shapes

        shapes.add(new Rectangle(3, 4)); // Add a rectangle with base 3 and height 4
        shapes.add(new Circle(5)); // Add a circle with radius 5

        double totalArea = 0; // Variable to store the total area

        // Iterate over the shapes and calculate the total area
        for (Shape shape : shapes) {
            totalArea += shape.calculateArea();
        }

        // Print the total area
        System.out.println(totalArea);
    }
}