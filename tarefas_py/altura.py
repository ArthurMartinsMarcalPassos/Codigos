#12
#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
#quantas alunos com mais 13 anos tem aluturaa inserior a media

contador = 0
idade = [10, 15, 9, 22, 13, 12, 14]
altura = [1.69, 1.45, 1.56, 1.98, 1.66, 1.80, 1.90]

media = sum(altura)/5


for i in range(len(idade)):

    if idade[i] > 13 and altura[i] < media:
        contador +=1

print(f"tem {contador} alunos a baixo da media ")