#include <iostream>
#include <string.h>
#define ARTHUR 15
#define PORJETO 15
using namespace std;

int main()
{
    char produto[PORJETO];
    float valores[ARTHUR], valordevendas[ARTHUR] ;     

    for ( int i = 0; i < 5;  i++)
    {   
        produto[i];
        cout<<"\ndigite um produto:"; 
        cin>>strcpy(produto, "");
        cout<<"\nvalor de compra:";
        cin>>valores[i];
        cout<<"\nvalor de venda:";
        cin>>valordevendas[i];
        cout<<"\n";
        cout<<"\nnome do produto:";
        for (int j = 0; j <strlen(produto); j++ )
        {
            cout<<produto[j];
        
        }
        cout<<"\nvalor: "<<valordevendas[i]; 
        
    }


return 0;
} 
