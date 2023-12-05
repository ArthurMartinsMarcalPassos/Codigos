nome = (input("Digite seu nome: "))
idade = (input("Digite sua idade: "))
if nome and idade:
    print(f"Seu nome e {nome} sau idade e {idade}.")
    print(f"Seu nome invertido de {nome[::-1]}")
    if" "in nome:
        print("Seu nome contem espaço(s)")
    else:
        print("seu nome não contem espaço")
    print(f"A pirmeira letra do seu nome e {nome[0]}")
    print(f"A ultima letra do seu nome e {nome[-1]}")
    print(f"Seu nome tem {len(nome)} letras")
else:
    print("Desculpa vc deixou os campos vazios.")   
    
 