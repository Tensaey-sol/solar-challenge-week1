import numpy as np

def handle_negative_irradiance(df, columns):
    """Replaces negative values in specified irradiance columns with NaN."""
    df = df.copy()
    for col in columns:
        df[col] = df[col].where(df[col] >= 0, np.nan)
    return df

def clean_outliers_and_missing(df, columns, z_threshold=3):
    """Cleans outliers based on z-scores and imputes missing values with median."""
    df = df.copy()
    for col in columns:
        z_col = f'{col}_zscore'
        if z_col in df:
            df = df[df[z_col].abs() <= z_threshold]
        df[col] = df[col].fillna(df[col].median())
        df.drop(columns=z_col, inplace=True, errors='ignore')
    return df
