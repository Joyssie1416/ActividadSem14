import streamlit as st
import os
from pymongo import MongoClient
from datetime import datetime

st.title("Calculadora de IMC 💪")
st.write("Esta aplicación calcula tu Índice de Masa Corporal (IMC).")

# Conexión de Mensajes
st.divider()
st.subheader("Conexión a MongoDB Atlas")

uri = os.environ.get("MONGODB_URI")

if uri:
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        info = client.admin.command("serverStatus")
        hora_servidor = info.get("localTime", datetime.utcnow())
        st.success(f"Conectado a MongoDB Atlas")
        st.info(f"Hora del servidor: {hora_servidor}")
        client.close()
    except Exception as e:
        st.error(f"Error al conectar: {e}")
else:
    st.warning("Variable MONGODB_URI no configurada.")

# Calculadora
st.divider()
peso = st.number_input("Ingresa tu peso (kg):", min_value=0.0, format="%.2f")
estatura = st.number_input("Ingresa tu estatura (m):", min_value=0.0, format="%.2f")

if st.button("Calcular IMC"):
    if peso > 0 and estatura > 0:
        imc = peso / (estatura ** 2)
        st.write(f"Tu IMC es: **{imc:.2f}**")
        if imc < 18.5:
            st.info("Bajo peso 🟡")
        elif 18.5 <= imc < 25:
            st.success("Peso normal ✅")
        elif 25 <= imc < 30:
            st.warning("Sobrepeso 🟠")
        else:
            st.error("Obesidad 🔴")
    else:
        st.warning("Por favor, ingresa valores válidos.")
