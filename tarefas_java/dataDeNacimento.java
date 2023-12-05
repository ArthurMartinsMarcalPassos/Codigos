import java.util.Scanner;
public class Main
{
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        System.out.println("Quando vc nasceu?");
        int anoNace = sc.nextInt();
        int idade = 2023 - anoNace ;
        System.out.println("sua idade e " + idade);
    }

}
