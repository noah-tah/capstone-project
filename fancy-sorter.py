from pathlib import Path
import re
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_FILE = OUTPUT_DIR / "Sorted Name List.xlsx"


def list_files_in_data_directory():
    files = sorted([path for path in DATA_DIR.iterdir() if path.is_file()])
    if not files:
        raise FileNotFoundError(f"No files were found in {DATA_DIR}")
    return files


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


def split_name(name):
    if pd.isna(name) or not isinstance(name, str):
        return []

    return [part for part in name.strip().split() if part]


def split_names_column(df):
    if df.empty or df.shape[1] == 0:
        return df

    result_df = df.copy()
    first_column = result_df.columns[0]
    cleaned_names = result_df[first_column].apply(fix_names_column)
    split_names = cleaned_names.apply(split_name)

    first_names = []
    middle_names = []
    last_names = []

    for parts in split_names:
        if not parts:
            first_names.append("N/A")
            middle_names.append("N/A")
            last_names.append("N/A")
        elif len(parts) == 1:
            first_names.append(parts[0])
            middle_names.append("N/A")
            last_names.append("N/A")
        elif len(parts) == 2:
            first_names.append(parts[0])
            middle_names.append("N/A")
            last_names.append(parts[1])
        else:
            first_names.append(parts[0])
            middle_names.append(" ".join(parts[1:-1]))
            last_names.append(parts[-1])

    name_columns = pd.DataFrame({
        "First": first_names,
        "Middle": middle_names,
        "Last": last_names,
    })

    remaining_columns = result_df.drop(columns=[first_column])
    return pd.concat([name_columns, remaining_columns], axis=1)

if __name__ == "__main__":
    orders = load_first_sheet_from_selected_file()

    orders = split_names_column(orders)
    orders = orders.sort_values(by="First", ascending=True, kind="mergesort")

    OUTPUT_DIR.mkdir(exist_ok=True)
    orders.to_excel(OUTPUT_FILE, index=False)
    print(f"Saved output to {OUTPUT_FILE}")

