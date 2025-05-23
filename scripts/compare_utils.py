import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, kruskal
import os

color_dict = {
    'Benin': '#1F77B4',
    'Sierra Leone': '#8C564B',
    'Togo': '#17BECF'
}

def load_country_data(files_dict):
    df_list = []
    required_columns = ['Timestamp', 'GHI', 'DNI', 'DHI']
    
    for country, path in files_dict.items():
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        try:
            df = pd.read_csv(path, parse_dates=['Timestamp'])
            missing_cols = [col for col in required_columns if col not in df.columns]
            if missing_cols:
                raise KeyError(f"Missing columns {missing_cols} in {path}")
            df['Country'] = country
            df_list.append(df)
        except pd.errors.EmptyDataError:
            raise ValueError(f"Empty or invalid CSV file: {path}")
    return pd.concat(df_list, ignore_index=True)


def plot_irradiance_boxplots(df, metrics=['GHI', 'DNI', 'DHI']):
    countries = df['Country'].unique()
    cmap = plt.cm.get_cmap('tab10', len(countries))
    color_dict = {country: cmap(i) for i, country in enumerate(countries)}

    fig, axes = plt.subplots(1, len(metrics), figsize=(6 * len(metrics), 5))

    if len(metrics) == 1:
        axes = [axes]

    for i, metric in enumerate(metrics):
        ax = axes[i]
        box = sns.boxplot(x='Country', y=metric, data=df, ax=ax)

        for patch, country in zip(ax.patches, countries):
            patch.set_facecolor(color_dict.get(country, '#333333'))

        ax.set_title(f'{metric} Distribution by Country')
        ax.set_ylabel(f'{metric} (W/m²)')
        ax.set_xlabel('Country')

    plt.tight_layout()
    plt.savefig('figures/irradiance_boxplots.png')



def generate_summary_table(df, metrics=['GHI', 'DNI', 'DHI']):
    summary = df.groupby('Country')[metrics].agg(['mean', 'median', 'std']).round(2)
    summary.columns = ['_'.join(col) for col in summary.columns]
    summary.reset_index(inplace=True)
    return summary  


def interpret_p_value(p_val, alpha=0.05):
    return "Significant" if p_val < alpha else "Not significant"

def perform_stat_tests(df, metrics=['GHI', 'DNI', 'DHI']):
    results = {}
    for metric in metrics:
        groups = [group[metric].dropna() for name, group in df.groupby('Country')]
        f_stat, anova_p = f_oneway(*groups)
        h_stat, kruskal_p = kruskal(*groups)
        results[metric] = {
            'ANOVA': {'F-statistic': round(f_stat, 2), 'p-value': round(anova_p, 4), 'Significance': interpret_p_value(anova_p)},
            'Kruskal–Wallis': {'H-statistic': round(h_stat, 2), 'p-value': round(kruskal_p, 4), 'Significance': interpret_p_value(kruskal_p)}
        }
    return results


def plot_avg_ghi_bar(df):
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    countries = avg_ghi.index.tolist()
    colors = [color_dict.get(country, '#333333') for country in countries]
    plt.figure(figsize=(8, 5))
    avg_ghi.plot(kind='bar', color=colors)
    plt.title('Average GHI by Country')
    plt.ylabel('GHI (W/m²)')
    plt.tight_layout()
    plt.savefig('figures/average_ghi_bar.png')