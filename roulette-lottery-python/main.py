"""CLI entry point for the roulette lottery exercise."""

import csv
import sys

import app


def main() -> None:
    file_name = sys.argv[1]

    with open(file_name, encoding="utf8", newline="") as file:
        reader = list(csv.reader(file))
        choose_number = [int(value) for value in reader[0]]
        winning_number = [int(value) for value in reader[1]]

    print(app.check_number(choose_number, winning_number))


if __name__ == "__main__":
    main()
