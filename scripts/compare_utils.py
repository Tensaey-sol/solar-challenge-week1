import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, kruskal
import os

def load_country_data(files_dict):
    """
    Load and combine CSV files for each country, adding a 'Country' column.
    
    Args:
        files_dict (dict): Dictionary with country names as keys and file paths as values.
                           Example: {'Benin': 'path_to_benin.csv', ...}
    
    Returns:
        pd.DataFrame: Combined DataFrame with a 'Country' column.
    
    Raises:
        FileNotFoundError: If a file path does not exist.
        KeyError: If required columns are missing.
        ValueError: If a CSV file is empty or invalid.
    """
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
    """
    Generate boxplots for specified irradiance metrics across countries.
    
    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and metric columns.
        metrics (list): List of column names to plot (default: ['GHI', 'DNI', 'DHI']).
    
    Saves:
        Boxplot images to 'figures/{metric}_boxplot.png'.
    """
    for metric in metrics:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x='Country', y=metric, data=df)
        plt.title(f'{metric} Distribution by Country', fontsize=12)
        plt.ylabel(f'{metric} (W/m²)', fontsize=10)
        plt.xlabel('Country', fontsize=10)
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(f'figures/{metric}_boxplot.png', dpi=300)
        plt.close()

def generate_summary_table(df, metrics=['GHI', 'DNI', 'DHI']):
    """
    Generate a summary table with mean, median, and standard deviation for each metric by country.
    
    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and metric columns.
        metrics (list): List of column names to summarize (default: ['GHI', 'DNI', 'DHI']).
    
    Returns:
        pd.DataFrame: Summary table with rounded values.
    
    Saves:
        Summary table to 'figures/summary_table.csv'.
    """
    summary = df.groupby('Country')[metrics].agg(['mean', 'median', 'std']).round(2)
    summary.columns = ['_'.join(col) for col in summary.columns]
    summary.to_csv('figures/summary_table.csv')
    return summary

def interpret_p_value(p_val, alpha=0.05):
    """
    Interpret p-value significance.
    
    Args:
        p_val (float): P-value from statistical test.
        alpha (float): Significance level (default: 0.05).
    
    Returns:
        str: 'Significant' or 'Not significant'.
    """
    return "Significant" if p_val < alpha else "Not significant"

def perform_stat_tests(df, metrics=['GHI', 'DNI', 'DHI']):
    """
    Perform ANOVA and Kruskal–Wallis tests for specified metrics across countries.
    
    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and metric columns.
        metrics (list): List of column names to test (default: ['GHI', 'DNI', 'DHI']).
    
    Returns:
        dict: Results with F/H statistics, p-values, and significance for each metric.
    """
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
    """
    Create a bar chart configuration for average GHI by country using chart.js format.
    
    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and 'GHI' columns.
    
    Returns:
        dict: Chart.js configuration for bar chart.
    """
    avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    countries = avg_ghi.index.tolist()
    values = avg_ghi.values.tolist()
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c'][:len(countries)]  # Match number of countries
    
    return {
        "type": "bar",
        "data": {
            "labels": countries,
            "datasets": [{
                "label": "Average GHI (W/m²)",
                "data": values,
                "backgroundColor": colors,
                "borderColor": colors,
                "borderWidth": 1
            }]
        },
        "options": {
            "scales": {
                "y": {
                    "beginAtZero": True,
                    "title": {
                        "display": True,
                        "text": "GHI (W/m²)"
                    },
                    "grid": {
                        "display": True,
                        "drawBorder": True
                    }
                },
                "x": {
                    "title": {
                        "display": True,
                        "text": "Country"
                    }
                }
            },
            "plugins": {
                "legend": {
                    "display": False
                },
                "title": {
                    "display": True,
                    "text": "Average GHI by Country"
                }
            }
        }
    }

def generate_key_observations(df, stat_results):
    """
    Generate key observations based on summary statistics and statistical tests.
    
    Args:
        df (pd.DataFrame): Combined DataFrame with 'Country' and metric columns.
        stat_results (dict): Results from perform_stat_tests.
    
    Returns:
        str: Markdown-formatted string with three key observations.
    """
    summary = generate_summary_table(df)
    observations = []
    
    # Highest median GHI
    max_median_ghi = summary['GHI_median'].idxmax()
    observations.append(f"- **{max_median_ghi}** has the highest median GHI ({summary.loc[max_median_ghi, 'GHI_median']} W/m²), indicating strong solar potential.")
    
    # Greatest variability
    max_std_ghi = summary['GHI_std'].idxmax()
    observations.append(f"- **{max_std_ghi}** shows the greatest GHI variability (std = {summary.loc[max_std_ghi, 'GHI_std']} W/m²), suggesting less predictable solar output.")
    
    # Statistical significance
    ghi_significance = stat_results['GHI']['ANOVA']['Significance']
    observations.append(f"- ANOVA test for GHI differences is {ghi_significance.lower()} (p={stat_results['GHI']['ANOVA']['p-value']:.4f}), indicating {'notable' if ghi_significance == 'Significant' else 'minimal'} differences in GHI across countries.")
    
    return "\n".join(observations)