import streamlit as st  # type: ignore
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Análisis de datos financieros")

# Cargar los datos financieros
df = pd.read_csv('static/datasets/META.csv')

# Convertir la columna 'Date' a tipo datetime
df['Date'] = pd.to_datetime(df['Date'])

# Obtener las opciones únicas para los filtros
fechas = sorted(df['Date'].dropna().unique())

# Función de filtro por rango de fechas
def filtro_por_rango_de_fechas():
    fecha_inicial = st.date_input("Fecha inicial", value=fechas[0].date())
    fecha_final = st.date_input("Fecha final", value=fechas[-1].date())
    
    # Convertir fecha_inicial y fecha_final a datetime64[ns]
    fecha_inicial = pd.to_datetime(fecha_inicial)
    fecha_final = pd.to_datetime(fecha_final)
    
    resultado = df[(df['Date'] >= fecha_inicial) & (df['Date'] <= fecha_final)]
    st.write(resultado)

    # Gráfico de líneas de los precios de la acción
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=resultado['Date'], y=resultado['Close'], mode='lines', name='Close'))
    fig.update_layout(title='Precio de cierre a lo largo del rango de fechas seleccionado', xaxis_title='Fecha', yaxis_title='Precio de Cierre')
    st.plotly_chart(fig)

# Función de filtro por precio de cierre
def filtro_por_precio_de_cierre():
    precio_min = st.number_input("Precio de cierre mínimo", min_value=float(df['Close'].min()), max_value=float(df['Close'].max()), value=float(df['Close'].min()))
    precio_max = st.number_input("Precio de cierre máximo", min_value=float(df['Close'].min()), max_value=float(df['Close'].max()), value=float(df['Close'].max()))
    resultado = df[(df['Close'] >= precio_min) & (df['Close'] <= precio_max)]
    st.write(resultado)

    # Gráfico de líneas de los precios de la acción por precio de cierre
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=resultado['Date'], y=resultado['Close'], mode='lines', name='Close'))
    fig.update_layout(title='Precio de Cierre en la Fecha Seleccionada', xaxis_title='Fecha', yaxis_title='Precio de Cierre')
    st.plotly_chart(fig)

# Función de filtro por precio de apertura
def filtro_por_precio_de_apertura():
    st.header('Filtrar por precio de apertura')
    precio_apertura_min = st.number_input('Precio de apertura mínimo:', value=0.0)
    precio_apertura_max = st.number_input('Precio de apertura máximo:', value=df['Open'].max())
    filtered_open = df[(df['Open'] >= precio_apertura_min) & (df['Open'] <= precio_apertura_max)]
    st.dataframe(filtered_open)
    
# Crear el gráfico de líneas con plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_open['Date'], y=filtered_open['Open'], mode='lines', name='Open'))
    fig.update_layout(title='Precio de apertura en el rango seleccionado', xaxis_title='Fecha', yaxis_title='Precio de apertura')
    st.plotly_chart(fig)


# Selección del filtro
filtro_seleccionado = st.selectbox("Seleccionar filtro", ["Por rango de fechas", "Por precio de cierre", "Por precio de apertura"])

# Aplicar el filtro seleccionado
if filtro_seleccionado == "Por rango de fechas":
    filtro_por_rango_de_fechas()
elif filtro_seleccionado == "Por precio de cierre":
    filtro_por_precio_de_cierre()
elif filtro_seleccionado == "Por precio de apertura":
    filtro_por_precio_de_apertura()
