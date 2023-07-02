#PFragoso

#TAREFA 1: Importei os dados com módulo 'Pandas'
import pandas as pd

ficheiro_dados = pd.read_csv('AtividadePedagogica4_10793_02.csv')
print(ficheiro_dados)

# O módulo 'Pandas' permite a análise e manipulação de dados, incluindo ficheiros em csv. Em alternativa podíamos importar o módulo 'csv' para trabalhar especificamente com ficheiros csv.

#TAREFA 2: Aplica 2 Algoritmos de Ordenação ('bubble_sort' e 'counting_sort')

# 1ª opção bubble_sort
print('______bubble_sort_______')

# definição da função que faz a contagem dos dados com função 'len' e função 'for'
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

# Exibe os campos ordenados, transformando em linhas os nomes das colunas do ficheiro csv
for produto in produtos:
    print(f"Data: {produto['data']}, Produto: {produto['produto']}, Preço Unitário: {produto['preco_unitario']}, Quantidade Vendida: {produto['quantidade_vendida']}")

# 2ª opção counting_sort
print('______counting_sort_______')

# definição da função que faz a contagem dos dados com função 'max_value' e função 'count'
def counting_sort(produtos):
    max_value = max(produto['quantidade_vendida'] for produto in produtos)
    count = [0] * (max_value + 1) # Cria uma lista de contagem
    
    for produto in produtos:
        count[produto['quantidade_vendida']] += 1 # Conta a frequência de cada valor (vezes que cada produto aparece)

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sorted_produtos = [None] * len(produtos) # Lista auxiliar para armazenar produtos ordenados
    # Ordena os produtos
    for produto in produtos: 
        index = count[produto['quantidade_vendida']] - 1
        sorted_produtos[index] = produto
        count[produto['quantidade_vendida']] -= 1
    # Atualiza a lista original de produtos
    produtos[:] = sorted_produtos
# Converte os dados para uma lista de dicionários
produtos = ficheiro_dados.to_dict('records')

counting_sort(produtos)
# Exibe os produtos ordenados
for produto in produtos:
    print(f"Data: {produto['data']}, Produto: {produto['produto']}, Preço Unitário: {produto['preco_unitario']}, Quantidade Vendida: {produto['quantidade_vendida']}")

#TAREFA 3: Apresentar resultados com gráfico de barras

import matplotlib.pyplot as plt

nomes_produtos = [produto['produto'] for produto in produtos]
quantidades_vendidas = [produto['quantidade_vendida'] for produto in produtos]

plt.bar(range(len(nomes_produtos)), quantidades_vendidas)
plt.xlabel('Produtos')
plt.ylabel('Quantidade Vendida')
plt.title('Quantidade Vendida por Produto')

plt.xticks(range(len(nomes_produtos)), nomes_produtos, rotation=90)

plt.show()

