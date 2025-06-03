import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Дашборд анализа данных", layout="wide")

st.title("📊 Дашборд анализа данных и моделирования")
st.markdown("""
На этой странице представлены основные результаты анализа данных и оценки моделей машинного обучения для задачи.
""")

image_dir = "Dashboard"
def display_image_with_caption(image_path, caption):
    image = Image.open(os.path.join(image_dir, image_path))
    st.image(image, caption=caption, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    display_image_with_caption("price.png", "График цен") 
    display_image_with_caption("sns.png", "График SNS")

with col2:
    display_image_with_caption("EDA.png", "Анализ данных EDA") 
    display_image_with_caption("corr_matrix.png", "Матрица корреляций") 

with col3:
    display_image_with_caption("tree.png", "Дерево решений")
    display_image_with_caption("polinom.png", "Полиномиальная регрессия")