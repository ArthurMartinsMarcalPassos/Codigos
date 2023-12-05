#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
using namespace std;

 bool fim(char *nome){
    if(strcmp(nome,"fim")==0||strcmp(nome,"FIM")==0||strcmp(nome,"f")==0||strcmp(nome,"F")==0){
        return true;
    }else return false;
}

typedef struct Aluno{
    char nome[50],curso[50];
    int matricula;
    struct Aluno *proximo;
}temp;

int main(){
    
    temp * ini_aluno;
    temp *proximo_aluno;
    ini_aluno=(temp *)malloc(sizeof(temp));
    
    if(ini_aluno==NULL)exit(1);
     
    proximo_aluno=ini_aluno; 
    
    while(true){//Entrada de dados
        cout<<"Digite nome: ";
        cin>>proximo_aluno->nome;
        if(fim(proximo_aluno->nome))break;
        cout<<"Diigte a matricula: ";
        cin>>proximo_aluno->matricula;
        cout<<"Diigte o curso: ";
        cin>>proximo_aluno->curso;
        system("cls");
        proximo_aluno->proximo=(temp*)malloc(sizeof(temp));
        proximo_aluno=proximo_aluno->proximo;
    }
    
    proximo_aluno->proximo=NULL;
    proximo_aluno=ini_aluno;
    
    while(proximo_aluno != NULL){
        if(fim(proximo_aluno->nome))break;
        cout<<"\n\nNome: "<<proximo_aluno->nome;
        cout<<"\nMatricula: "<<proximo_aluno->matricula;
        cout<<"\ncurso: "<<proximo_aluno->curso;
        proximo_aluno=proximo_aluno->proximo;    
    }
}