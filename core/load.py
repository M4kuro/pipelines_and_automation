from pathlib import Path

def load_csv(df, output_path: str) -> None: # type: ignore
    output_path = Path(output_path) # type: ignore
    output_path.parent.mkdir(parents=True, exist_ok=True) # type: ignore

    df.to_csv(output_path, index=False) # type: ignore

