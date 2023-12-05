import java.util.Scanner;
public class Main
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Insira um número: ");
        int n = scanner.nextInt();
        
        System.out.println("Números pares de 0 até " + n + ":");
        for (int i = 0; i <= n; i += 2)
        {
            System.out.println(i);
        }
        
    }
}






