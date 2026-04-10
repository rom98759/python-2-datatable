import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV dataset, print its dimensions, and return it.

    Returns None when the file path or file format is invalid.
    """
    try:
        dataset = pd.read_csv(path, encoding="utf-8-sig")
    except (
        FileNotFoundError,
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        UnicodeDecodeError,
        OSError,
    ):
        print("Error: bad path or bad file format")
        return None

    print(f"Loading dataset of dimensions {dataset.shape}")
    return dataset
