This stage implements a reproducible storage layer for datasets.

## Folder Structure
- `data/raw/` — stores original CSV files as ingested.
- `data/processed/` — stores cleaned or transformed datasets in Parquet format.

## Formats
- **CSV**: Human-readable and widely compatible.
- **Parquet**: Efficient binary columnar format, suitable for analytics and large-scale storage.

## Environment-driven Paths
The paths are configured through the `.env` file:
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed

This allows the notebook and utility functions to automatically locate the correct directories without hardcoding paths.

## Utilities
We provide two helper functions in `src/storage.py`:
- `write_df(df, path)`: Saves a DataFrame to either CSV or Parquet, based on the file suffix.
- `read_df(path)`: Loads a DataFrame from CSV or Parquet, validating the format.

These functions ensure directories are created if missing and provide clear error messages if required engines (e.g., `pyarrow`) are not installed.
