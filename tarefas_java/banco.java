import java.util.Scanner;
public class Main
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        
        double saldo = 0.0;
        char opcao;
        
        do 
        {
            System.out.println("Menu:");
            System.out.println("a) Consultar Saldo");
            System.out.println("b) Realizar Saque");
            System.out.println("c) Realizar Depósito");
            System.out.println("d) Sair");
            
            System.out.print("Escolha uma opção: ");
            opcao = scanner.next().charAt(0);
            
            switch (opcao) 
            {
                case 'a':
                    System.out.println("Saldo atual: R$ " + saldo);
                    break;
                case 'b':
                    System.out.print("Digite o valor do saque: ");
                    double saque = scanner.nextDouble();
                    if (saque > 0 && saque <= saldo) 
                    {
                        saldo -= saque;
                        System.out.println("Saque realizado com sucesso.");
                    } else 
                    {
                        System.out.println("Saldo insuficiente ou valor inválido.");
                    }
                    break;
                case 'c':
                    System.out.print("Digite o valor do depósito: ");
                    double deposito = scanner.nextDouble();
                    if (deposito > 0) 
                    {
                        saldo += deposito;
                        System.out.println("Depósito realizado com sucesso.");
                    } else 
                    {
                        System.out.println("Valor de depósito inválido.");
                    }
                    break;
                case 'd':
                    System.out.println("Encerrando o programa...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
            
        } while (opcao != 'd');
        {
           System.out.println("Adeus!!!");
        }
        
    }    
}


