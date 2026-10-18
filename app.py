import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

st.title('Vehicle Listings Dashboard')
st.caption(
    'Explore vehicle listings by type, condition, transmission, '
    'and advertised price.'
)

st.sidebar.header('Filters')
exclude_outliers = st.sidebar.checkbox(
    'Exclude extreme prices',
    help='Removes advertised prices above the 99th percentile.'
)

vehicle_types = sorted(df['type'].dropna().unique())
conditions = sorted(df['condition'].dropna().unique())
transmissions = sorted(df['transmission'].dropna().unique())

selected_types = st.sidebar.multiselect(
    'Vehicle type',
    vehicle_types,
    placeholder='All vehicle types'
)

type_filter = selected_types if selected_types else vehicle_types

selected_conditions = st.sidebar.multiselect(
    'Condition',
    conditions,
    placeholder='All conditions'
)
condition_filter = (
    selected_conditions if selected_conditions else conditions
)

selected_transmissions = st.sidebar.multiselect(
    'Transmission',
    transmissions,
    placeholder='All transmissions'
)
transmission_filter = (
    selected_transmissions if selected_transmissions else transmissions
)

df_filtered = df[
    df['type'].isin(type_filter)
    & df['condition'].isin(condition_filter)
    & df['transmission'].isin(transmission_filter)
].copy()

price_limit = df['price'].quantile(0.99)

if exclude_outliers:
    df_filtered = df_filtered[df_filtered['price'] <= price_limit]

if df_filtered.empty:
    st.warning('No listings match the selected filters.')
    st.stop()
col1, col2, col3 = st.columns(3)

col1.metric(
    'Listings',
    f'{len(df_filtered):,}'
)

col2.metric(
    'Median advertised price',
    f"${df_filtered['price'].median():,.0f}"
)

col3.metric(
    'Median model year',
    f"{df_filtered['model_year'].median():.0f}"
)
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
    color='condition',
    opacity=0.5,
    labels={
        'model_year': 'Model year',
        'price': 'Advertised price',
        'condition': 'Condition'
    }
)

st.plotly_chart(price_scatter, width='stretch')

with st.expander('View filtered data'):
    st.dataframe(
        df_filtered,
        width='stretch'
    )
