#include<stdlib.h>
#include<iostream>
#include<string.h>
using namespace std;
typedef struct aluno
 {
  char nome[50], curso[50];
  int matricula;
  struct aluno *proximo; 
 }temp;


int main()
{
    temp*primeiro;
    temp*registro;
    primeiro=(temp*)malloc(sizeof(temp));
    if(primeiro==NULL)exit(1);
    registro=primeiro;
    while(1)
    {
    cout<<"\nnome:";
    cin>>registro->nome;
    if(!strcmp(registro->nome,"fim"))break;
    cout<<"\nmatricula:";
    cin>>registro->matricula;
    cout<<"\ncurso:";
    cin>>registro->curso;
    registro->proximo=(temp*)malloc(sizeof(temp));
    registro=registro->proximo;
    }

    registro->proximo=NULL;
    registro=primeiro;
    while(1){
       if(!strcmp(registro->nome,"fim"))break;
       cout<<"\n\nnome :"<<registro->nome;
       cout<<"\nmatricula :"<<registro->matricula;
       cout<<"\ncurso :"<<registro->curso;
       registro=registro->proximo;
    }
    

return 0;
}