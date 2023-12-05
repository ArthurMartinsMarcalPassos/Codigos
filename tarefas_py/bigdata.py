from bs4 import BeautifulSoup
import requests

def buscaPreco(nomeMed):
    url = f'https://www.drogasil.com.br/search?w={nomeMed}' 

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        resultados = soup.find_all('span', class_="Pricestyles__ProductPriceStyles-sc-118x8ec-0 fzwZWj price")

        precos = []
        for resultado in resultados:
            preco = resultado.text.strip()
            precos.append(preco)

        return precos
    
    return None

medicamento = input('Digite o nome do medicamento: ')
precos = buscaPreco(medicamento)

if precos:
    print(f'Preços encontrados para {medicamento}:')
    for preco in precos:
        print(preco)
else:
    print('Nenhum preço encontrado.')

