import java.util.LinkedList;
import java.util.Queue;

public class Program7 {
    public static void main(String[] args) {
        // LinkedList as queue
        Queue<String> queue = new LinkedList<>();
        queue.add("First");
        queue.add("Second");
        queue.add("Third");

        System.out.println("Queue: " + queue);
        System.out.println("Poll: " + queue.poll());
        System.out.println("After poll: " + queue);
    }
}
