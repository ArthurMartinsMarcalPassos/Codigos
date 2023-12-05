import java.util.Scanner;
public class Main
{
   public static void main(String[] args) 
   {
        Scanner scanner = new Scanner(System.in);
        
        int voto;
        int votosJair = 0, votosCarlos = 0, votosNeves = 0, votosNulos = 0, votosBrancos = 0, totalVotos = 0;
        
        do 
        {
            System.out.println("As opções de votos são:");
            System.out.println("1. Candidato Jair Rodrigues");
            System.out.println("2. Candidato Carlos Luz");
            System.out.println("3. Candidato Neves Rocha");
            System.out.println("4. Nulo");
            System.out.println("5. Branco");
            System.out.println("6. Encerrar a votação");
            
            System.out.print("Entre com o seu voto: ");
            voto = scanner.nextInt();
            
            switch (voto) 
            {
                case 1:
                    votosJair++;
                    totalVotos++;
                    break;
                case 2:
                    votosCarlos++;
                    totalVotos++;
                    break;
                case 3:
                    votosNeves++;
                    totalVotos++;
                    break;
                case 4:
                    votosNulos++;
                    totalVotos++;
                    break;
                case 5:
                    votosBrancos++;
                    totalVotos++;
                    break;
                case 6:
                    System.out.println("Encerrando a votação...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
            
        } while (voto != 6);
        
        System.out.println("Resultados:");
        System.out.println("Votos para Candidato Jair Rodrigues: " + votosJair);
        System.out.println("Votos para Candidato Carlos Luz: " + votosCarlos);
        System.out.println("Votos para Candidato Neves Rocha: " + votosNeves);
        System.out.println("Votos Nulos: " + votosNulos);
        System.out.println("Votos Brancos: " + votosBrancos);
        
        double percentualNulos = (double) votosNulos / totalVotos * 100;
        double percentualBrancos = (double) votosBrancos / totalVotos * 100;
        
        System.out.println("Porcentagem de votos nulos: " + percentualNulos + "%");
        System.out.println("Porcentagem de votos brancos: " + percentualBrancos + "%");
        
        String candidatoVencedor = "Nenhum";
        
        if (votosJair > votosCarlos && votosJair > votosNeves) 
        {
            candidatoVencedor = "Jair Rodrigues";
        } else if (votosCarlos > votosJair && votosCarlos > votosNeves) 
        {
            candidatoVencedor = "Carlos Luz";
        } else if (votosNeves > votosJair && votosNeves > votosCarlos) 
        {
            candidatoVencedor = "Neves Rocha";
        }
        
        System.out.println("Candidato vencedor: " + candidatoVencedor);
        
    }
}   