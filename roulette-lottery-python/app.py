"""Roulette winner counting logic."""


def check_number(choose_number: list[int], winning_number: list[int]) -> int:
    """Count chosen numbers that appear at least once in the winning numbers."""
    winning_set = set(winning_number)
    count = 0

    for number in choose_number:
        if number in winning_set:
            count += 1

    return count
