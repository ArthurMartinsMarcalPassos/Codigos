#5
#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,valordoproduto):
    calculo1 = (taxaImposto*valordoproduto)/100
    return calculo1 + valordoproduto

impostos = float(input("digite a porcentagem do imposto,sem o simbolo: "))
produto =  float(input("digite o preco do produto"))
result = somaImposto(impostos,produto)
print(f"seu produto com valor somado aos impostos e {result}")