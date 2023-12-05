#include <iostream>
using namespace std; 
int main()
{
 int coluna;
 float produtos[10];
//entrada//
 for(coluna=0; coluna<10;coluna++)
 {
    cout<<"digite produto: ";
    cin>>produtos[coluna];
 }
 //saida//]
  cout<<"valor do produto";
 for (coluna=0; coluna<10; coluna++)
 {
    produtos[coluna] = produtos[coluna]*2;
    cout<<"\n"<<produtos[coluna];
 }
   return 0;
}
