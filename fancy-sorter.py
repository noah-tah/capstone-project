# The first column contains the names to be created by the artists
# A space between parts of the name is where it would be broken apart.
# The second column contains the material the name will be created with,
# and the third column contains whether it is returned to store "Store"
# or shipped from the art factory.

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def list_data_files():
    files = sorted([path for path in DATA_DIR.iterdir() if path.is_file()])
    if not files:
        raise FileNotFoundError(f"No files were found in {DATA_DIR}")
    return files


def load_orders():
    files = list_data_files()

    print("Available files in the data folder:")
    for index, file_path in enumerate(files, start=1):
        print(f"{index}. {file_path.name}")

    while True:
        selection = input("Select a file by number: ").strip()
        if selection.isdigit():
            choice = int(selection)
            if 1 <= choice <= len(files):
                selected_file = files[choice - 1]
                break
        print("Please enter a valid number from the list.")

    excel_file = pd.ExcelFile(selected_file)
    sheet_names = excel_file.sheet_names

    if "Orders" in sheet_names:
        sheet_name = "Orders"
    else:
        sheet_name = sheet_names[0]

    df = pd.read_excel(selected_file, sheet_name=sheet_name)
    return df


orders = load_orders()
print(orders.head())
print(orders.columns)