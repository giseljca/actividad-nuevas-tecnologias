import streamlit as st # type: ignore
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("Análisis de Datos Financieros")

# Cargar los datos financieros
df = pd.read_csv('static/datasets/META.csv')

# Convertir la columna 'Date' a tipo datetime
df['Date'] = pd.to_datetime(df['Date'])

# Obtener las opciones únicas para los filtros
fechas = sorted(df['Date'].dropna().unique())

# Función de filtro por fecha
def filtro_por_fecha():
    fecha = st.selectbox("Fecha", fechas)
    resultado = df[df['Date'] == fecha]
    st.write(resultado)

    # Gráfico de líneas de los precios de la acción
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=resultado['Date'], y=resultado['Close'], mode='lines', name='Close'))
    fig.update_layout(title='Precio de Cierre en la Fecha Seleccionada', xaxis_title='Fecha', yaxis_title='Precio de Cierre')
    st.plotly_chart(fig)

# Función de filtro por rango de fechas
def filtro_por_rango_de_fechas():
    fecha_inicial = st.date_input("Fecha Inicial", value=fechas[0].date())
    fecha_final = st.date_input("Fecha Final", value=fechas[-1].date())
    
    # Convertir fecha_inicial y fecha_final a datetime64[ns]
    fecha_inicial = pd.to_datetime(fecha_inicial)
    fecha_final = pd.to_datetime(fecha_final)
    
    resultado = df[(df['Date'] >= fecha_inicial) & (df['Date'] <= fecha_final)]
    st.write(resultado)

    # Gráfico de líneas de los precios de la acción
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=resultado['Date'], y=resultado['Close'], mode='lines', name='Close'))
    fig.update_layout(title='Precio de Cierre a lo largo del Rango de Fechas Seleccionado', xaxis_title='Fecha', yaxis_title='Precio de Cierre')
    st.plotly_chart(fig)

# Función de filtro por precio de cierre
def filtro_por_precio_de_cierre():
    precio_min = st.number_input("Precio de Cierre Mínimo", min_value=float(df['Close'].min()), max_value=float(df['Close'].max()), value=float(df['Close'].min()))
    precio_max = st.number_input("Precio de Cierre Máximo", min_value=float(df['Close'].min()), max_value=float(df['Close'].max()), value=float(df['Close'].max()))
    resultado = df[(df['Close'] >= precio_min) & (df['Close'] <= precio_max)]
    st.write(resultado)

    # Gráfico de líneas de los precios de la acción por precio de cierre
    # Gráfico de líneas de los precios de la acción
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=resultado['Date'], y=resultado['Close'], mode='lines', name='Close'))
    fig.update_layout(title='Precio de Cierre en la Fecha Seleccionada', xaxis_title='Fecha', yaxis_title='Precio de Cierre')
    st.plotly_chart(fig)


# Selección del filtro
filtro_seleccionado = st.selectbox("Seleccionar filtro", ["Por Fecha", "Por Rango de Fechas", "Por Precio de Cierre"])

# Aplicar el filtro seleccionado
if filtro_seleccionado == "Por Fecha":
    filtro_por_fecha()
elif filtro_seleccionado == "Por Rango de Fechas":
    filtro_por_rango_de_fechas()
elif filtro_seleccionado == "Por Precio de Cierre":
    filtro_por_precio_de_cierre()