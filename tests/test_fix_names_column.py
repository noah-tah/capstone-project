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
