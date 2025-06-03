from sklearn.base import BaseEstimator, TransformerMixin

class AddVolumeFeature(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X['v'] = X['x'] * X['y'] * X['z']  # Assuming volume is x * y * z
        return X