from sklearn_extra.cluster import KMedians
import numpy as np

# Datos de ejemplo
X = np.array([[lat1, lon1], [lat2, lon2], ...])

# Número de clusters deseado
k = 3

# Número máximo de puntos por cluster
max_points_per_cluster = 50

# Crear el modelo KMedians
kmedians = KMedians(n_clusters=k)
kmedians.fit(X)

# Obtener etiquetas y centros de los clusters
labels = kmedians.labels_
medians = kmedians.cluster_centers_

# Contar puntos por cluster
points_per_cluster = np.bincount(labels)

# Reasignar puntos si es necesario
for cluster_id in range(k):
    if points_per_cluster[cluster_id] > max_points_per_cluster:
        # Encontrar puntos en el cluster actual
        cluster_points = X[labels == cluster_id]

        # Calcular distancias a otros centros
        distances_to_other_medians = np.linalg.norm(cluster_points - medians[cluster_id], axis=1)

        # Encontrar el cluster más cercano
        closest_cluster = np.argmin(distances_to_other_medians)

        # Reasignar puntos al cluster más cercano
        labels[labels == cluster_id] = closest_cluster

# Imprimir resultados
print("Cluster Labels:", labels)
print("Cluster Medians:", medians)
