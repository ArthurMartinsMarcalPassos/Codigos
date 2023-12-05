def fatorial(num):
    fat=1
    while num>1:
        fat=fat*num
        num=num-1
    return fat

numero=int(input("digitr um numero"))
calculo=fatorial(numero)
print(calculo)
