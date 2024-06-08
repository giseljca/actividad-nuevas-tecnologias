
import streamlit as st # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Set the page title and header
st.title("Proyecto Integrador")
st.header("Bienvenido a nuestro Proyecto Integrador")

# Hero Section with image and project description
st.image("https://i1.sndcdn.com/artworks-nTgGESMaN9t5TBxQ-xO5rFg-t500x500.jpg", width=600)
st.write("**Descripción del proyecto:** Breve descripción del proyecto, sus objetivos y su impacto.")


# Project Overview
st.subheader("Resumen del Proyecto")
st.write("- Punto 1: Introduccion.")
st.write("- Punto 2: Simulador cesde.")
st.write("- Punto 3: Proyecto integrador.")
st.write("- Punto 4: Proyecto Individual.")

# Interactive Chart or Visualization (Optional)
# Replace with your specific data and visualization
data = [10, 20, 30, 40, 50]
labels = ["Categoría A", "Categoría B", "Categoría C", "Categoría D", "Categoría E"]
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%")
st.pyplot(fig)

# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
st.write("- Nombre 1: Heidi Yinela Perez Moreno")
st.write("- Nombre 2: Gisel Lorena Jaramillo")
st.write("- Nombre 3: Bryan Ruiz")
