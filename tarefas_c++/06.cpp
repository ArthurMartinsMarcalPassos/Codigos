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
        cout<<"\nPrencha a M�triz:";
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
    } while (cs>=1);
    cout<<"Adeus";
    
    
   



return 0;
}