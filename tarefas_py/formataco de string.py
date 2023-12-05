
#variaveis//
nome = "arthur martins" #str
idade = 19 #int
altura = 1.70 #float
e_maior = idade>18 #bool
peso = 66.800 #float
imc = peso / (altura**2)
#formatação//
#print(nome,"tem", idade,"anos de idade e seu imc e", imc)
#print(f'{nome} tem {idade} anos de idade e seu imc e {imc:.2f}')
#print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))
#print('{n} tem {i} anos de idade e seu imc e {im:.2f}'.format(n=nome, i=idade, im=imc))
#formas de fazer input //
#variaver = int(input('str'))
#variavel = input("str")
# variavel = int(variavel)
#.format//
#print( "{:.2f}".format(imc))
#print(f"{nome:s}")
#interpolaçao// 
interpolacao = "%s tem %i de idade seu peso e %.2f." % (nome, idade, peso)
print(interpolacao)
variavel= "abc" 
print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}")
print(f"{variavel: ^11}")
print (f"O hexadecimal de 1500 e {1500:04x}")