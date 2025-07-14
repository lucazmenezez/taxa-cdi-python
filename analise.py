import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importa a função de extração
from extracao import main as extrair

def gerar_grafico(nome_arquivo):
    df = pd.read_csv("taxa-cdi.csv")

    plt.figure(figsize=(10, 4))
    grafico = sns.lineplot(x="hora", y="taxa", data=df, marker="o")
    grafico.set_title("Evolução da Taxa CDI")
    grafico.set_xlabel("Hora")
    grafico.set_ylabel("Taxa (%)")
    grafico.set_xticklabels(df["hora"], rotation=90)

    plt.tight_layout()
    plt.savefig(f"{nome_arquivo}.png")
    print(f"Gráfico gerado em: {nome_arquivo}.png")

def main():
    try:
        nome_arquivo = sys.argv[1]
    except IndexError:
        print("Uso: python analise.py nome_do_arquivo")
        sys.exit(1)

    extrair()  # Coleta os dados
    gerar_grafico(nome_arquivo)  # Gera o gráfico

if __name__ == "__main__":
    main()