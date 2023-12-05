produtos=[]
for i in range(0,3):
    valores=float(input("digite o valor do produto:"))
    produtos.append(valores)
print(f"o mais barato e {min(produtos)}")