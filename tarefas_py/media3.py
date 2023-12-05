nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
media = (nota1+nota2)/2
if media<=5:
    print(f"sua media e :{media:.2f}")
    print("reprovado")
elif media>=6 and media<=8:
    print(f"sua media e :{media:.2f}")
    print("aprovado")
else:
    print(f"sua media e :{media:.2f}")
    print("aprovado distinçao")