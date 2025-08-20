import pathlib
import pandas as pd
import typing as t

def detect_format(path: t.Union[str, pathlib.Path]) -> str:
    """判斷檔案格式 (csv / parquet)"""
    s = str(path).lower()
    if s.endswith('.csv'):
        return 'csv'
    if s.endswith('.parquet') or s.endswith('.pq') or s.endswith('.parq'):
        return 'parquet'
    raise ValueError(f'Unsupported format: {s}')

def write_df(df: pd.DataFrame, path: t.Union[str, pathlib.Path]) -> pathlib.Path:
    """根據副檔名自動存檔，並自動建立資料夾"""
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fmt = detect_format(p)

    if fmt == 'csv':
        df.to_csv(p, index=False)
    else:
        try:
            df.to_parquet(p, index=False)
        except Exception as e:
            raise RuntimeError("Parquet engine not available. Install pyarrow or fastparquet.") from e
    return p

def read_df(path: t.Union[str, pathlib.Path]) -> pd.DataFrame:
    """根據副檔名自動讀檔，支援 CSV 與 Parquet"""
    p = pathlib.Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")

    fmt = detect_format(p)

    if fmt == 'csv':
        # 如果檔案有 date 欄位，就自動 parse 成 datetime
        header = pd.read_csv(p, nrows=0).columns
        parse_cols = ['date'] if 'date' in header else None
        return pd.read_csv(p, parse_dates=parse_cols)
    else:
        try:
            return pd.read_parquet(p)
        except Exception as e:
            raise RuntimeError("Parquet engine not available. Install pyarrow or fastparquet.") from e
