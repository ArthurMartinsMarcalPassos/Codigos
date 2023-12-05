import java.util.Scanner;
public class Main
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        char resposta;
        do 
        {
            System.out.print("Digite o primeiro número: ");
            int num1 = scanner.nextInt();
            
            System.out.print("Digite o segundo número: ");
            int num2 = scanner.nextInt();
            
            int soma = num1 + num2;
            System.out.println("A soma de " + num1 + " + " + num2 + " é: " + soma);
            
            System.out.print("Deseja continuar (S/N): ");
            resposta = scanner.next().charAt(0);
        } while (resposta != 'N' && resposta != 'n');
        {
          System.out.print("Adeus!!!");
        }
    }
}