import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
FILES = [
    DATA_DIR / "daily_sales_data_0.csv",
    DATA_DIR / "daily_sales_data_1.csv",
    DATA_DIR / "daily_sales_data_2.csv",
]

def parse_price_to_float(price_series: pd.Series) -> pd.Series:
    # "$3.00" -> 3.00
    return (
        price_series.astype(str)
        .str.replace("$", "", regex=False)
        .astype(float)
    )

def main():
    # Read + combine all files
    dfs = [pd.read_csv(f) for f in FILES]
    df = pd.concat(dfs, ignore_index=True)

    # Keep only Pink Morsel
    df["product"] = df["product"].astype(str).str.strip().str.lower()
    df = df[df["product"] == "pink morsel"].copy()

    # Convert price and calculate sales
    df["price"] = parse_price_to_float(df["price"])
    df["sales"] = df["price"] * df["quantity"]

    # Final output format
    out = df[["sales", "date", "region"]].copy()
    out.columns = ["Sales", "Date", "Region"]   # match required names

    # Save output file
    output_path = DATA_DIR / "processed_pink_morsel_sales.csv"
    out.to_csv(output_path, index=False)

    print(f" Saved: {output_path} ({len(out)} rows)")

if __name__ == "__main__":
    main()