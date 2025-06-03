import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(page_title="Diamond Price Prediction", layout="centered")
st.title("💎 Прогнозирование цены алмаза")
st.markdown("Введите характеристики алмаза для получения прогноза цены.")

models_dir = "models"

if not os.path.exists(models_dir):
    st.error(f"Папка с моделями не найдена: {models_dir}")
else:
    model_files = [f for f in os.listdir(models_dir) if f.endswith('.pkl')]
    if not model_files:
        st.warning("В папке models нет моделей (.pkl файлов)")
    else:
        selected_model = st.selectbox("Выберите модель", model_files)
        model_path = os.path.join(models_dir, selected_model)
        
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        st.success(f"✅ Модель '{selected_model}' загружена")

        pipeline_models = ['PolynomialRegression.pkl', 'DecisionTreeRegressor.pkl']

        st.subheader("✍️ Введите характеристики алмаза")
        carat = st.number_input("Карат", min_value=0.2, max_value=5.0, value=1.0, step=0.01)
        cut = st.selectbox("Огранка", ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
        color = st.selectbox("Цвет", ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
        clarity = st.selectbox("Чистота", ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
        depth = st.number_input("Глубина (%)", min_value=30.0, max_value=90.0, value=60.0, step=0.1)
        table = st.number_input("Таблица (%)", min_value=30.0, max_value=90.0, value=55.0, step=0.1)
        x = st.number_input("Длина (мм)", min_value=3.0, max_value=10.0, value=5.0, step=0.01)
        y = st.number_input("Ширина (мм)", min_value=3.0, max_value=10.0, value=5.0, step=0.01)
        z = st.number_input("Высота (мм)", min_value=2.0, max_value=6.0, value=3.0, step=0.01)

        if st.button("🔮 Получить предсказание"):
            input_data = pd.DataFrame({
                'carat': [carat],
                'cut': [cut],
                'color': [color],
                'clarity': [clarity],
                'depth': [depth],
                'table': [table],
                'x': [x],
                'y': [y],
                'z': [z]
            })
            prediction = model.predict(input_data)[0]

            st.success(f"💰 Прогнозируемая цена алмаза: **${round(prediction, 2)}**")

st.markdown("---")
st.markdown("© 2025 — Diamond Price Predictor App")