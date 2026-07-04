# The first column contains the names to be created by the artists

# a space between parts of the name is where it would be broken apart.

# The second column contains the material the name will be created with and the third column contains whether it is return to store "Store" or "Shipped" from Art Factory.

from pathlib import Path
import pandas as pd

def load_orders():
    file_path = Path(__file__).resolve().parent / "data" / "Name List.xlsx"
    df = pd.read_excel(file_path, sheet_name="Orders")
    return df

orders = load_orders()
print(orders.head())
print(orders.columns)