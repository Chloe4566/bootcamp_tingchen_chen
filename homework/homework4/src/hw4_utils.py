from __future__ import annotations
import os, re
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

def load_api_key(env_key: str = "API_KEY") -> str | None:
    return os.getenv(env_key)

def timestamp(fmt: str = "%Y%m%d-%H%M") -> str:
    return datetime.now(timezone.utc).astimezone().strftime(fmt)

def safe_slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", s).strip("-").lower()

def save_raw_csv(df: pd.DataFrame, *, kind: str, source: str, tag: str, outdir: Path) -> Path:
    """
    kind: 'api' 或 'scrape'
    source: 來源名稱（如 yfinance / alphavantage / wikipedia 等）
    tag: 額外資訊（如 TICKER 或 TABLE 名稱）
    outdir: data/raw 目錄
    產出檔名格式：{kind}_{source}_{tag}_{YYYYMMDD-HHMM}.csv
    """
    outdir.mkdir(parents=True, exist_ok=True)
    fname = f"{kind}_{safe_slug(source)}_{safe_slug(tag)}_{timestamp()}.csv"
    path = outdir / fname
    df.to_csv(path, index=False)
    return path

def ensure_dtypes(df: pd.DataFrame, *, date_cols: list[str] = None, float_cols: list[str] = None) -> pd.DataFrame:
    date_cols = date_cols or []
    float_cols = float_cols or []
    for c in date_cols:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors="coerce", utc=True).dt.tz_localize(None)
    for c in float_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def validate_df(df: pd.DataFrame, *, required_cols: list[str], min_rows: int = 1) -> dict:
    """
    回傳簡單驗證報告：缺少欄、NA 統計、形狀是否符合。
    """
    missing = [c for c in required_cols if c not in df.columns]
    na_counts = df[required_cols].isna().sum().to_dict() if not missing else {}
    ok = (len(missing) == 0) and (len(df) >= min_rows)
    return {
        "ok": ok,
        "missing_cols": missing,
        "na_counts": na_counts,
        "shape": df.shape,
    }
