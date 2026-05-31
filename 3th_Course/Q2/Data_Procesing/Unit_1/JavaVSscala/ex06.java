public class Rectangle {
    private final double width;
    private final double height;

    // Constructor
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

// Método para calcular el área
    public double area() {
        return width * height;
    }

    // Getters
    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }
}

// Llamada en Java
Rectangle rect = new Rectangle(5.0, 10.0);
System.out.println("Area: " + rect.area());