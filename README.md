# Dashboard de anuncios de vehículos

Aplicación web interactiva desarrollada con Streamlit para explorar un conjunto de datos de anuncios de vehículos y analizar la distribución de sus precios y su relación con el año del modelo.

## Funcionalidades

El dashboard permite:

- Visualizar el número de anuncios disponibles según los filtros seleccionados.
- Consultar la mediana del precio anunciado y del año del modelo.
- Filtrar los anuncios por tipo de vehículo, condición y transmisión.
- Excluir precios extremos superiores al percentil 99 para facilitar la visualización de la distribución principal de los datos.
- Explorar un histograma interactivo de la distribución de precios anunciados.
- Analizar la relación entre el año del modelo y el precio mediante un gráfico de dispersión.
- Diferenciar los puntos del gráfico de dispersión según la condición del vehículo.
- Consultar en una tabla desplegable los registros correspondientes a los filtros seleccionados.
- Mostrar un mensaje informativo cuando una combinación de filtros no contiene resultados.

## Tecnologías utilizadas

- Python
- Pandas
- Plotly
- Streamlit

## Conjunto de datos

El conjunto de datos contiene anuncios de vehículos con información como precio, año del modelo, modelo, condición, kilometraje, tipo de combustible, transmisión, tipo de vehículo y fecha de publicación del anuncio.

## Análisis exploratorio

El análisis exploratorio utilizado como base para el desarrollo del dashboard se encuentra en:

`notebooks/EDA.ipynb`

## Aplicación web

La aplicación está desplegada en Render.

**URL de Render:** https://vehicles-dashboard-o3ie.onrender.com