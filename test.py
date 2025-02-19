# a = [ "1	        44669", "2	        44795","3	        44459"]	
# lista = a[0].split()
# x = []
# y = []

# x.append(lista[0])

# print(x)

# lista[0] = 'a'
# print(lista)
# print(x)

# b = list(range(100))

# Dados a serem escritos no arquivo
# dados = [
#     {"nome": "João", "idade": 25, "cidade": "São Paulo"},
#     {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
#     {"nome": "Carlos", "idade": 40, "cidade": "Belo Horizonte"}
# ]

# # Abrindo o arquivo em modo de escrita ('w')
# with open("dados.txt", "w") as arquivo:
#     # Escrevendo os dados no arquivo com espaçamento fixo
#     for linha in dados:
#         arquivo.write("{:<10}{:<10}{:<15}\n".format(linha["nome"], linha["idade"], linha["cidade"]))

# print("Arquivo 'dados.txt' criado e conteúdo salvo com sucesso!")

# int(input("Mensagem"))

# criar conjunto de dados

import random
import numpy as np

dados = [random.randint(100, 4000) for i in range(10)]
print(len(dados))

def movavg(data, window):
    average_data = []
    i = 0
    while i < len(data) - window + 1:
        for _ in range(window):
          average_data.append(np.mean(data[i:i+window]))
          print(i)
        i = i + window
    print("fim do cálculo!")
    return average_data

avg = movavg(dados, 3)
print(avg, len(avg), len(dados))

print(7629/100)