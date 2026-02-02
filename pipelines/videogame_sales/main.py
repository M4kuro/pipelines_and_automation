from core.extract import extract_csv
from core.load import load_csv 
from core.transform import transform_data

# Business-logic import
from pipelines.videogame_sales.transform_vgsales import transform_vgsales_data


RAW_PATH = "data/raw/vgsales.csv"
OUTPUT_PATH = "data/processed/vgsales_clean.csv"

def run():
    df = extract_csv(RAW_PATH)
    df = transform_data(df) # Standard transformation
    df = transform_vgsales_data(df) # bussiness-specific transformation

    print(df.head())
    print(df.dtypes)

    load_csv(df, OUTPUT_PATH)

if __name__ == "__main__":
    run()


