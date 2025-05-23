import streamlit as st
import pandas as pd
from utils import (
    load_data,
    generate_radiation_boxplot,
    get_top_regions
)

st.set_page_config(page_title="Solar GHI Dashboard", layout="wide")
st.title("🔆 Solar Global Horizontal Irradiance (GHI) Dashboard")

# Load data
benin_df = load_data("https://drive.google.com/uc?export=download&id=1Cj-Jn1osz2TjqLQKHiuRj2d87XZf3lrg", country_name="Benin")
togo_df = load_data("https://drive.google.com/uc?export=download&id=1qAZiiwfkuzd1uL8boZvmH91Duro-zoRI", country_name="Togo")
sierra_df = load_data("https://drive.google.com/uc?export=download&id=1Z_Ac2wfmYjfAx7mC9N9nng0xeXj6Kx2G", country_name="Sierra Leone")
df = pd.concat([benin_df, togo_df, sierra_df], ignore_index=True)

# Country selection
countries = sorted(df["Country"].unique())
selected_countries = st.multiselect("Select countries", countries, default=countries)

filtered_df = df[df["Country"].isin(selected_countries)]

# GHI Boxplot
st.subheader("📦 GHI Distribution by Country")
if not filtered_df.empty:
    fig = generate_radiation_boxplot(filtered_df, column="GHI")
    st.pyplot(fig)
else:
    st.warning("Please select at least one country.")

# Top regions table
st.subheader("🏆 Top Regions by GHI")
top_n = st.slider("Top N Regions", min_value=3, max_value=10, value=3)
if not filtered_df.empty:
    top_regions_df = get_top_regions(filtered_df, column="GHI", top_n=top_n)
    st.dataframe(top_regions_df)
else:
    st.info("No data to show.")
