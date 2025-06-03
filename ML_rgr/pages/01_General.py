import streamlit as st
import os

st.set_page_config(page_title="Информация о студенте", layout="wide")

st.markdown("<h1 style='text-align: center;'>Информация о студенте</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1]) 

with col1:
    st.markdown("""
    <p style='font-size: 20px;'>
    <strong>ФИО:</strong> Жигайло Иван Алексеевич<br>
    <strong>Группа:</strong> МО-231<br>
    <strong>Тема РГР:</strong> Разработка Web-приложения для инференса моделей ML и анализа данных
    </p>
    """, unsafe_allow_html=True)

with col2:
    image_path = "Dashboard/photo.png"
    if os.path.exists(image_path):
        st.image(image_path, caption="Аватар автора", width=300)
    else:
        st.error(f"Файл {image_path} не найден! Проверьте путь.")

st.markdown("---")
st.markdown("""
<div style='margin-bottom: 50px;'>
    <p style='text-align: center; font-size: 16px;'>Омск 2025</p>
</div>
""", unsafe_allow_html=True)