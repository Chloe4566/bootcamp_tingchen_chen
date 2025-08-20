import pandas as pd
import numpy as np

def fill_missing_median(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Fill missing values in the specified columns with the median of each column.
    """
    for col in cols:
        if col in df.columns:
            median = df[col].median()
            df[col] = df[col].fillna(median)
    return df


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """
    Drop rows where the fraction of missing values exceeds the threshold.
    threshold=0.5 means if more than 50% of a row is NaN, drop it.
    """
    return df.dropna(thresh=int((1 - threshold) * len(df.columns)))


def normalize_data(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Normalize the given columns using Min-Max scaling (0–1 range).
    """
    for col in cols:
        if col in df.columns:
            min_val = df[col].min()
            max_val = df[col].max()
            if pd.notna(min_val) and pd.notna(max_val) and max_val > min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
    return df
