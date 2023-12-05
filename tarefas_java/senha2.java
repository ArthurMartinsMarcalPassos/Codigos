import java.util.Scanner;
public class Main
{

    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Crie uma senha de quatro dígitos: ");
        final String senhaCorreta = scanner.nextLine();
        
        boolean senhaCorretaDigitada = false;
        
        while (!senhaCorretaDigitada) 
        {
            System.out.print("Digite a senha de quatro dígitos: ");
            String senhaDigitada = scanner.nextLine();
            
            if (senhaDigitada.equals(senhaCorreta)) 
            {
                System.out.println("Senha Correta");
                senhaCorretaDigitada = true;
            } else 
            {
                System.out.println("Senha Incorreta. Tente novamente.");
            }
        }
        
        scanner.close();
    }
}

