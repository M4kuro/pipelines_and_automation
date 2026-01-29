from core.extract import extract_csv
from core.transform import transform_vgsales_data as transform
from core.load import load_csv 

RAW_PATH = "data/raw/vgsales.csv"
OUTPUT_PATH = "data/processed/vgsales_clean.csv"

def run():
    df = extract_csv(RAW_PATH)
    df = transform(df)

    print(df.head())
    print(df.dtypes)

    load_csv(df, OUTPUT_PATH)

if __name__ == "__main__":
    run()


