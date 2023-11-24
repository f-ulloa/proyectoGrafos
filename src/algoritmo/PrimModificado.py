import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo completo no dirigido con 10 vértices
G = nx.complete_graph(10)

# Asignar pesos aleatorios a las aristas
for u, v in G.edges():
    G[u][v]['weight'] = nx.utils.rand_weight()

# Visualizar el grafo original
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Encontrar 5 árboles de expansión mínima usando el algoritmo de Prim
subtrees = []
while len(subtrees) < 5:
    MST = nx.minimum_spanning_tree(G, algorithm='prim')
    subtrees.append(MST)
    G.remove_edges_from(MST.edges())

# Visualizar los 5 subárboles de expansión mínima
for i, MST in enumerate(subtrees):
    pos = nx.spring_layout(G)
    nx.draw(MST, pos, with_labels=True, font_weight='bold', node_size=700, edge_color='r')
    labels = nx.get_edge_attributes(MST, 'weight')
    nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels)
    plt.title(f"Subárbol {i + 1}")
    plt.show()

# Imprimir las aristas seleccionadas en cada subárbol
for i, MST in enumerate(subtrees):
    selected_edges = list(MST.edges())
    print(f"\nAristas seleccionadas en Subárbol {i + 1}:")
    for edge in selected_edges:
        print(edge)
