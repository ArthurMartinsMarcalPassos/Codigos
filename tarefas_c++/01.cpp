#include <iostream>
#include <stdlib.h>
using namespace std;

int main ()
{
 do
 {
   struct alunos
   {
      char nome[50];
      float matricula;
      char curso[50];   
   };
   struct alunos turma[1];
   struct alunos*p;
   int i;
   
   
   p=(struct alunos*)malloc(sizeof(struct alunos));
   if (!p)
   {
    cout<<"try agin!!!"
    exit(1);
   }
   cout<<"\ndigite o nome do aluno:";
   cin>>p->nome;
   cout<<"\ndigite a matricula do aluno:"
   cin>>p->matricula;
   cout<<"\ndigite o curso do aluno:";
   cin>>p->curso;
   
   cout<<"\nnome do aluno:";
   cout<<p->nome;
   cout<<"\nmatricula do aluno:";
   cout<<p->matricula;
   cout<<"\ncurso do aluno:"
   cout<<p->curso;
   }while (1);
 
 return 0;

}