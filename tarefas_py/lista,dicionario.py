cor= {"green" : "verde","blue": "azul","red":"vermelho"}
print(cor)
print(cor["green"])
cor["yellow"]="amarelo"
print(cor)
cor["green"] = "sapo"
print(cor)
del cor["green"]
print(cor)
pessoa = { "nome":"arthur","idade":"19","profissao":"aluno" }
pessoatupla=("arthur","19","aluno")

al1=int(input("digite sua idade\n"))
al2=int(input("digite sua idade\n"))
al3=int(input("digite sua idade\n"))

idades=[al1,al2,al3]
print(idades)
soma=sum (idades)
print(soma/len(idades))

def imprimiranos (idades):
  print(idades)
imprimiranos

def arearetangulo(lado, altura):
    area = lado*altura
    return print (area)
arearetangulo(3, 8)