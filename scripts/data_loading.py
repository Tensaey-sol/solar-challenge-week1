import pandas as pd

def load_data(filepath):
    """Loads CSV data into a pandas DataFrame with error handling."""
    try:
        df = pd.read_csv(filepath, parse_dates=['Timestamp'])
        if "Comments" in df.columns:
            df = df.drop(columns=["Comments"])
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found. Please check the path.")
        raise
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
