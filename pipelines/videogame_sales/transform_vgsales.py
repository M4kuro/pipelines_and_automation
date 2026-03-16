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
    "platform",
    "publisher",
    "na_sales",
    "eu_sales",
    "jp_sales",
    "other_sales"
]
    
    df = df[required_columns]
    
    df = df.rename(
    columns={
        "na_sales": "NA",
        "eu_sales": "EU",
        "jp_sales": "JP",
        "other_sales": "Other",
        "publisher": "pub",
        "platform": "plats"
    }
)
    
    # Drop rows with missing year
    df = df.dropna(subset=["year"]) 
    #Year = 0 should be considered as missing
    df = df[df["year"] > 0] # Or Replaced ?
    

    # Fix data types
    df["year"] = df["year"].astype(int)
    
    # Convert wide → long format
    # This is necessary to make it easier to analyze sales by region and genre over time.
    df_long = df.melt(  
        id_vars=["year", "genre", "plats", "pub"],
        value_vars=["NA", "EU", "JP", "Other"],
        var_name="region",
        value_name="sales",        
    )
    
    df_long = df_long[df_long["sales"] > 0] 

    # Aggregate sales by year, genre, and region and publisher
    df_long = (
        df_long  
        .groupby(["year","genre","plats","region","pub"], as_index=False)
        .agg(sales=("sales", "sum")).round(2) # Round to 2 decimals; Prevent those ginormous weird numbers
        .sort_values("year")
    )
    
    
    
    
    return df_long