def bellman_ford(graph, s):
    # Initialisation
    n = len(graph)  # Nombre de sommets
    d = [float('inf')] * n  # Distance minimale de s à chaque sommet
    pi = [None] * n  # Prédécesseurs de chaque sommet
    d[s] = 0

    # Boucle principale
    for _ in range(n - 1):
        for u in range(n):
            print("Pour u : "+str(u))
            for v, w_uv in graph[u]:
                if d[v] > d[u] + w_uv:
                    d[v] = d[u] + w_uv
                    pi[v] = u
                    print(str(d[v])+" "+str(pi[v]))

    # Vérification de la présence de cycles négatifs
    for u in range(n):
        for v, w_uv in graph[u]:
            if d[v] > d[u] + w_uv:
                return None  # Cycle négatif détecté

    return d, pi  # Pas de cycle négatif, retourne les distances minimales et les prédécesseurs

# Exemple d'utilisation
graph = [
    [(1, 5), (2, 4)],
    [(2, -2)],
    [(3, 3)],
    [(0, 2), (1, 1)]
]



s = 0  # Sommet d'origine
result = bellman_ford(graph, s)
if result is None:
    print("Cycle négatif détecté, pas de solution.")
else:
    distances, predecessors = result
    print("Distances minimales:", distances)
    print("Prédécesseurs:", predecessors)

