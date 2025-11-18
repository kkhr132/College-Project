public class Program1 {
    // Instance variables
    private int number;
    private String text;

    // Constructor
    public Program1(int number, String text) {
        this.number = number;
        this.text = text;
    }

    // Method
    public void display() {
        System.out.println("Number: " + number + ", Text: " + text);
    }

    public static void main(String[] args) {
        // Primitive types and operators
        int a = 10;
        int b = 5;
        System.out.println("Arithmetic: " + (a + b));
        System.out.println("Comparison: " + (a > b));

        // Object creation (memory allocation on heap)
        Program1 obj = new Program1(42, "Hello World");
        obj.display();
    }
}
