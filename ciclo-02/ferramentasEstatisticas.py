import numpy as np
import matplotlib.pyplot as plt

# Desvio padrão
dados = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
desvio_padrao = np.std(dados)
print('O desvio padrão é {:.2f}'.format(desvio_padrao))

# Histograma
plt.hist(dados)
plt.show()


