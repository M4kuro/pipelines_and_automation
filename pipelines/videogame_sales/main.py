import yaml
from core.extract import extract_csv
from core.load import load_csv 
from core.transform import transform_data

# Business-logic import
from pipelines.videogame_sales.transform_vgsales import transform_vgsales_data

CONFIG_PATH = "pipelines/videogame_sales/config.yaml"


def run():
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)


    df = extract_csv(config["raw_path"])
    df = transform_data(df) # Standard transformation
    df = transform_vgsales_data(df) # bussiness-specific transformation
    
    load_csv(df, config["output_path"])

    print(df.head())
    print(df.dtypes)

    print("Pipeline executed successfully.")

if __name__ == "__main__":
    run()


