print("Ola, bem vindo à calculadora!!!")
print("1 = soma\n2 = subutração\n3 = divisão\n4 = multiplicação\n5 = expodenciação")
operador = int(input("Qual seria a operação???"))
numero1 = float(input("Digite numero 1: "))
numero2 = float(input("Digite numero 2: "))
if operador==1:
    resultado = numero1 + numero2
    print(f"A soma e: {resultado}")
elif operador==2:
    resultado = numero1 - numero2
    print(f"A subtração e: {resultado}")
elif operador==3:
    resultado = numero1 / numero2
    print(f"A  disivisão  e: {resultado}")
elif operador==4:
    resultado = numero1 * numero2
    print(f"A multiplicação e: {resultado}")
elif operador==5:
    resultado = numero1 * numero2
    print(f"A multiplicação e: {resultado}")