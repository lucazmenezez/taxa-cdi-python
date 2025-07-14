import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Verifica se o nome do gráfico foi passado
try:
    nome_arquivo = sys.argv[1]
except IndexError:
    print("Uso: python visualizacao.py nome_do_arquivo")
    sys.exit(1)

# Lê os dados do CSV
df = pd.read_csv("taxa-cdi.csv")

# Gera o gráfico
plt.figure(figsize=(10, 4))
grafico = sns.lineplot(x="hora", y="taxa", data=df, marker="o")
grafico.set_title("Evolução da Taxa CDI")
grafico.set_xlabel("Hora")
grafico.set_ylabel("Taxa (%)")
grafico.set_xticklabels(df["hora"], rotation=90)

plt.tight_layout()
plt.savefig(f"{nome_arquivo}.png")
print(f"Gráfico gerado: {nome_arquivo}.png")