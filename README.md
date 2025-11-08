# Rota Inteligente: Otimização de Entregas com IA

Projeto desenvolvido para a disciplina **Artificial Intelligence Fundamentals**.  
O objetivo é aplicar algoritmos clássicos de Inteligência Artificial (A* e K-Means) para otimizar as rotas de entrega da empresa fictícia **Sabor Express**, reduzindo tempo e custo logístico.

---

## 1. Objetivo do Projeto

A empresa **Sabor Express** enfrenta dificuldades em gerenciar as rotas de entrega durante horários de pico.  
O objetivo deste projeto é desenvolver uma **solução inteligente** que:

- Encontre o menor caminho entre dois pontos (usando o algoritmo A*);
- Agrupe entregas próximas entre si (usando o algoritmo K-Means);
- Gere representações visuais das rotas e zonas de entrega otimizadas.

---

## 2. Abordagem Técnica

1. Representação da cidade como **grafo ponderado**, com bairros e distâncias.
2. Busca da melhor rota com o algoritmo **A*** (heurístico baseado em custo).
3. Agrupamento dos pedidos por **proximidade geográfica** com **K-Means**.
4. Geração automática de imagens (`grafo.png` e `agrupamento.png`) salvas na pasta `/docs`.

---

## 3. Tecnologias Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| Linguagem  | Python 3.11 |
| Bibliotecas | NetworkX, scikit-learn, Matplotlib, Pandas, NumPy |
| Visualização | Geração automática de gráficos (`grafo.png`, `agrupamento.png`) |
| Versionamento | Git e GitHub |

---

## 4. Resultados

- Cálculo do menor caminho entre os pontos da cidade com o algoritmo A*;
- Agrupamento eficiente das entregas com K-Means, reduzindo sobreposição de trajetos;
- Visualizações geradas automaticamente e salvas na pasta `/docs`.

---

## 5. Visualizações

### Grafo de Rotas (A*)
![Mapa de Entregas](docs/grafo.png)

### Agrupamento de Entregas (K-Means)
![Agrupamento](docs/agrupamento.png)

---

## 6. Estrutura do Projeto


