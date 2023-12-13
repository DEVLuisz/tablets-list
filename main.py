import pandas as pd
import matplotlib.pyplot as plt
import os

# Leitura dos dados do Excel
df = pd.read_excel('./baseData/Relação.xlsx')

# Criar um gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
df.plot(kind='bar', x='NOME DA ESCOLA', y='PORCENTAGEM%', ax=ax, color='skyblue')

# Adicionar rótulos e título
plt.xlabel('Escola')
plt.ylabel('Porcentagem %')
plt.title('Porcentagem de Tablets Recebidos por Escola')

# Adicionar rótulos de dados nas barras
for i, v in enumerate(df['PORCENTAGEM%']):
    ax.text(i, v + 0.5, f'{v:.2f}%', ha='center', va='bottom', fontsize=8)

# Criar pasta 'pdf' se não existir
output_folder = 'pdf'
os.makedirs(output_folder, exist_ok=True)

# Salvar o gráfico em PDF
output_file = os.path.join(output_folder, 'grafico.pdf')
plt.savefig(output_file, bbox_inches='tight')

# Exibir o gráfico
plt.show()
