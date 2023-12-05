#14
#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#Telefonou para a vítima?"
#Esteve no local do crime?"
#Mora perto da vítima?"
#Devia para a vítima?"
#Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será calassificado como "Inocente"""

perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]

acusacoes = {1:"Inocente",2:"Suspeita",3 or 4: "Cúmplice",5:"Assassino"}
contador = 0
print(" vc podererar responder {sim ou s} para[sim] e {não ou n} para[não]")

for i in perguntas:
    while True:
        resposta = input(f"{i}:")
        resposta = resposta.upper()
        if resposta == "SIM" or resposta =="S":
            contador +=1 
            break

        elif resposta == "NAO" or resposta == "N" or resposta == "NÃO":
            pass
            break
        else:
            print("digite sim ou não")