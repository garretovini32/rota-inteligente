import networkx as nx

def criar_grafo():
    G = nx.Graph()

    # Adiciona os nós (bairros)
    bairros = ["Centro", "Bela Vista", "República", "Liberdade", "Consolação"]
    G.add_nodes_from(bairros)

    # Adiciona as conexões (ruas) com distâncias (em km)
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
    # Usa o algoritmo A* (heurística: distância direta estimada)
    try:
        caminho = nx.astar_path(G, origem, destino, weight='weight')
        distancia = nx.astar_path_length(G, origem, destino, weight='weight')
        return caminho, distancia
    except nx.NetworkXNoPath:
        return None, None
