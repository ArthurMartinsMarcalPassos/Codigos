#include <iostream>
using namespace std;
 
 int main()
{
    int matricula[5];
    float n1[5], n2[5], media[5], cs;
    do
    {
       for (int i = 0; i < 5; i++)
     {
        cout<<"\ndigite matricula: ";
        cin>>matricula[i];
        cout<<"digite notas:\n"; 
        cin>>n1[i]>>n2[i]; 
        media[i] = (n1[i]+n2[i])/2;
        cout<<"media:\n"<<media[i];
        if (media[i]>=6)
        {
            cout<<"\naprovado";
        }
        else if (media[i]<6)
        {
            cout<<"\nreprovado"; 
        }
     }
     cout<<"\ndigite [0] para sair e [1] para continuar.";
     cin>>cs;
    } while (cs>=1);
    cout<<"Obrigado e adeus!!!";
    
return 0; 
}