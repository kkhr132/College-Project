import java.util.LinkedHashMap;

public class Program13 {
    public static void main(String[] args) {
        // LinkedHashMap maintains insertion order
        LinkedHashMap<String, Integer> map = new LinkedHashMap<>();
        map.put("Three", 3);
        map.put("One", 1);
        map.put("Two", 2);

        System.out.println("LinkedHashMap (insertion order): " + map);
    }
}
