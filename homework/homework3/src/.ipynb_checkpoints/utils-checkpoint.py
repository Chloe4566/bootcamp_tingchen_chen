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

def get_summary_stats(df: pd.DataFrame, category_col: str | None = None):
    """
    回傳：
      numeric_summary: df 的數值欄位 .describe()
      by_cat: 若提供 category_col，回傳 groupby(category_col) 的數值統計
    """
    numeric_summary = df.describe(include='number')
    by_cat = None
    if category_col and category_col in df.columns:
        by_cat = df.groupby(category_col).describe(include='number')
    return numeric_summary, by_cat

def save_outputs(numeric_summary: pd.DataFrame,
                 by_cat: pd.DataFrame | None,
                 out_dir: Path,
                 base_name: str = "summary"):
    out_dir.mkdir(parents=True, exist_ok=True)
    # 數值統計
    numeric_summary.to_csv(out_dir / f"{base_name}_numeric.csv")
    numeric_summary.to_json(out_dir / f"{base_name}_numeric.json", orient="table")
    # 分組統計（若有）
    if by_cat is not None:
        if isinstance(by_cat.columns, pd.MultiIndex):
            by_cat.columns = ['_'.join([str(c) for c in col if c != '']) for col in by_cat.columns]
        by_cat.to_csv(out_dir / f"{base_name}_by_category.csv")
        by_cat.to_json(out_dir / f"{base_name}_by_category.json", orient="table")

def find_first_categorical(df: pd.DataFrame) -> str | None:
    """找出第一個類別型欄位（object/category），找不到則回傳 None。"""
    for col in df.columns:
        if df[col].dtype == 'object' or str(df[col].dtype).startswith('category'):
            return col
    return None

def basic_plot_by_category_mean(df: pd.DataFrame,
                                category_col: str,
                                value_col: str,
                                out_path: Path):
    """依類別的數值平均畫出 bar chart 並存檔。"""
import matplotlib.pyplot as plt
ax = df.groupby(category_col)[value_col].mean().sort_values().plot(kind="bar")
ax.set_title(f"Mean {value_col} by {category_col}")
ax.set_ylabel(value_col)
plt.tight_layout()
plt.savefig(out_path)
plt.close()

