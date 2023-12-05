#include <iostream>
#include <locale.h>
using namespace std;

int main()
{
    setlocale(LC_ALL,"Portuguese");
    int matriz[5][5], i, j, cs;
    //for 1 = a linha//
    do
    {
        cout<<"\nPrencha a Matriz:";
    for (i = 0; i <5; i++)
    {
        //for 2 = a coluna//
      for ( j = 0; j <5; j++)
      {
         cin>>matriz[i][j];
         cout<<"\t"<<matriz[i][j];
      }
      cout<<"\n";
    }
    //saida da digonal//
    cout<<"Diagonal: ";
    for ( i = 0; i <5; i++)
    {
        for (j = 0; j <5; j++)
        {
            if(i==j)
            {
                cout<<matriz[i][j]<<"; ";
            }

        }
        
    }
    cout<<";)";
    cout<<"\ndigite [0] para sair e [1] para continuar.";
    cin>>cs;
    } while (cs>=1);
    cout<<"Obrigado e adeus!!!";
    
    
   



return 0;
}