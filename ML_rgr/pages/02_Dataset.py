import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Описание данных", layout="wide")
st.title("📊 Описание датасета — Стоимость бриллианта")

st.markdown("""
Данные представляют собой набор информации о стоимость и признаки бриллианта. Цель — предсказание о стоимости алмаза
на основе ряда признаков. Датасет содержит как числовые, так и категориальные данные.
""")

st.header("🔢 Структура датасета")

data_description = {
"-`carat`" : "вес бриллианта",
"-`cut`" : "качество огранки",
"-`color`" : "цвет",
"-`clarity`" : "чистота",
"-`x`" : "длинна в мм по x",
"-`y`" : "длинна в мм по y",
"-`z`" : "длинна в мм по z",
"-`depth`" : "общая глубина в процентах",
"-`table`" : "ширина верхней части бриллианта относительно самой широкой точки",
}

st.subheader("📌 Признаки и их описание:")
for feature, desc in data_description.items():
    st.markdown(f"**{feature}**: {desc}")

st.subheader("🎯 Целевая переменная")
st.markdown("`price` : цена")

st.subheader("🧮 Тип задачи")
st.markdown("Задача регрессии: предсказание стоимости алмаза по основным признакам.")

st.write(f"Количество признаков: {len(data_description)}")

st.markdown("---")
