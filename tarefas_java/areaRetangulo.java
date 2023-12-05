import java.util.Scanner;
public class Main
{
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        System.out.println("base do retangulo?");
        int base = sc.nextInt();
        System.out.println("altura do retangulo?");
        int altura = sc.nextInt();
        int area = base * altura ;
        System.out.println("a area do retangulo e : " + area);
    }

}