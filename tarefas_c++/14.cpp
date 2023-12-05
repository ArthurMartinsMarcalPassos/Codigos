#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

int main(){

    struct Aluno{
        char nome[50];
        int matricula;
        char curso[50];
        struct Aluno* proximo;
        struct Aluno* anterior;        
        
    };

    struct Aluno* alunoInicial = (struct Aluno*) malloc(sizeof(struct Aluno));
    struct Aluno* alunoFinal;

    struct Aluno* temp = alunoInicial;
    
    while(true){
        cout <<"Digite o nome do Aluno: ";
        cin >> temp -> nome;
        if((strcmp(temp->nome, "Fim") == 0) || (strcmp(temp->nome, "fim")) == 0)
        {
            break;
        }
        cout <<"Digite a matrícula do Aluno: ";
        cin >> temp -> matricula;
        cout <<"Digite o curso do Aluno: ";
        cin >> temp -> curso;
        cout << "\n";
        
        temp -> proximo = (struct Aluno*) malloc(sizeof(struct Aluno));
        temp -> anterior = alunoFinal;
        alunoFinal = temp;
        temp = temp -> proximo;
    }    
    
    cout << "\n";
    cout << "\n";
    temp = alunoFinal;
    
    while(true){
        if(temp == NULL){
            break;
        }
        cout << "Aluno: " << temp->nome;
        cout << "Matricula: " << temp->matricula;
        cout << "Curso: " << temp->curso;
        temp = temp->anterior;
        
     }
 }