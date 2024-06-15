import streamlit as st # type: ignore
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Análisis de Datos Financieros")

# Cargar los datos financieros
df = pd.read_csv('static/datasets/META.csv')

# Convertir la columna 'Date' a tipo datetime
df['Date'] = pd.to_datetime(df['Date'])

# Obtener las opciones únicas para los filtros
fechas = sorted(df['Date'].dropna().unique())

# Filtrar por precio de apertura
st.header('Filtrar por precio de apertura')
precio_apertura = st.number_input('Precio de Apertura mayor a:', value=0.0)
filtered_open = df[df['Open'] > precio_apertura]
st.dataframe(filtered_open)

# Generar categorías de intervalos de precios
intervalos = [0, 100, 200, 300, 400, 500, 600]
labels = ['0-100', '100-200', '200-300', '300-400', '400-500', '500-600']
filtered_open['Price_Range'] = pd.cut(filtered_open['Open'], bins=intervalos, labels=labels, include_lowest=True)

# Contar las ocurrencias en cada intervalo
counts = filtered_open['Price_Range'].value_counts().sort_index()

# Crear el gráfico de pastel
fig, ax = plt.subplots()
ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Mostrar el gráfico en Streamlit
st.header('Gráfico de Pastel de Intervalos de Precio de Apertura')
st.pyplot(fig)

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
    precio_apertura()
elif filtro_seleccionado == "Por Rango de Fechas":
    filtro_por_rango_de_fechas()
elif filtro_seleccionado == "Por Precio de Cierre":
    filtro_por_precio_de_cierre()