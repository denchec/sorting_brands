import csv
from operator import itemgetter


def get_row_data_by_index(data: list[list[str]], keep: list[int]) -> list[list[str]]:
    get_cols = itemgetter(*keep)
    cleaned = [list(get_cols(row)) for row in data]
    return cleaned


def is_valid_input(report_list: list[str], files: list[str]) -> bool:
    if not report_list:
        print("Report title not specified")
        return False

    if not files:
        print("File names not specified")
        return False

    return True


def read_csv(files: list[str]) -> list[list[str]]:
    data = []

    for file in files:
        if not file.lower().endswith(".csv"):
            continue

        with open(file, "r") as f:
            reader = csv.reader(f)

            if not reader:
                continue

            for i, row in enumerate(reader):
                if i == 0:  # Skip the header row
                    continue

                if len(row) != 4:
                    continue

                data.append(row)

    return data


def sort_by_rating(data: list[list[str]], sort_category: int) -> list[list[str]]:
    return sorted(data, key=lambda x: x[sort_category], reverse=True)
