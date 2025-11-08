import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def agrupar_entregas(caminho_csv, n_clusters=2):
    df = pd.read_csv(caminho_csv)

    # Seleciona as colunas de coordenadas
    coords = df[["latitude", "longitude"]]

    modelo = KMeans(n_clusters=n_clusters, random_state=42)
    df["cluster"] = modelo.fit_predict(coords)

    # Mostra e salva o agrupamento
    plt.scatter(df["latitude"], df["longitude"], c=df["cluster"], cmap="viridis", s=80)
    plt.title("Agrupamento de Entregas (K-Means)")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")

    # 🔹 Salva o gráfico na pasta /docs e não trava o terminal
    plt.tight_layout()
    plt.savefig("../docs/agrupamento.png")
    plt.close()

    return df
