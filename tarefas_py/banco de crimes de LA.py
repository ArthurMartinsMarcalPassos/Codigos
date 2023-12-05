print("banco de crimes de LA")
pergunta=input("vc recebeu alguma ligacao da vitima ?: ")
if pergunta=="sim":
    pergunta = 1
elif pergunta == "nao":
    pergunta = 0
pergunta2 =input("vc estava na cena do crime ?: ")
if pergunta2=="sim":
    pergunta2 = 1
elif pergunta2 == "nao":
    pergunta2 = 0
pergunta3 =input("vc mora perto da vitima ?: ")
if pergunta3=="sim":
    pergunta3 = 1
elif pergunta3 == "nao":
    pergunta3 = 0
pergunta4 = input("vc tinha alguma divida com a vitima ?: ")
if pergunta4=="sim":
    pergunta4 = 1
elif pergunta4 == "nao":
    pergunta4 = 0
pergunta5= input("vc esteve trabalhando com a vitima  ?: ")
if pergunta5=="sim":
    pergunta5 = 1
elif pergunta5 == "nao":
    pergunta5 = 0
print("ok\n")
case = pergunta + pergnuta2 + pergunta3 + pergunta4 + pergunta5
if case == 5:
    print("vc e o assasino?")
elif case == 4 or case== 3:
    print("suspeito")
elif case == 1 or case == 2 :
    print("Inocente") 