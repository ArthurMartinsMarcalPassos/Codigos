peso=float(input("qual e o seu peso?"))
altura=float(input("qual sau altura?"))
imc=peso/altura**2
print(f"seu imc e:{imc:.1f}")
if imc<=16:
    print("magreza grave !!!")
    
elif imc>16 and imc<17:
    print("magreza moderada !!!")
elif imc>17 and imc<18.5:
    print("magreza leve !!!")
elif imc>18.5 and imc<25:
    print("saudavel !!!")
elif imc>25 and imc<30:
    print("sobre peso !!!")
elif imc>30 and imc<35:
    print("obesidade grau I !!!")
elif imc>35 and imc<40:
    print("obesidade grau II obesidade severa !!!")
elif imc<40:
    print("obesidade grua III ou obesidade morbida!!!")