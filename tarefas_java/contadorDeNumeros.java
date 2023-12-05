import java.util.Scanner;
public class Main
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        
        int contador = 0;
        double soma = 0;
        
        while (true) 
        {
            System.out.print("Digite um número (0 para sair): ");
            double numero = scanner.nextDouble();
            
            if (numero == 0) 
            {
                break; 
            }
            
            if (numero > 0) {
                contador++;
                soma += numero;
            } else 
            {
                System.out.println("Número inválido. Digite um número maior que zero.");
            }
        }
        
        if (contador > 0) {
            double media = soma / contador;
            System.out.println("Foram lidos " + contador + " números.");
            System.out.println("A média dos números é: " + media);
        } else 
        {
            System.out.println("Nenhum número válido foi lido.");
        }
    }
}
