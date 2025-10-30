import csv
import pytest


@pytest.fixture
def sample_rows():
    return [
        ["iphone 15 pro", "apple", "999", "4.9"],
        ["galaxy s23 ultra", "samsung", "1199", "4.8"],
        ["redmi note 12", "xiaomi", "199", "4.6"],
    ]


@pytest.fixture
def sample_csv_path(tmp_path):
    csv_path = tmp_path / "products.csv"

    with csv_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "brand", "price", "rating"])
        writer.writerow(["iphone 15 pro", "apple", "999", "4.9"])
        writer.writerow(["galaxy s23 ultra", "samsung", "1199", "4.8"])
        writer.writerow(["redmi note 12", "xiaomi", "199", "4.6"])

    return csv_path
