from grafo import criar_grafo, menor_caminho
from clustering import agrupar_entregas

# === Parte 1: GRAFO ===
print("\n=== 🚚 Rota Inteligente - Otimização de Entregas ===")

G = criar_grafo()
origem = "Centro"
destino = "Consolação"
caminho, distancia = menor_caminho(G, origem, destino)

if caminho:
    print(f"Melhor rota entre {origem} e {destino}: {' → '.join(caminho)}")
    print(f"Distância total: {distancia:.2f} km")
else:
    print("Não há caminho possível entre os pontos informados.")

# === Parte 2: AGRUPAMENTO ===
print("\n=== 📦 Agrupamento de Entregas ===")
df_resultado = agrupar_entregas("../data/entregas.csv", n_clusters=2)
print(df_resultado[["bairro", "cluster"]])
