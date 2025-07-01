
import streamlit as st
import pandas as pd

# Datos de ejemplo (se cargarán desde archivo en versión completa)
data = [
    {"Nombre": "Gorra azul marino", "Imagen": "https://drive.google.com/uc?export=view&id=1HjUd7lC1GX8eu6H3ltchENthtwP0LBi7"},
    {"Nombre": "Pantalón de mezclilla azul", "Imagen": "https://drive.google.com/uc?export=view&id=1egfVxfccV2UIRFnPzj6FW60vuI4x6Emq"},
    {"Nombre": "Playera de rayas blancas", "Imagen": "https://drive.google.com/uc?export=view&id=1A0D8_HkZh4SJvgHEy-qP7V-dDaowY4JX"},
    {"Nombre": "Playera de rayas negras", "Imagen": "https://drive.google.com/uc?export=view&id=1kRIQwsazbRV3QWXA9I5l2CaRxFKt6xfX"},
    {"Nombre": "Polo azul rey", "Imagen": "https://drive.google.com/uc?export=view&id=1IaKufADtgDRWdV4-Zq4s067W-zG17wn5"},
    {"Nombre": "Short verde", "Imagen": "https://drive.google.com/uc?export=view&id=1pWe6T1rgj4tUIftUc43CvixtdvWkljaS"},
    {"Nombre": "Zapatos blancos", "Imagen": "https://drive.google.com/uc?export=view&id=1amqR2NNvf3O4z5iWl4fwLHuShdObwUji"},
]

st.set_page_config(page_title="Armario GPT", layout="centered")
st.title("🧠 Armario GPT")

st.markdown("""
### ¿Qué tipo de día tienes hoy?
Selecciona el tipo de clima y ocasión, y te recomendamos un outfit.
""")

clima = st.selectbox("Clima actual", ["Cálido", "Templado", "Frío"])
ocasión = st.selectbox("Tipo de ocasión", ["Casual", "Trabajo", "Ejercicio", "Evento especial"])

if st.button("Sugerir outfit"):
    st.markdown("### 👕 Outfit recomendado:")
    sugerencias = data[:3]  # Simplificación por ahora: primeros 3 artículos
    for prenda in sugerencias:
        st.image(prenda["Imagen"], width=200)
        st.caption(prenda["Nombre"])

st.markdown("---")
st.markdown("### 👚 Tu armario actual:")
for prenda in data:
    cols = st.columns([1, 3])
    with cols[0]:
        st.image(prenda["Imagen"], width=100)
    with cols[1]:
        st.write(f"**{prenda['Nombre']}**")
