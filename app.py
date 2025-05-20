import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de Anuncios de Venta de Vehículos')

# Mostrar las primeras filas de los datos
st.write('### Primeros 50 vehiculos')
st.write(df.head(50))

# Crear un histograma interactivo con Plotly Express
st.subheader('Selecciona el rango de precios')
min_price = int(df['price'].min())
max_price = int(df['price'].max())

price_range = st.slider(
    'Rango de precios (USD)',
    min_value=min_price,
    max_value=max_price,
    value=(0, 20000)  # Rango por defecto
)

filtered_df = df[(df['price'] >= price_range[0]) &
                 (df['price'] <= price_range[1])]

fig = px.histogram(
    filtered_df,
    x='price',
    nbins=50,
    color_discrete_sequence=['indigo'],
    title=f'Distribución de Precios (${price_range[0]} - ${price_range[1]})'
)

fig.update_layout(
    xaxis_title='Precio (USD)',
    yaxis_title='Número de vehículos',
    bargap=0.1,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    title_x=0.5
)

st.plotly_chart(fig)


st.header('Análisis de Anuncios de Vehículos')

# Casilla de verificación para mostrar el gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión Precio vs. Kilometraje'):
    scatter_fig = px.scatter(
        df,
        x='odometer',
        y='price',
        color='transmission',
        title='Precio vs. Kilometraje (por tipo de transmisión)',
        labels={'odometer': 'Kilometraje',
                'price': 'Precio (USD)', 'transmission': 'Transmisión'},
        opacity=0.6,
        color_discrete_map={
            'manual': 'blue',
            'automatic': 'red',
            'other': 'green'
        }
    )

    scatter_fig.update_traces(marker=dict(size=8))

    st.plotly_chart(scatter_fig)
