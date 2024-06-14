import streamlit as st # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Set the page title and header
st.title("Proyecto Integrador")
st.header("Bienvenido a nuestro Proyecto Integrador")

# Hero Section with image and project description
st.image("https://i1.sndcdn.com/artworks-nTgGESMaN9t5TBxQ-xO5rFg-t500x500.jpg", width=600)
st.write("*Descripción del proyecto:Este proyecto hace parte del trabajo final del área de nuevas tecnologías de la programación.Para su realización, se utilizó el lenguaje de programación python y la librería para la manipulación y análisis de datos Pandas, así como también el framework de streamlit, el cual sirvió para realizar toda la parte gráfica del proyecto. ")

# Project Overview
st.subheader("Resumen del Proyecto")
st.write("- Home: aquí se visualiza los integrantes del grupo, un poco de información acerca del trabajo y se da la bienvenida a los lectores. ")
st.write("- Proyecto Integrador: en este se mostrarán 3 gráficos de 3 filtros que se realizaron a una base de datos de spotify.")
st.write("- Simulador Cesde: En este apartado se visualiza 3 gráficos que se realizaron a una base de datos simulada del Cesde.")
st.write("- Proyecto Individual: para realizarlo se utilizó una base de datos de activos financieros de Meta, a este también se le realizaron 3 filtros y 3 gráficos.")

st.image("https://blog.jcharistech.com/wp-content/uploads/2021/07/sample_app_workflow_streamlit_app_jcharistech.png", width=600)

# Call to Action
st.subheader("¡Contáctanos!")
st.write("*Visite nuestro sitio web:* (https://actividad-nuevas-tecnologias-dvnopwyefvvt6x8cseteif.streamlit.app/)")
st.write("*Contáctenos:* (gljaramilloca@cesde.net)")

# Footer with team members and project information
st.subheader("Equipo")
st.write("*Miembros del equipo:*")
st.write("- 1: Heidi Yinnela Perez Moreno.")
st.write("- 2: Gisel Lorena Jaramillo.")
st.write("- 3: Bryan Ruiz.")

