import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

plt.style.use("Solarize_Light2")
class AnaliseEDA:
    def __init__(self):
        pass
    def analiseUnivariada(self, df, tipo):
        colunas = df.select_dtypes(include=tipo).columns
        if tipo == "number":
            fig, axs = plt.subplots(figsize = (15, 8), ncols= 3, nrows=4)
            axs = axs.flatten()
            for i, coluna in enumerate(colunas):
                axs[i].hist(df[coluna])
                axs[i].set_xlabel(coluna)
                axs[i].set_ylabel("count")
            plt.suptitle("Distribuição das Variaveis numéricas")
            plt.tight_layout()
            plt.show()
        else:
            fig, axs = plt.subplots(figsize = (15, 5), ncols= 3, nrows=1)
            axs = axs.flatten()
            for i, coluna in enumerate(colunas):
                analiseColuna = df[coluna].value_counts().reset_index()
                analiseColuna.columns = [coluna, "Quantidade"]
                axs[i].bar(analiseColuna[coluna], analiseColuna["Quantidade"])
                for j, v in enumerate(analiseColuna["Quantidade"]):
                    axs[i].text(j, v, str(v), ha="center", va="bottom")
                axs[i].set_xlabel(coluna)
                axs[i].set_ylabel("count")
            plt.suptitle("Distribuição das Variaveis numéricas")
            plt.tight_layout()
            plt.show()
    
    def analiseBivariada(self, df, tipo):
        if tipo == "number":
            corr = df.select_dtypes(include=tipo).corr()
            # Criando o gráfico de correlação
            plt.figure(figsize=(10, 7))
            sns.heatmap(
                corr,
                annot=True,
                fmt=".2f",
                cmap='Blues',           # Paleta azul
                linewidths=0.5,
                linecolor='white',
                square=True,
            )

            plt.title('Mapa de Correlação - Variáveis Numéricas', fontsize=14, weight='bold')
            plt.tight_layout()
            plt.show()
        else:
            colunas = df.select_dtypes(include="object").columns

            fig, axs = plt.subplots(figsize=(15, 5), ncols=3, nrows=1)
            axs = axs.flatten()

            for i, coluna in enumerate(colunas):
                # Cria uma tabela de frequência cruzada entre a categoria da coluna e a variável binária "saida"
                tabela = pd.crosstab(df[coluna], df["Exited"])
                
                # Índices e larguras para barras lado a lado
                indices = np.arange(len(tabela.index))
                largura = 0.35
                
                # Plotando barras para "não sai" (assumindo saída = 0)
                axs[i].bar(indices - largura/2, tabela[0], width=largura, label='Não sai')
                # Plotando barras para "sai" (assumindo saída = 1)
                axs[i].bar(indices + largura/2, tabela[1], width=largura, label='Sai')
                
                # Colocando valores em cima das barras
                for j, v in enumerate(tabela[0]):
                    axs[i].text(j - largura/2, v + 0.5, str(v), ha='center', va='bottom')
                for j, v in enumerate(tabela[1]):
                    axs[i].text(j + largura/2, v + 0.5, str(v), ha='center', va='bottom')
                    
                axs[i].set_xticks(indices)
                axs[i].set_xticklabels(tabela.index, rotation=45)
                axs[i].set_xlabel(coluna)
                axs[i].set_ylabel('Contagem')
                axs[i].legend()

            plt.suptitle("Distribuição das categorias por saída (Sai/Não Sai)")
            plt.tight_layout()
            plt.show()
    