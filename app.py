import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.title('Vehicle Listings Dashboard')
exclude_outliers = st.checkbox('Exclude extreme prices')

price_limit = df['price'].quantile(0.99)

if exclude_outliers:
    df_filtered = df[df['price'] <= price_limit]
else:
    df_filtered = df
st.header('Advertised Price Distribution')

price_hist = px.histogram(
    df_filtered,
    x='price',
    nbins=50,
)

st.plotly_chart(price_hist, width='stretch')
st.header('Model Year vs Advertised Price')

scatter_df = df_filtered.dropna(subset=['model_year'])

price_scatter = px.scatter(
    scatter_df,
    x='model_year',
    y='price',
    opacity=0.4,
)

st.plotly_chart(price_scatter, width='stretch')
