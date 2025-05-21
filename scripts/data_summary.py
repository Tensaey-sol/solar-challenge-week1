from IPython.display import display

def summarize_statistics(df):
    """Prints Summary statistics of the DataFrame."""
    display(df.describe(include='all').T)

def report_missing_values(df, threshold=0.05):
    """Prints missing values per column and lists columns with >threshold nulls."""
    na = df.isna().sum().sort_values(ascending=False)
    na = na[na > 0]

    if na.empty:
        print("✅ No missing values found.")
        return

    print("⚠️ Missing Values per Column:")
    display(na)

    important = na[na > threshold * len(df)]
    if not important.empty:
        print(f"🚨 Columns with >{int(threshold * 100)}% nulls:")
        print(important.index.tolist())
    else:
        print("✅ No columns with more than 5% missing values.")