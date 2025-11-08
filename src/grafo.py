import networkx as nx
import matplotlib.pyplot as plt

def criar_grafo():
    G = nx.Graph()

    # Nós (bairros)
    bairros = ["Centro", "Bela Vista", "República", "Liberdade", "Consolação"]
    G.add_nodes_from(bairros)

    # Arestas com distâncias (em km)
    G.add_weighted_edges_from([
        ("Centro", "Bela Vista", 1.0),
        ("Centro", "República", 0.8),
        ("Centro", "Liberdade", 1.2),
        ("Bela Vista", "Consolação", 1.1),
        ("República", "Consolação", 0.9),
        ("Liberdade", "República", 1.3)
    ])

    return G


def menor_caminho(G, origem, destino):
    try:
        caminho = nx.astar_path(G, origem, destino, weight='weight')
        distancia = nx.astar_path_length(G, origem, destino, weight='weight')
        return caminho, distancia
    except nx.NetworkXNoPath:
        return None, None


def desenhar_grafo(G, caminho=None, arquivo_saida="../docs/grafo.png"):
    pos = nx.spring_layout(G, seed=42)  # Layout fixo para consistência visual

    # Desenha os nós e arestas
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1800, font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Destaca o caminho encontrado (em vermelho)
    if caminho:
        edges = list(zip(caminho, caminho[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="red", width=3)

    plt.title("Mapa de Entregas - Rota Otimizada (A*)")
    plt.tight_layout()
    plt.savefig(arquivo_saida)
    plt.close()
