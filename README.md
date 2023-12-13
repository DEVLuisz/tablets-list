# Projeto de Visualização de Dados em Python

Este repositório contém scripts Python para visualização de dados a partir de um arquivo Excel (`Relação.xlsx`). Os scripts geram gráficos de barras representando o número de tablets recebidos por escola.

## `main.py`

### Funcionalidades

1. **Leitura de Dados:**
   - Utiliza a biblioteca pandas para ler dados do arquivo Excel `Relação.xlsx`.

   ```python
   import pandas as pd

   # Leitura dos dados do Excel
   df = pd.read_excel('./baseData/Relação.xlsx')

2. **Criação do Gráfico de Barras:**
   - Gera um gráfico de barras usando matplotlib, exibindo o número de tablets recebidos por escola

    ```python
    import matplotlib.pyplot as plt
    
    # Criar um gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(kind='bar', x='NOME DA ESCOLA', y='TABLETS RECEBIDOS', ax=ax, color='skyblue')
    ```

3. **Adição de Rótulos e Título:**
     - Adiciona rótulos e título ao gráfico para uma melhor compreensão.

      ```python
      # Adicionar rótulos e título
      plt.xlabel('Escola')
      plt.ylabel('Tablets Recebidos')
      plt.title('Número de Tablets Recebidos por Escola')
      ```

4. **Adição de Rótulos de Dados nas Barras:**

   - Inclui rótulos de dados nas barras do gráfico para fornecer informações detalhadas.
    ```python
    # Adicionar rótulos de dados nas barras
    for i, v in enumerate(df['TABLETS RECEBIDOS']):
        ax.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=8)
    ```

5. **Salvamento do Gráfico em PDF:**

     - Cria uma pasta 'pdf' se não existir e salva o gráfico em formato PDF.
      ```python
        # Criar pasta 'pdf' se não existir
      import os
      output_folder = 'pdf'
      os.makedirs(output_folder, exist_ok=True)
      
      # Salvar o gráfico em PDF
      output_file = os.path.join(output_folder, 'grafico_tablets.pdf')
      plt.savefig(output_file, bbox_inches='tight')
      ```
6. **Exibição do Gráfico:**

    - Exibe o gráfico na interface gráfica.
     ```python
     # Exibir o gráfico
     plt.show()
      ```

## `tabletsRecebidos.py`
O segundo script, tabletsRecebidos.py, realiza funcionalidades similares para a visualização dos dados. Ambos os scripts são complementares e oferecem flexibilidade na escolha da abordagem para a análise de dados.

## Como Utilizar:
- Clone este repositório em sua máquina local.
- Execute os scripts Python principais: python main.py e python tabletsRecebidos.py.

## Estrutura do Projeto
- main.py: Script principal para visualização do número de tablets recebidos por escola.
- tabletsRecebidos.py: Script adicional para uma abordagem alternativa na visualização dos dados.
- baseData/Relação.xlsx: Arquivo Excel contendo os dados para visualização.
- pdf/: Pasta de saída para armazenar os gráficos em formato PDF.

## Autor
Luís Felipe (Louís)
      
