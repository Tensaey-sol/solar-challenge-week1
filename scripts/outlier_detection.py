from scipy.stats import zscore
import matplotlib.pyplot as plt
import seaborn as sns

def compute_z_scores(df, columns):
    """Computes z-scores for specified columns after filling NaNs with median."""
    df = df.copy()
    for col in columns:
        df[f'{col}_zscore'] = zscore(df[col].fillna(df[col].median()))
    return df

def plot_zscore_distribution(df, columns):
    """Plots distribution of z-scores for specified columns."""
    fig, axes = plt.subplots(len(columns), 1, figsize=(8, 4 * len(columns)))
    if len(columns) == 1:
        axes = [axes]
    for i, col in enumerate(columns):
        z_col = f'{col}_zscore'
        if z_col in df:
            sns.histplot(df[z_col], bins=30, kde=True, ax=axes[i])
            axes[i].set_title(f'Z-score Distribution for {col}')
    plt.tight_layout()
    plt.savefig('figures/zscore_distribution.png')

def plot_boxplots(df, columns):
    """Plots boxplots for specified columns."""
    plt.figure(figsize=(12, 6))
    df[columns].boxplot()
    plt.title("Boxplots of Selected Columns")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('figures/boxplots.png')
