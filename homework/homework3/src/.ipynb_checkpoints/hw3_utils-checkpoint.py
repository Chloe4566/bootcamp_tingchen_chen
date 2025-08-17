import pandas as pd

def get_summary_stats(df: pd.DataFrame, by: str | None = None):
    """
    若 by=None：回傳數值欄位的 describe()（轉置，較易讀）
    若 by 非 None：回傳 df.groupby(by) 對數值欄位的 count/mean/std/min/max
    """
    numeric_df = df.select_dtypes(include="number")
    if by is None:
        return numeric_df.describe().T

    grouped = df.groupby(by)[numeric_df.columns].agg(['count','mean','std','min','max'])
    # 攤平多層欄名
    grouped.columns = ['_'.join([c for c in col if c]) for col in grouped.columns.values]
    return grouped

from pathlib import Path
import pandas as pd

def _flatten_multiindex_columns(df: pd.DataFrame) -> pd.DataFrame:
    """若欄位是 MultiIndex，攤平成單層欄名。"""
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = ['_'.join([str(c) for c in col if c]) for col in df.columns.values]
    return df

def save_outputs(numeric_summary: pd.DataFrame,
                 by_cat: pd.DataFrame | None,
                 out_dir: Path,
                 base_name: str = "summary") -> None:
    """把統計結果存成 CSV/JSON（自動處理 MultiIndex 欄名）。"""
    out_dir.mkdir(parents=True, exist_ok=True)

    num_out = _flatten_multiindex_columns(numeric_summary)
    num_out.to_csv(out_dir / f"{base_name}_numeric.csv")
    num_out.to_json(out_dir / f"{base_name}_numeric.json", orient="table")

    if by_cat is not None:
        by_out = _flatten_multiindex_columns(by_cat)
        by_out.to_csv(out_dir / f"{base_name}_by_category.csv")
        by_out.to_json(out_dir / f"{base_name}_by_category.json", orient="table")

def find_first_categorical(df: pd.DataFrame) -> str | None:
    """找出第一個類別型欄位（object/category），找不到則回傳 None。"""
    for col in df.columns:
        if df[col].dtype == 'object' or str(df[col].dtype).startswith('category'):
            return col
    return None

def basic_plot_by_category_mean(df: pd.DataFrame,
                                category_col: str,
                                value_col: str,
                                out_path: Path) -> None:
    """依類別的數值平均畫出 bar chart 並存檔。"""
    import matplotlib.pyplot as plt
    ax = df.groupby(category_col)[value_col].mean().sort_values().plot(kind="bar")
    ax.set_title(f"Mean {value_col} by {category_col}")
    ax.set_ylabel(value_col)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
