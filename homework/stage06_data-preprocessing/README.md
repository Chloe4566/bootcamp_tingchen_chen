# Stage 06: Data Preprocessing

## Cleaning Strategy
- **fill_missing_median()**: Replace missing numeric values with the column median.  
- **drop_missing()**: Drop rows that exceed a missing value threshold (default 50%).  
- **normalize_data()**: Scale numeric features to [0,1] range for comparability.  

These modular functions ensure reproducibility and can be reused for different datasets.  
