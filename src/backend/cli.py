"""Command-line interface for generating a randomized matrix."""

from libraries.matrix import Matrix


def parse_positive_int(value: str, name: str) -> int:
    """Parse a string as a positive integer. Raises ValueError with a clear message if invalid."""
    try:
        parsed = int(value)
    except ValueError:
        raise ValueError(f"{name} must be a whole number, got {value!r}")
    if parsed <= 0:
        raise ValueError(f"{name} must be greater than 0, got {parsed}")
    return parsed


def prompt_int(prompt: str, name: str) -> int:
    """Repeatedly prompt the user until a valid positive integer is entered."""
    while True:
        raw = input(prompt)
        try:
            return parse_positive_int(raw, name)
        except ValueError as e:
            print(e)


def build_random_matrix(rows: int, cols: int, low: int = 1, high: int = 10) -> Matrix:
    """Create a rows x cols Matrix filled with random integers in [low, high)."""
    return Matrix(rows, cols).randomizeInt((low, high))


def main():
    print("Random Matrix Generator")
    rows = prompt_int("Enter number of rows (n): ", "rows")
    cols = prompt_int("Enter number of columns (m): ", "columns")
    matrix = build_random_matrix(rows, cols)
    print(matrix)


if __name__ == "__main__":
    main()
