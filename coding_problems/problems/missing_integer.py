
def missing_digit(digits: list, n: int) -> int:
    total: int = sum(digits)
    sum_to_n: int = (n * (n + 1)) // 2
    missing_digit: int = sum_to_n - total

    return missing_digit