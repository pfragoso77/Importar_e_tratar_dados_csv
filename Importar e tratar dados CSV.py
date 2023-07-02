#PFragoso

#TAREFA 1: Importei dados com módulo 'Pandas'
import pandas as pd

ficheiro_dados = pd.read_csv('AtividadePedagogica4_10793_02.csv')
print(ficheiro_dados)

# Importei o módulo 'Pandas' que permite a análise e manipulação de dados, incluindo ficheiros em csv. Em alterantiva podíamos importar o módulo 'csv' para trabalhar especificamente com ficheiros csv.

#TAREFA 2: Aplica 2 Algoritmos de Ordenação ('bubble_sort' e 'counting_sort')

# opção bubble_sort
print('______bubble_sort_______')

# definição da função que faz a contagem dos dados
def bubble_sort(produtos):
    n = len(produtos)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if produtos[j]['quantidade_vendida'] > produtos[j + 1]['quantidade_vendida']:
                produtos[j], produtos[j + 1] = produtos[j + 1], produtos[j]


# Converte os dados para uma lista de dicionários com a função 'to.dict("records")'
produtos = ficheiro_dados.to_dict('records')

# Chama a função bubble_sort para ordenar os produtos pela quantidade vendida
bubble_sort(produtos)

# Exibe os produtos ordenados
for produto in produtos:
    print(f"Data: {produto['data']}, Produto: {produto['produto']}, Preço Unitário: {produto['preco_unitario']}, Quantidade Vendida: {produto['quantidade_vendida']}")

# opção counting_sort
print('______counting_sort_______')

def counting_sort(produtos):
    # Encontra o valor máximo da coluna "quantidade_vendida"
    max_value = max(produto['quantidade_vendida'] for produto in produtos)

    # Cria uma lista com o tamanho máximo encontrado
    count = [0] * (max_value + 1)

    # Conta a frequência de cada valor da coluna "quantidade_vendida"
    for produto in produtos:
        count[produto['quantidade_vendida']] += 1

    # Atualiza as contagens para obter as posições corretas no resultado
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Cria uma lista auxiliar para armazenar os produtos ordenados
    sorted_produtos = [None] * len(produtos)

    # Ordena os produtos com base na coluna "quantidade_vendida"
    for produto in reversed(produtos):
        index = count[produto['quantidade_vendida']] - 1
        sorted_produtos[index] = produto
        count[produto['quantidade_vendida']] -= 1

    # Atualiza a lista original de produtos com os produtos ordenados
    produtos[:] = sorted_produtos


# Converte os dados para uma lista de dicionários
produtos = ficheiro_dados.to_dict('records')

# Chama a função counting_sort para ordenar os produtos pela quantidade vendida
counting_sort(produtos)

# Exibe os produtos ordenados
for product in produtos:
    print(f"Data: {produto['data']}, Produto: {produto['produto']}, Preço Unitário: {produto['preco_unitario']}, Quantidade Vendida: {produto['quantidade_vendida']}")

#TAREFA 3 Apresentar Resultados:
