from pathlib import Path
from utils import get_row_data_by_index, is_valid_input, read_csv, sort_by_rating


def test_get_row_data_by_index_name_and_rating(sample_rows):
    result = get_row_data_by_index(sample_rows, [0, 3])

    assert result == [
        ["iphone 15 pro", "4.9"],
        ["galaxy s23 ultra", "4.8"],
        ["redmi note 12", "4.6"],
    ]


def test_get_row_data_by_index_brand_and_rating(sample_rows):
    result = get_row_data_by_index(sample_rows, [1, 3])

    assert result == [
        ["apple", "4.9"],
        ["samsung", "4.8"],
        ["xiaomi", "4.6"],
    ]


def test_is_valid_input_happy_path():
    assert is_valid_input(["average-rating"], ["products.csv"]) is True


def test_is_valid_input_reports_missing(capsys):
    ok = is_valid_input([], ["products.csv"])
    out = capsys.readouterr().out

    assert ok is False
    assert "Report title not specified" in out


def test_is_valid_input_files_missing(capsys):
    ok = is_valid_input(["average-rating"], [])
    out = capsys.readouterr().out

    assert ok is False
    assert "File names not specified" in out


def test_read_csv_reads_expected_rows(sample_csv_path: Path):
    rows = read_csv([str(sample_csv_path)])

    assert rows == [
        ["iphone 15 pro", "apple", "999", "4.9"],
        ["galaxy s23 ultra", "samsung", "1199", "4.8"],
        ["redmi note 12", "xiaomi", "199", "4.6"],
    ]


def test_read_csv_ignores_non_csv_extension(sample_csv_path: Path, tmp_path: Path):
    txt_file = tmp_path / "note.txt"
    txt_file.write_text("this is not csv")
    rows = read_csv([str(sample_csv_path), str(txt_file)])

    assert len(rows) == 3


def test_sort_by_rating_descending(sample_rows):
    sorted_rows = sort_by_rating(sample_rows, 3)

    assert [r[0] for r in sorted_rows] == [
        "iphone 15 pro",
        "galaxy s23 ultra",
        "redmi note 12",
    ]
