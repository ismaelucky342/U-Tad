public interface DrawinbggAPI {
    void drawCircle(int radius, int x, int y);
}

public class ConsoleDrawingAPI implements DrawingAPI {
    @Override
    public void drawCircle(int radius, int x, int y) {
        System.out.println("Drawing circle at (" + x + ", " + y + ") with radius " + radius);
    }
}

public class SVGDrawingAPI implements DrawingAPI {
    @Override
    public void drawCircle(double x, double y, double radius) {
        System.out.println("<circle cx=\"" + x + "\" cy=\"" + y + "\" r=\"" + radius + "\" />");
    }
}

public abstract class Shape {
    protected DrawingAPI drawingAPI;

    protected Shape(DrawingAPI drawingAPI) {
        this.drawingAPI = drawingAPI;
    }

    public abstract void draw();     // delega en DrawingAPI
    public abstract void resizeByPercentage(double pct);
}

public class Circle extends Shape {
    private double x, y, radius;

    public Circle(double x, double y, double radius, DrawingAPI drawingAPI) {
        super(drawingAPI);
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    @Override
    public void draw() {
        drawingAPI.drawCircle(x, y, radius);
    }

    @Override
    public void resizeByPercentage(double pct) {
        radius *= (1.0 + pct / 100.0);
    }
}

public class Main {
    public static void main(String[] args) {
        Shape[] shapes = new Shape[] {
            new Circle(1, 2, 3, new ConsoleDrawingAPI()),
            new Circle(5, 7, 11, new SVGDrawingAPI())
        };

        for (Shape shape : shapes) {
            shape.resizeByPercentage(10);
            shape.draw();
        }
    }
}