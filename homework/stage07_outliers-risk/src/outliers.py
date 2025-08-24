import pandas as pd
import numpy as np
from scipy import stats

def detect_outliers_iqr(series: pd.Series, factor: float = 1.5) -> pd.Series:
    """
    Detect outliers in a numeric series using the IQR rule.
    
    Parameters
    ----------
    series : pd.Series
        Numeric column to evaluate.
    factor : float, default=1.5
        Multiplier for IQR. Larger factor = less sensitive.

    Returns
    -------
    pd.Series (bool)
        Boolean mask where True indicates an outlier.
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - factor * iqr
    upper = q3 + factor * iqr
    return (series < lower) | (series > upper)


def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """
    Detect outliers in a numeric series using Z-score.

    Parameters
    ----------
    series : pd.Series
        Numeric column to evaluate.
    threshold : float, default=3.0
        Absolute Z-score above this threshold is considered an outlier.

    Returns
    -------
    pd.Series (bool)
        Boolean mask where True indicates an outlier.
    """
    z_scores = np.abs(stats.zscore(series.dropna()))
    mask = pd.Series(False, index=series.index)
    mask[series.dropna().index] = z_scores > threshold
    return mask


def winsorize_series(series: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:
    """
    Winsorize a numeric series by capping extreme values to given quantiles.

    Parameters
    ----------
    series : pd.Series
        Numeric column to modify.
    lower : float, default=0.05
        Lower quantile cutoff.
    upper : float, default=0.95
        Upper quantile cutoff.

    Returns
    -------
    pd.Series
        Winsorized series with capped values.
    """
    lower_val = series.quantile(lower)
    upper_val = series.quantile(upper)
    return series.clip(lower=lower_val, upper=upper_val)
