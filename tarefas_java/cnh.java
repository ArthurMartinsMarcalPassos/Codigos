import java.util.Scanner;
public class Main
{
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        System.out.println("Seu nome?");
        String nome = sc.next();
        
        if (id >= 18) 
        {
           System.out.println(nome +" vc pode ter CNH" ); 
        } else {
            System.out.println(nome +" vc n pode ter CNH" );
        }
    }

}