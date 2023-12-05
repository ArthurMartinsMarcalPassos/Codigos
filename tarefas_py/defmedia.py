def criarDic():
    dic = {}
    for c in range(3):
        matricula = int(input("matricula: "))
        nota = float(input("av1: "))
        nota2 = float(input("av2: "))
        nota3 = float(input("av3: "))
        print("\n")
        dic[f'matricula-{matricula}'] = matricula
        dic[f'av1-{matricula}'] = nota
        dic[f'av2-{matricula}'] = nota2
        dic[f'av3-{matricula}'] = nota3
        dic[f'media-{matricula}'] = (nota + nota2 + nota3) / 3

        if dic[f'media-{matricula}'] >= 7:
            dic[f'situacao-{matricula}'] = "Aprovado"
        else:
            dic[f'situacao-{matricula}'] = "Reprovado"
    return dic

