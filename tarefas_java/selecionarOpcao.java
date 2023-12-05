import java.util.Scanner;
public class Main
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        
        int opcao;
        
        do {
            System.out.println("Menu de Opções:");
            System.out.println("1 - Imprimir o número 1");
            System.out.println("0 - Imprimir o número 0");
            System.out.println("-1 - Encerrar o programa");
            
            System.out.print("Digite sua opção: ");
            opcao = scanner.nextInt();
            
            if (opcao == 1 || opcao == 0) 
            {
                System.out.println("Opção escolhida: " + opcao);
            } else if (opcao == -1) 
            {
                System.out.println("Encerrando o programa...");
            } else 
            {
                System.out.println("Opção inválida. Tente novamente.");
            }
        } while (opcao != -1);
        {
            System.out.println("Adeus!!!");
        }
        
    }
}