public class Program3 {
    // Inner class
    static class InnerClass {
        public void display() {
            System.out.println("Inside inner class");
        }
    }

    public static void main(String[] args) {
        // Exception handling
        try {
            int result = 10 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Caught exception: " + e.getMessage());
        } finally {
            System.out.println("Finally block executed");
        }

        // Usage of inner class
        InnerClass inner = new InnerClass();
        inner.display();
    }
}
