import java.util.Stack;

public class Program12 {
    public static void main(String[] args) {
        // Stack implementation
        Stack<String> stack = new Stack<>();
        stack.push("First");
        stack.push("Second");
        stack.push("Third");

        System.out.println("Stack: " + stack);
        System.out.println("Pop: " + stack.pop());
        System.out.println("Peek: " + stack.peek());
        System.out.println("Stack after pop: " + stack);
    }
}
