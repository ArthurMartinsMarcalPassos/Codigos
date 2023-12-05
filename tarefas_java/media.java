import java.util.Scanner;
public class Main
{
    public static void main(String[] args) 
  {
        Scanner scanner = new Scanner(System.in);
        
        final int numNotas = 10;
        double[] notas = new double[numNotas];
        
        for (int i = 0; i < numNotas; i++) 
        {
            System.out.print("Digite a nota " + (i + 1) + ": ");
            notas[i] = scanner.nextDouble();
        }
        
        double soma = 0;
        for (double nota : notas) 
        {
            soma += nota;
        }
        
        double media = soma / numNotas;
        
        System.out.println("Média das notas: " + media);
        
        
    }
}  

