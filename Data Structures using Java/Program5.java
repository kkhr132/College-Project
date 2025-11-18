class Parent {
    private int value;

    public Parent(int value) {
        this.value = value;
    }

    public void display() {
        System.out.println("Parent value: " + value);
    }
}

class Child extends Parent {
    private String name;

    public Child(int value, String name) {
        super(value); // Super constructor
        this.name = name;
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Child name: " + name);
    }
}

public class Program5 {
    public static void main(String[] args) {
        // Type checking and casting
        Parent parent = new Child(10, "Test");
        if (parent instanceof Child) {
            Child child = (Child) parent; // Casting
            child.display();
        }

        // Super constructor usage
        Child child2 = new Child(20, "Another");
        child2.display();
    }
}
