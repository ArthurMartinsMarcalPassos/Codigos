import java.util.Scanner;
public class Main
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        
        final int senhaCorreta = 1234;  
        
        while (true) {
            System.out.print("Digite a senha de quatro dígitos: ");
            int senhaDigitada = scanner.nextInt();
            
            if (senhaDigitada == senhaCorreta) {
                System.out.println("Senha Correta");
                break;  
            } else {
                System.out.println("Senha Incorreta. Tente novamente.");
            }
        }
        
    }
}
