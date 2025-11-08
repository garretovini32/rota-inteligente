from grafo import criar_grafo, menor_caminho, desenhar_grafo
from clustering import agrupar_entregas

print("\n=== Rota Inteligente - Otimização de Entregas ===\n")
print("Iniciando execução do projeto...\n")

# ----------------- ETAPA 1: A* (rota) -----------------
print("Etapa 1: calculando a melhor rota com o algoritmo A*...\n")

G = criar_grafo()
origem = "Centro"
destino = "Consolação"

caminho, distancia = menor_caminho(G, origem, destino)

if caminho:
    print(f"Melhor rota entre {origem} e {destino}: {' → '.join(caminho)}")
    print(f"Distância total: {distancia:.2f} km\n")
else:
    print("Não há caminho possível entre os pontos informados.\n")

print("Gerando imagem do grafo com a rota destacada...")
desenhar_grafo(G, caminho)
print("Imagem do grafo salva em: docs/grafo.png\n")

# ----------------- ETAPA 2: K-MEANS (clusters) -----------------
print("Etapa 2: executando K-Means para agrupar as entregas...\n")

df_resultado = agrupar_entregas("../data/entregas.csv", n_clusters=2)

print("Agrupamento concluído. Resultado por bairro:")
print(df_resultado[["bairro", "cluster"]])

print("\nExecução finalizada. As imagens foram salvas na pasta docs/.")
