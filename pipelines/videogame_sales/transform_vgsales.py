import pandas as pd

#! READ BELLOW
'''
After core.transform, all column names are lowercase + snake_case.
Dataset logic must always assume that.
'''

def transform_vgsales_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # Keep only required columns
    required_columns = [
        "year",
        "genre",
        "na_sales",
        "eu_sales",
        "jp_sales",
        "other_sales",
        
    ]
    
    df = df[required_columns]
    
    df=df.rename(  
        columns={
            "na_sales": "NA",
            "eu_sales": "EU",
            "jp_sales": "JP",
            "other_sales": "Other",
        }
    )
    
    # Drop rows with missing year
    df = df.dropna(subset=["year"]) 
    #Year = 0 should be considered as missing
    df = df[df["year"] > 0] # Or Replaced ?
    

    # Fix data types
    df["year"] = df["year"].astype(int)
    
    # Convert wide → long format
    df_long = df.melt(  
        id_vars=["year", "genre"],
        value_vars=["NA", "EU", "JP", "Other"],
        var_name="region",
        value_name="sales",
    )
    
    df_long = df_long[df_long["sales"] > 0] 

    # Aggregate
    df_long = (
        df_long  
        .groupby(["year","genre", "region"], as_index=False)
        .agg(total_sales=("sales", "sum"))
        .sort_values("year")
    )
    

    return df_long