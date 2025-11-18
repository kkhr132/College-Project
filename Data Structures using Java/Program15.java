import java.util.TreeMap;

public class Program15 {
    public static void main(String[] args) {
        // TreeMap stores elements sorted by keys
        TreeMap<String, Integer> map = new TreeMap<>();
        map.put("Banana", 2);
        map.put("Apple", 1);
        map.put("Cherry", 3);

        System.out.println("TreeMap (sorted by keys): " + map);
    }
}
