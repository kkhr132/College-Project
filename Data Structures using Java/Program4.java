import java.util.ArrayList;
import java.util.List;

// Interface
interface Shape {
    double area();
    void draw();
}

// Implementing class
class Circle implements Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public void draw() {
        System.out.println("Drawing a circle");
    }
}

public class Program4 {
    public static void main(String[] args) {
        // Using interface
        Shape circle = new Circle(5.0);
        System.out.println("Area: " + circle.area());
        circle.draw();

        // Abstract data types using collections
        List<Shape> shapes = new ArrayList<>();
        shapes.add(new Circle(3.0));
        shapes.add(new Circle(4.0));

        for (Shape s : shapes) {
            System.out.println("Shape area: " + s.area());
        }
    }
}
