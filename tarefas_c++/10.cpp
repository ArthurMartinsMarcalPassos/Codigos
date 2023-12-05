#include <iostream>
using namespace std;
#include <stdlib.h>
#include <string.h>
int main() {
    struct alunos {
        char nome[50];
        float matricula;
        char curso[50];
        struct alunos *proximo;
        
    };
        struct alunos *primeiro;
        struct alunos *temp;
        struct alunos *temp2;
        primeiro = (struct alunos*)malloc(sizeof(struct alunos));
        primeiro->proximo=temp;
        temp = (struct alunos*)malloc(sizeof(struct alunos));
        temp->proximo=temp2;
        temp2 = (struct alunos*)malloc(sizeof(struct alunos));
        temp2-> proximo = temp;

    
do {
        if (!p) {
            cout<<"não foi boy, deu ruim!";
            exit(1);
        }
        cout<<"\nDigite o seu nome: ";
        cin>>p->nome;
        char *out;
        out = strstr("fim", p->nome);
        if(out) {
            cout<<"\nHASTA LA VISTA BABY!\nTHE END...";
            exit(1);
        }
        cout<<"Digite a sua matricula: ";
        cin>>p->matricula;
        cout<<"Digite o seu curso: ";
        cin>>p->curso;

        cout<<"\nNome: "<<p->nome;
        cout<<"\nMatricula: "<<p->matricula;
        cout<<"\nCurso: "<<p->curso;
            
    } while(1);
    return 0; 
}