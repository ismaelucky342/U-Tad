// Componente base
public interface Shape {
    void draw();
    void resizeByPercentage(double pct);
}

// Implementación concreta
public class Circle implements Shape {
    private double x, y, radius;

    public Circle(double x, double y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    @Override
    public void draw() {
        System.out.println("Circle at (" + x + ", " + y + ") with radius " + radius);
    }

    @Override
    public void resizeByPercentage(double pct) {
        radius *= (1.0 + pct / 100.0);
    }

    public double getX() { return x; }
    public double getY() { return y; }
    public double getRadius() { return radius; }
}

// Decorador base
public abstract class ShapeDecorator implements Shape {
    protected Shape decoratedShape;

    public ShapeDecorator(Shape decoratedShape) {
        this.decoratedShape = decoratedShape;
    }

    @Override
    public void draw() {
        decoratedShape.draw();
    }

    @Override
    public void resizeByPercentage(double pct) {
        decoratedShape.resizeByPercentage(pct);
    }
}

// Decorador concreto: ConsoleDrawing
public class ConsoleDrawingDecorator extends ShapeDecorator {
    public ConsoleDrawingDecorator(Shape decoratedShape) {
        super(decoratedShape);
    }

    @Override
    public void draw() {
        if (decoratedShape instanceof Circle) {
            Circle c = (Circle) decoratedShape;
            System.out.println("Drawing circle at (" + c.getX() + ", " + c.getY() + ") with radius " + c.getRadius());
        } else {
            decoratedShape.draw();
        }
    }
}

// Decorador concreto: SVGDrawing
public class SVGDrawingDecorator extends ShapeDecorator {
    public SVGDrawingDecorator(Shape decoratedShape) {
        super(decoratedShape);
    }

    @Override
    public void draw() {
        if (decoratedShape instanceof Circle) {
            Circle c = (Circle) decoratedShape;
            System.out.println("<circle cx=\"" + c.getX() + "\" cy=\"" + c.getY() + "\" r=\"" + c.getRadius() + "\" />");
        } else {
            decoratedShape.draw();
        }
    }
}

// Main
public class Main {
    public static void main(String[] args) {
        Shape circle1 = new ConsoleDrawingDecorator(new Circle(1, 2, 3));
        Shape circle2 = new SVGDrawingDecorator(new Circle(5, 7, 11));

        Shape[] shapes = new Shape[] { circle1, circle2 };

        for (Shape shape : shapes) {
            shape.resizeByPercentage(10);
            shape.draw();
        }
    }
}