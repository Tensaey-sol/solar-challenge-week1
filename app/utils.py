import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

color_dict = {
    'Benin': '#1F77B4',
    'Sierra Leone': '#8C564B',
    'Togo': '#17BECF'
}

def load_data(url, country_name=None):
    df = pd.read_csv(url)
    if country_name:
        df["Country"] = country_name
    df.columns = df.columns.str.strip()
    return df

def generate_radiation_boxplot(df, column="GHI"):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x="Country", y=column, ax=ax, palette=color_dict)
    ax.set_title(f"{column} Distribution by Country")
    ax.set_ylabel(column)
    ax.set_xlabel("Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def get_top_regions(df, column="GHI", top_n=5):
    if "Region" in df.columns:
        return df.sort_values(by=column, ascending=False)[["Region", "Country", column]].head(top_n)
    else:
        return df.sort_values(by=column, ascending=False)[["Country", column]].head(top_n)
