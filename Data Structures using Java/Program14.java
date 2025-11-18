import java.util.ArrayDeque;
import java.util.Deque;

public class Program14 {
    public static void main(String[] args) {
        // ArrayDeque as deque
        Deque<String> deque = new ArrayDeque<>();
        deque.addFirst("First");
        deque.addLast("Last");
        deque.addFirst("New First");

        System.out.println("Deque: " + deque);
        System.out.println("Remove first: " + deque.removeFirst());
        System.out.println("After remove: " + deque);
    }
}
