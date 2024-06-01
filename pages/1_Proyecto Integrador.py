import streamlit as st # type: ignore
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Análisis de Música")

# Cargar los datos de música
df = pd.read_csv('static/datasets/proyectointegrador.csv')

# Obtener los valores únicos de la columna 'Track Name' sin NaN
track_names = df['Track Name'].dropna().unique().tolist()

# Obtener las opciones únicas para los filtros
artist_names = sorted(df['Artist Name'].dropna().unique())
album_names = sorted(df['Album Name'].dropna().unique())
popularity = sorted(df['Popularity'].dropna().unique())
dates = sorted(df['Date'].dropna().unique())
markets = sorted(df['Markets'].dropna().unique())
danceability = sorted(df['Danceability'].dropna().unique())
acousticness = sorted(df['Acousticness'].dropna().unique())
duration = sorted(df['duration'].dropna().unique())
energy = sorted(df['Energy'].dropna().unique())
instrumentalness = sorted(df['Instrumentalness'].dropna().unique())
key = sorted(df['Key'].dropna().unique())
liveness = sorted(df['Liveness'].dropna().unique())
loudness = sorted(df['Loudness'].dropna().unique())
mode = sorted(df['Mode'].dropna().unique())
speechiness = sorted(df['Speechiness'].dropna().unique())
tempo = sorted(df['Tempo'].dropna().unique())

# Función de filtro por nombre de pista
def filtro_por_nombre_pista():
    nombre_pista = st.selectbox("Nombre de la Pista", track_names)
    resultado = df[df['Track Name'] == nombre_pista]
    st.write(resultado)
    if not resultado.empty:
        fig = px.bar(resultado, x='Track Name', y='Popularity', color='Track Name', title="Popularidad de la Pista")
        st.plotly_chart(fig)

# Función de filtro por nombre de artista
def filtro_por_nombre_artista():
    nombre_artista = st.selectbox("Nombre del Artista", artist_names)
    resultado = df[df['Artist Name'] == nombre_artista]
    st.write(resultado)
    if not resultado.empty:
        fig = px.bar(resultado, x='Track Name', y='Popularity', color='Track Name', title="Popularidad de las Pistas del Artista")
        st.plotly_chart(fig)

# Función de filtro por nombre de álbum
def filtro_por_nombre_album():
    nombre_album = st.selectbox("Nombre del Álbum", album_names)
    resultado = df[df['Album Name'] == nombre_album]
    st.write(resultado)
    if not resultado.empty:
        fig = px.bar(resultado, x='Track Name', y='Popularity', color='Track Name', title="Popularidad de las Pistas del Álbum")
        st.plotly_chart(fig)

# Selección del filtro
filtro_seleccionado = st.selectbox("Seleccionar filtro", ["Por Nombre de Pista", "Por Nombre de Artista", "Por Nombre de Álbum"])

# Aplicar el filtro seleccionado
if filtro_seleccionado == "Por Nombre de Pista":
    filtro_por_nombre_pista()
elif filtro_seleccionado == "Por Nombre de Artista":
    filtro_por_nombre_artista()
elif filtro_seleccionado == "Por Nombre de Álbum":
    filtro_por_nombre_album()
