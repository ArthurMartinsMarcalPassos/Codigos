#progeto contas
emails=[]
senhas=[]
entrada=input("criar conta, logar ou sair?: ")
entrada = entrada.upper()
if entrada == "CRIAR CONTA" and "C":
    email=(input("digite email!!"))
    senha=(input("digite senha!!"))
    emails.append(email)
    senhas.append(senha)
elif entrada=="LOGAR"and "L":
    email=(input("digite email!!"))
    senha=(input("digite senha!!"))
else:
    print("Adeus!!!" )