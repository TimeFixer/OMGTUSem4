import numpy as np
class KMeansCustom:
    def __init__(self, k, max_iter=1000, tol=1e-4, random_state=None):

        self.k = k
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state
        self.centroids = None
        self.labels_ = None
        
    def fit(self, data):
        data = np.array(data)
        n = data.shape[0]
        
        if self.random_state is not None:
            np.random.seed(self.random_state)
        
        indices = np.random.choice(n, size=self.k, replace=False)
        self.centroids = data[indices].tolist()
        
        for _ in range(self.max_iter):
            self.labels_ = self._data_distribution(data)
            old_centroids = self.centroids
            self.centroids = self._cluster_update(data)
            
            if np.allclose(old_centroids, self.centroids, atol=self.tol):
                break
                
        return self
    
    def predict(self, data):
        data = np.array(data)
        return self._data_distribution(data)
    
    def _data_distribution(self, data):
        return [np.argmin([np.linalg.norm(point - c) for c in self.centroids]) 
                for point in data]
    
    def _cluster_update(self, data):
        new_centroids = []
        for i in range(self.k):
            cluster_points = data[np.array(self.labels_) == i]
            if len(cluster_points) == 0:
                new_centroids.append(data[np.random.randint(len(data))].tolist())
                continue
            new_centroids.append(cluster_points.mean(axis=0).tolist())
        return new_centroids