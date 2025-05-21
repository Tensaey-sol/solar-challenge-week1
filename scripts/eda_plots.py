import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes

def plot_time_series(df_daytime):
    fig, axes = plt.subplots(4, 1, figsize=(15, 12), sharex=True)
    df_daytime["GHI"].plot(ax=axes[0], title="GHI over Time (Daytime)")
    df_daytime["DNI"].plot(ax=axes[1], title="DNI over Time (Daytime)")
    df_daytime["DHI"].plot(ax=axes[2], title="DHI over Time (Daytime)")
    df_daytime["Tamb"].plot(ax=axes[3], title="Ambient Temperature over Time (Daytime)")
    plt.tight_layout()
    plt.savefig('figures/time_series_daytime.png')

def plot_monthly_avg(df_clean):
    df_clean['Month'] = df_clean.index.month
    monthly_avg = df_clean.groupby('Month')[['GHI', 'DNI', 'DHI']].mean()
    monthly_avg.plot(kind='bar', figsize=(10, 6))
    plt.title('Monthly Average GHI, DNI, DHI')
    plt.xlabel('Month')
    plt.ylabel('Average Irradiance (W/m²)')
    plt.tight_layout()
    plt.savefig('figures/monthly_avg.png')

def plot_cleaning_impact(df_clean):
    if len(df_clean['Cleaning'].unique()) > 1:
        fig, ax = plt.subplots(figsize=(10, 6))
        df_clean.groupby("Cleaning")[["ModA", "ModB"]].mean().plot(kind="bar", ax=ax)
        ax.set_title("Average ModA and ModB by Cleaning Flag")
        ax.set_ylabel("Mean Sensor Value")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig('figures/cleaning_impact.png')
    else:
        print("Cleaning column has no variation (all values are the same). Skipping cleaning impact plot.")

def plot_correlation_heatmap(df_clean, columns):
    plt.figure(figsize=(8, 6))
    sns.heatmap(df_clean[columns].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig('figures/correlation_heatmap.png')

def plot_scatter_plots(df_clean, scatter_pairs):
    fig, axes = plt.subplots(3, 2, figsize=(15, 12))
    axes = axes.flatten()
    for i, (x, y) in enumerate(scatter_pairs):
        sns.scatterplot(data=df_clean, x=x, y=y, ax=axes[i])
        axes[i].set_title(f"{x} vs {y}")
        axes[i].set_xlabel(x)
        axes[i].set_ylabel(y)
    plt.tight_layout()
    plt.savefig('figures/scatter_plots.png')

def plot_wind_rose(df_clean):
    fig = plt.figure(figsize=(8, 6))
    ax = WindroseAxes.from_ax(fig=fig)
    ax.bar(df_clean["WD"], df_clean["WS"], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend()
    plt.title("Wind Rose: Wind Speed and Direction")
    plt.savefig('figures/wind_rose.png')

def plot_histograms(df_clean):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    sns.histplot(df_clean["GHI"], bins=30, kde=True, ax=axes[0])
    axes[0].set_title("Distribution of GHI")
    axes[0].set_xlabel("GHI (W/m²)")
    axes[0].set_ylabel("Frequency")
    sns.histplot(df_clean["WS"], bins=30, kde=True, ax=axes[1])
    axes[1].set_title("Distribution of Wind Speed (WS)")
    axes[1].set_xlabel("Wind Speed (m/s)")
    axes[1].set_ylabel("Frequency")
    plt.tight_layout()
    plt.savefig('figures/histograms.png')

def plot_temperature_analysis(df_clean):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.scatterplot(data=df_clean, x="RH", y="Tamb", ax=axes[0])
    axes[0].set_title("RH vs Ambient Temperature")
    axes[0].set_xlabel("Relative Humidity (%)")
    axes[0].set_ylabel("Ambient Temperature (°C)")
    sns.scatterplot(data=df_clean, x="RH", y="GHI", ax=axes[1])
    axes[1].set_title("RH vs GHI")
    axes[1].set_xlabel("Relative Humidity (%)")
    axes[1].set_ylabel("GHI (W/m²)")
    plt.tight_layout()
    plt.savefig('figures/temperature_analysis.png')

def plot_bubble_chart(df_daytime):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    rh_scaled = (df_daytime["RH"] - df_daytime["RH"].min()) / (df_daytime["RH"].max() - df_daytime["RH"].min()) * 990 + 10
    bp_scaled = (df_daytime["BP"] - df_daytime["BP"].min()) / (df_daytime["BP"].max() - df_daytime["BP"].min()) * 990 + 10
    sns.scatterplot(data=df_daytime, x="Tamb", y="GHI", size=rh_scaled, sizes=(10, 1000), alpha=0.5, ax=axes[0])
    axes[0].set_title("GHI vs Tamb (Bubble Size: RH, Daytime)")
    sns.scatterplot(data=df_daytime, x="Tamb", y="GHI", size=bp_scaled, sizes=(10, 1000), alpha=0.5, ax=axes[1])
    axes[1].set_title("GHI vs Tamb (Bubble Size: BP, Daytime)")
    for ax in axes:
        ax.set_xlabel("Ambient Temperature (°C)")
        ax.set_ylabel("GHI (W/m²)")
    plt.tight_layout()
    plt.savefig('figures/bubble_chart_daytime.png')
