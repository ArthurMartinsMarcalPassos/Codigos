#include <iostream>
using namespace std;
int main()

{
  float media, av1, av2, avd;
    
    cout<<"\n insira nota av1:";
    cin>>av1;
    cout<<"\n insira nota av2:";
    cin>>av2;
    cout<<"\n insira nota avd:";
    cin>>avd;
    media=(av1+av2+avd)/3;
    cout<<"\nmedia:";
    cout<<media;

   if (media >= 6)
  
    {
     cout<<"\naprovado;)";
    }
   else if(media <6)
    {
     cout<<"\nreprovdo:(";
    }
return 0;
}