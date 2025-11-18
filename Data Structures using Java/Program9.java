import java.util.HashMap;

public class Program9 {
    public static void main(String[] args) {
        // HashMap for key-value pairs
        HashMap<String, Integer> map = new HashMap<>();
        map.put("One", 1);
        map.put("Two", 2);
        map.put("Three", 3);

        System.out.println("Map: " + map);
        System.out.println("Value for 'Two': " + map.get("Two"));
        System.out.println("Contains key 'Four': " + map.containsKey("Four"));
    }
}
