#include <iostream>;
using namespace std;
int main ()
{
    float peso, altura, imc, cs;
    do
    {
        cout<< "digite seu peso:";
        cin>> peso;
        cout<< "\ndigite sua altura:";
        cin>> altura;
        imc==(altura*2)/peso;
        if (imc<18.5)
        {
        cout<<"vc esta muito magro"<<imc;
        }
        if (imc>=18.5 && imc<24.9)
        {
            cout<<"vc esta normal"<<imc;
        }
        if (imc>=25)
        {
            cout<<"vc precisa imagrecer:"<<imc;
        }
        
        cout<<"\ndigite [0] para sair e [1] para continuar.";
        cin>>cs;
    } while (cs>=1);
    cout<<"Obrigado e adeus!!!";
    
 return 0;
}