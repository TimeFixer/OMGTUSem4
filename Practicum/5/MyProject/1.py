import sys
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.svm import SVC
import pandas as pd
import json

def main(dataset_path, new_data_path):
    # Чтение и предобработка данных
    data = pd.read_csv(dataset_path)
    figure_dict = {
        'circle': 0,
        'rectangle': 1
    }
    data['figure1'] = data['figure1'].map(figure_dict)
    data['figure2'] = data['figure2'].map(figure_dict)
    X = data.drop('collision', axis=1)
    y = data['collision']

    # Список моделей
    models = {
        'xgboost': XGBClassifier(eval_metric='logloss'),
        'logistic': LogisticRegression(),
        'svc_poly': SVC(kernel='poly'),
        'svc_rbf': SVC(kernel='rbf')
    }

    # Хранение предсказаний для каждой модели
    predictions_dict = {}

    # Обучение и предсказание для каждой модели
    for model_name, model in models.items():
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', model)
        ])

        pipeline.fit(X, y)

        # Чтение новых данных
        new_data = pd.read_csv(new_data_path)
        print("Значения figure в new_data:", new_data['figure1'].unique())
        # Применение словаря с обработкой NaN
        new_data['figure1'] = new_data['figure1'].map(figure_dict).fillna(0)
        new_data['figure2'] = new_data['figure2'].map(figure_dict).fillna(0)
        X_new = new_data[X.columns]  # Убедимся, что столбцы совпадают

        # Предсказание
        predictions = pipeline.predict(X_new)
        predictions_dict[model_name] = predictions.tolist()

    # Сохранение результатов для всех моделей
    return predictions_dict

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Имитация выполнения: script.py <dataset_path> <new_data_path>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])