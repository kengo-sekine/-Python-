import subprocess
import tempfile
import unittest
from pathlib import Path

import app


PROJECT_DIR = Path(__file__).resolve().parent.parent


class CheckNumberTests(unittest.TestCase):
    def test_example_1(self) -> None:
        self.assertEqual(app.check_number([1, 2, 3], [1, 3, 5]), 2)

    def test_example_2(self) -> None:
        self.assertEqual(app.check_number([20, 20, 10, 10, 10], [10, 3, 10]), 3)

    def test_duplicate_winning_numbers_do_not_double_count_one_choice(self) -> None:
        self.assertEqual(app.check_number([7], [7, 7, 7]), 1)

    def test_duplicate_chosen_numbers_count_individually(self) -> None:
        self.assertEqual(app.check_number([5, 5, 2], [5]), 2)

    def test_main_reads_csv_and_prints_result(self) -> None:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf8", newline="", suffix=".csv", delete=False
        ) as file:
            file.write("1,2,3\n1,3,5\n")
            temp_path = file.name

        completed = subprocess.run(
            ["python3", "main.py", temp_path],
            cwd=PROJECT_DIR,
            check=True,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.stdout, "2\n")


if __name__ == "__main__":
    unittest.main()
