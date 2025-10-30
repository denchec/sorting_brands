import argparse
import tabulate
from utils import (
    get_row_data_by_index,
    is_valid_input,
    read_csv,
    sort_by_rating,
)


def average_rating_report(data: list[str]):
    data = get_row_data_by_index(data, [0, 3])
    data = sort_by_rating(data, 1)
    print(
        tabulate.tabulate(
            data,
            headers=["Brand", "Rating"],
            tablefmt="pipe",
            showindex="always",
        )
    )


ALL_REPORTS = {
    "average-rating": average_rating_report,
}


def main(report_list: list[str], files: list[str]):
    if not is_valid_input(report_list, files):
        return

    data = read_csv(files)

    for report_name in report_list:
        if report_name not in ALL_REPORTS:
            print(f"Report '{report_name}' not found")
            continue

        report = ALL_REPORTS[report_name]
        report(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", type=str, help="File names", nargs="+")
    parser.add_argument("--report", type=str, help="Report name", nargs="+")
    args = parser.parse_args()

    main(args.report, args.files)
