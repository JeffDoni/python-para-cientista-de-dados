# Lendo arquivos CSV

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar o dataset

data =  pd.read_csv('/home/jdn1937/Projetos pessoais/python-para-cientista-de-dados/ciclo-01/AB_NYC_2019.csv')

# PERGUNTAS DO CEO

# Quais são as categorias de imóveis que estão cadastradas dentro da base de dados da cidade de Nova York?

print(data.head())
room_type = data.loc[:, 'room_type']
print(np.unique(room_type))

# Quantos usuários (Hosts) únicos cadastrados existem dentro da base de dados da cidade de Nova York?

host_id = data.loc[:, 'host_id']
host_id_unique = np.unique(host_id)
print(len(host_id_unique))

# Como é a variação do preços dos imóveis em NY?

price = data.loc[:, 'price']
print( 'O STD {}'.format(np.std(price)))
print('A media {}'.format(np.mean(price)))

# Existem mais imóveis baratos ou caros?

linhas = data.loc[:, 'price'] < 1200
data_barato = data.loc[linhas, 'price']

print('O maior valor de aluguel é {}'.format(np.max(price)))

# Desenhar um histograma com os preços dos imóveis

plt.hist(data_barato, bins=12)
plt.show()


# Qual a distribuição do número de Reviews? Existem imóveis com muitose outro com poucos reviews?

linha_n_reviews = data.loc[:, 'number_of_reviews'] > 100
data_n_reviews = data.loc[linha_n_reviews, 'number_of_reviews']

plt.hist(data_n_reviews, bins=12)
plt.show()
