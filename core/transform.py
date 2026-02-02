import pandas as pd

# Standard data transformation function
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    
    # 1. Standardize column names
    df.columns = (
        df.columns
        .str.strip() 
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Drop duplicate rows
    df = df.drop_duplicates()

    # 3. Handle missing values
    for col in df.select_dtypes(include="number").columns: 
        df[col] = df[col].fillna(0) 

    for col in df.select_dtypes(include="object").columns: 
        df[col] = df[col].fillna("unknown") 

    return df


