'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma,
a multiplicação e os números..'''

vetor=[]
for i in range(5):
    numero=input(f"{i+1} numero")
    if numero.isnumeric():
        numero=int(numero)
        vetor.append(numero)
soma=sum(vetor)
mul=1
for i in vetor:
    mul=mul*i
print(f"a soma do vetor e :{soma}\nA multilicacao e: {mul}\nOs numeros do vetor sao: {vetor}")