import pandas as pd

data = pd.read_csv("gasolina.csv")

print(data.head())

flights = data[["dia", "venda"]].groupby("dia").agg("sum").reset_index()
flights.head()

import pandas as pd
import matplotlib.pyplot as plt

# Configuração do estilo do eixo
plt.style.use('seaborn-whitegrid')

# Criar o gráfico de linha
grafico = plt.plot(flights["dia"], flights["venda"], color='blue')

# Configurações do título e dos rótulos dos eixos
plt.title('Vendas por dia')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.savefig('gasolina.png')
plt.show()
