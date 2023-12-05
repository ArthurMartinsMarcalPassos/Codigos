import java.util.Scanner;
public class Main
{
    
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Insira um numero: ");
        int n = scanner.nextInt();
        
        int contador = 0;
        while (contador <= n)
        {
            System.out.println(contador);
            contador++;
        }
        
        scanner.close();
    }
}