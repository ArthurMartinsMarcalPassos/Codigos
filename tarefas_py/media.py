nota1=float(input("nota da prova 01:"))
nota2=float(input("nota da prova 02:"))
nota3=float(input("nota do trabalho:"))
media=(nota1+nota2+nota3)/3
print(f"sua media e {media:.1f}")
if media<4.5:
    print("reprovado!!!")
elif media>4.5 and media<6:
    print("reprovado estudar um pucoo mais!!!")
elif media>=6 and media<7:
    print("aprovado!!!")
elif media>7 and media<=10:
    print("aprovado muito bem vc esta de parabens!!!")