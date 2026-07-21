import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("fancy_sorter", ROOT / "fancy-sorter.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def test_fix_names_column_inserts_space_before_middle_capital():
    assert module.fix_names_column("JohnDoe") == "John Doe"
    assert module.fix_names_column("EvanVaverka") == "Evan Vaverka"
    assert module.fix_names_column("MaryJaneWatson") == "Mary Jane Watson"
    assert module.fix_names_column("Evan PatrickVaverka") == "Evan Patrick Vaverka"
    assert module.fix_names_column("EvanVaverka Smith") == "Evan Vaverka Smith"
    assert module.fix_names_column("AliciaKeys") == "Alicia Keys"


def test_fix_names_column_preserves_common_name_prefixes():
    assert module.fix_names_column("McMahan") == "McMahan"
    assert module.fix_names_column("MacDonald") == "MacDonald"
    assert module.fix_names_column("VanHouten") == "VanHouten"
    assert module.fix_names_column("DeSoto") == "DeSoto"


def test_split_names_column_splits_names_into_first_middle_last():
    df = module.pd.DataFrame({"Name": ["Evan Vaverka", "Evan Patrick Vaverka", "Evan", "E. Vaverka"]})

    result = module.split_names_column(df)

    assert list(result.columns) == ["First", "Middle", "Last"]
    assert "Name" not in result.columns
    assert result["First"].tolist() == ["Evan", "Evan", "Evan", "E."]
    assert result["Middle"].tolist() == ["N/A", "Patrick", "N/A", "N/A"]
    assert result["Last"].tolist() == ["Vaverka", "Vaverka", "N/A", "Vaverka"]
