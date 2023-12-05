import sqlite3

def busca_nomes_medicamentos():
    # Conecte-se ao banco de dados
    conexão = sqlite3.connect('controlefacil')

    # Crie um cursor
    cursor = conexão.cursor()

    # Execute a consulta SQL para selecionar os nomes dos medicamentos da tabela "medicamentos"
    cursor.execute('SELECT nome FROM medicamentos')

    # Acesse os resultados
    resultados = cursor.fetchall()

    # Feche a conexão
    conexão.close()

    # Crie uma lista para armazenar os nomes dos medicamentos
    nomes_medicamentos = []

    # Itere sobre os resultados e armazene os nomes dos medicamentos na lista
    for linha in resultados:
        nome_medicamento = linha[0]
        nomes_medicamentos.append(nome_medicamento)

    return nomes_medicamentos

# Chamada da função para buscar os nomes dos medicamentos
nomes_medicamentos = busca_nomes_medicamentos()

# Imprima os nomes dos medicamentos
for nome_medicamento in nomes_medicamentos:
    print(nome_medicamento)

import requests
from bs4 import BeautifulSoup
import sqlite3

# Função para extrair valores/preços de remédios e armazená-los no banco de dados
def extrair_precos_medicamentos():
    # URL do site que contém os valores/preços dos remédios
    url = 'https://www.exemplo.com/remedios'

    # Realiza a requisição GET para obter o conteúdo da página
    response = requests.get(url)
    if response.status_code == 200:
        # Cria o objeto BeautifulSoup para analisar o conteúdo da página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontra os elementos HTML que contêm os valores/preços dos remédios
        resultados = soup.find_all('span', class_='valor-remedio')

        # Conecta-se ao banco de dados
        conexao = sqlite3.connect('remedios.db')
        cursor = conexao.cursor()

        # Cria a tabela "remedios" no banco de dados (se ela ainda não existir)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS remedios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                preco REAL
            )
        ''')

        # Itera sobre os elementos encontrados e armazena os valores/preços no banco de dados
        for resultado in resultados:
            nome_remedio = resultado['data-nome']
            preco_remedio = float(resultado['data-preco'])

            # Insere o nome e o preço do remédio na tabela "remedios"
            cursor.execute('INSERT INTO remedios (nome, preco) VALUES (?, ?)', (nome_remedio, preco_remedio))

        # Finaliza a transação e fecha a conexão com o banco de dados
        conexao.commit()
        conexao.close()

# Chama a função para extrair os preços dos medicamentos e armazená-los no banco de dados
extrair_precos_medicamentos()