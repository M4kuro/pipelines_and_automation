import pandas as pd

# Standard data transformation function
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # 1. Standardize column names
    df.columns = (
        df.columns
        .str.strip() # type: ignore
        .str.lower()
        .str.replace(" ", "_")
    )

    # 2. Drop duplicate rows
    df = df.drop_duplicates()

    # 3. Handle missing values
    for col in df.select_dtypes(include="number").columns: # type: ignore
        df[col] = df[col].fillna(0) # type: ignore

    for col in df.select_dtypes(include="object").columns: # type: ignore
        df[col] = df[col].fillna("unknown") # type: ignore

    return df


# Additional function for transforming video game sales data
def transform_vgsales_data(df: pd.DataFrame) -> pd.DataFrame:
    # Keep only required columns
    df = df[
        [
            "Year",
            "Genre",
            "NA_Sales",
            "EU_Sales",
            "JP_Sales",
            "Other_Sales",
        ]
    ]

    # Drop rows with missing year
    df = df.dropna(subset=["Year"]) # type: ignore

    # Fix data types
    df["Year"] = df["Year"].astype(int)

    # Rename columns
    df = df.rename(
        columns={
            "Year": "year",
            "Genre": "genre",
            "NA_Sales": "NA",
            "EU_Sales": "EU",
            "JP_Sales": "JP",
            "Other_Sales": "Other",
        }
    )

    # Convert wide → long format
    df_long = df.melt(  # type: ignore
        id_vars=["year", "genre"],
        var_name="region",
        value_name="sales",
    )
    df_long = df_long[df_long["sales"] > 0]  # type: ignore

    # Aggregate
    df_long = (
        df_long  # type: ignore
        .groupby(["year", "genre", "region"], as_index=False)
        .agg({"sales": "sum"})
        .sort_values("year")
    )
    

    return df_long