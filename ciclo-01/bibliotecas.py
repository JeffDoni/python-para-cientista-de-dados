import pandas as pd
import numpy as np

# Carregar o dataset

data =  pd.read_csv('/home/jdn1937/Projetos pessoais/python-para-cientista-de-dados/ciclo-01/AB_NYC_2019.csv')
data.head()
pŕeco_aluguel = data.loc[:, 'price']

# Calcular a média de todos os valores da cidade de Nova York

print(np.mean(pŕeco_aluguel))

# Contar todos os nomes distintos que aparecem na coluna região

regiao = data.loc[ :, 'neighbourhood_group']

print(pd.unique(regiao))

# Encontrar o valor maXIMO de alugueIS
price = np.max(pŕeco_aluguel)

print(price)
