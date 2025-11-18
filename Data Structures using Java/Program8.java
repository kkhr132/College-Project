import java.util.HashSet;

public class Program8 {
    public static void main(String[] args) {
        // HashSet for unique elements
        HashSet<String> set = new HashSet<>();
        set.add("Apple");
        set.add("Banana");
        set.add("Apple"); // Duplicate, won't be added

        System.out.println("Set: " + set);
        System.out.println("Contains 'Apple': " + set.contains("Apple"));
        System.out.println("Size: " + set.size());
    }
}
