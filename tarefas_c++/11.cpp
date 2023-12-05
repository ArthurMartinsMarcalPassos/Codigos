#include <iostream>
#include <stdlib.h>
using namespace std;
 int main ()
 {
struct aluno{

    char nome[50];
    float matricula;
    char curso[50];
};
struct aluno *p;

p=(struct aluno *) malloc(sizeof(aluno));

cout<<"Digite nome:";
cin>>p->nome;
cout<<"Matricula:";
cin>>p->matricula;
cout<<"Digite curso:";
cin>>p->curso;

cout<<p->nome;
cout<<p->matricula;
cout<<p->curso;


return 0;
 }