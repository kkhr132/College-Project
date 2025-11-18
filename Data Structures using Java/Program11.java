import java.util.PriorityQueue;

public class Program11 {
    public static void main(String[] args) {
        // PriorityQueue as min heap
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(30);
        pq.add(10);
        pq.add(20);

        System.out.println("PriorityQueue: " + pq);
        System.out.println("Poll (min): " + pq.poll());
        System.out.println("After poll: " + pq);
    }
}
