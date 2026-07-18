# The first column contains the names to be created by the artists
# A space between parts of the name is where it would be broken apart.
# The second column contains the material the name will be created with,
# and the third column contains whether it is returned to store "Store"
# or shipped from the art factory.

from pathlib import Path
import re
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def list_files_in_data_directory():
    files = sorted([path for path in DATA_DIR.iterdir() if path.is_file()])
    if not files:
        raise FileNotFoundError(f"No files were found in {DATA_DIR}")
    return files

# Here i might consider a different naming convention because
# the function actually only loads the first sheet in the spreadsheet
# The name currently implies that it loads all the sheets

def load_first_sheet_from_selected_file():
    files_listed = list_files_in_data_directory()

    print("Available files in the data folder:")
    for index, file_path in enumerate(files_listed, start=1):
        print(f"{index}. {file_path.name}")

    while True:
        selection = input("Select a file by number: ").strip()
        if selection.isdigit():
            choice = int(selection)
            if 1 <= choice <= len(files_listed):
                selected_file = files_listed[choice - 1]
                break
        print("Please enter a valid number from the list.")

    excel_file = pd.ExcelFile(selected_file)
    sheet_names = excel_file.sheet_names


    sheet_name = sheet_names[0]

    df = pd.read_excel(selected_file, sheet_name=sheet_name)
    return df


PREFIXES = ["Mc", "Mac", "Van", "De", "Del", "La", "Le", "St", "O'"]


def fix_names_column(name):
    if pd.isna(name):
        return name
    if not isinstance(name, str):
        return name

    cleaned_name = re.sub(r"(?<=[a-z])([A-Z])", r" \1", name)

    for prefix in PREFIXES:
        cleaned_name = re.sub(rf"({re.escape(prefix)})\s+([A-Z])", r"\1\2", cleaned_name)

    return cleaned_name.strip()


def clean_names_column(df):
    if df.empty:
        return df

    first_column = df.columns[0]
    df[first_column] = df[first_column].apply(fix_names_column)
    return df

def print_all_rows(df):
    if df.empty:
        print("The DataFrame is empty.")
        return
    
    print(df.to_string(index=False))


def print_first_column(df):
    if df.empty:
        print("The DataFrame is empty.")
        return

    first_column = df.columns[0]
    print(df[first_column].to_string(index=False))

if __name__ == "__main__":
    orders = load_first_sheet_from_selected_file()

    orders = clean_names_column(orders)

    print_first_column(orders)


