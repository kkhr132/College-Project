import java.util.ArrayList;

public class Program6 {
    public static void main(String[] args) {
        // ArrayList to store and manipulate integers
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);

        System.out.println("Original list: " + list);

        // Manipulate
        list.remove(1); // Remove index 1
        list.add(1, 25); // Add at index 1

        System.out.println("Modified list: " + list);
        System.out.println("Size: " + list.size());
    }
}
