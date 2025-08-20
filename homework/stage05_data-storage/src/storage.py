from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import pandas as pd

def ts(fmt: str = "%Y%m%d-%H%M") -> str:
    return datetime.now(timezone.utc).astimezone().strftime(fmt)

def _ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def write_df(df: pd.DataFrame, path: Path) -> Path:
    """Route by suffix (.csv/.parquet). Auto-create dirs. Helpful error if parquet engine missing."""
    path = Path(path)
    _ensure_dir(path.parent)
    suf = path.suffix.lower()
    if suf == ".csv":
        df.to_csv(path, index=False)
        return path
    elif suf == ".parquet":
        try:
            df.to_parquet(path, index=False)
            return path
        except Exception as e:
            raise RuntimeError("Parquet write failed: install 'pyarrow' or 'fastparquet'.") from e
    else:
        raise ValueError(f"Unsupported suffix: {suf}. Use .csv or .parquet")

def read_df(path: Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    suf = path.suffix.lower()
    if suf == ".csv":
        return pd.read_csv(path)
    elif suf == ".parquet":
        try:
            return pd.read_parquet(path)
        except Exception as e:
            raise RuntimeError("Parquet read failed: install 'pyarrow' or 'fastparquet'.") from e
    else:
        raise ValueError(f"Unsupported suffix: {suf}. Use .csv or .parquet")
