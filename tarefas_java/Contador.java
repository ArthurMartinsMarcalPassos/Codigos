public class Contador {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        for (int i = 0; i <= 1000; i++) {
            System.out.println(i);
        }
        long endTime = System.nanoTime();
        long duration = (endTime - startTime) / 1000000;
    }
}
