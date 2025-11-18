import java.util.ArrayList;
import java.util.List;

// Generic class
class Container<T> {
    private T item;

    public Container(T item) {
        this.item = item;
    }

    public T getItem() {
        return item;
    }

    public void setItem(T item) {
        this.item = item;
    }
}

// Base class
class Animal {
    public void makeSound() {
        System.out.println("Animal sound");
    }
}

// Subclass overriding method
class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof");
    }
}

public class Program2 {
    public static void main(String[] args) {
        // Polymorphism: method overriding
        Animal animal = new Dog();
        animal.makeSound(); // Calls Dog's makeSound

        // Generics usage
        Container<String> stringContainer = new Container<>("Hello");
        Container<Integer> intContainer = new Container<>(123);

        System.out.println("String: " + stringContainer.getItem());
        System.out.println("Integer: " + intContainer.getItem());

        // Generic list
        List<String> list = new ArrayList<>();
        list.add("Polymorphism");
        list.add("Generics");
        System.out.println("List: " + list);
    }
}
