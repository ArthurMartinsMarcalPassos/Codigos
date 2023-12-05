#6
#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo,
#o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver
#pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação
#A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões
#terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o 
#usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar."""
#funcao pra converter horario para horario americano
def coverte_hora(hora,minutos):

    if hora > 13:
        m_ou_t = "A.M"
        hora = hora - 12

    else:
        m_ou_t = "P.M"
    x = print(f"{hora}:{minutos} {m_ou_t}")
    return x

horas = input("digite horas: ")
minuto = input("digite os minutos: ")

if horas.isnumeric() and minuto.isnumeric():
    horas = int(horas)
    minuto = int(minuto)
    result = coverte_hora(horas,minuto)
    print(result)

else:
    print("vc n digitou um numero")