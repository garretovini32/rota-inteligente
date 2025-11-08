from grafo import criar_grafo, menor_caminho, desenhar_grafo
from clustering import agrupar_entregas

print("\n=== Rota Inteligente - Otimização de Entregas ===")

G = criar_grafo()
origem = "Centro"
destino = "Consolação"

caminho, distancia = menor_caminho(G, origem, destino)

if caminho:
    print(f"Melhor rota entre {origem} e {destino}: {' → '.join(caminho)}")
    print(f"Distância total: {distancia:.2f} km")
else:
    print("Não há caminho possível entre os pontos informados.")

# Gera o grafo visual com o caminho destacado
desenhar_grafo(G, caminho)
print("\nImagem do grafo salva em: docs/grafo.png")

print("\n=== Agrupamento de Entregas ===")
df_resultado = agrupar_entregas("../data/entregas.csv", n_clusters=2)
print(df_resultado[["bairro", "cluster"]])
