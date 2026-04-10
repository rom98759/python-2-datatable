import matplotlib.pyplot as plt
from load_csv import load


def parse_population(value: str) -> float:
    """Convert values like '3.25M', '400k' or '1.2B' to absolute numbers."""
    raw = str(value).strip()
    if raw.endswith("k"):
        return float(raw[:-1]) * 1_000
    if raw.endswith("M"):
        return float(raw[:-1]) * 1_000_000
    if raw.endswith("B"):
        return float(raw[:-1]) * 1_000_000_000
    return float(raw)


def main() -> None:
    dataset = load("population_total.csv")
    if dataset is None:
        return

    years = [str(year) for year in range(1800, 2051)]
    france_row = dataset.loc[dataset["country"] == "France", years]
    belgium_row = dataset.loc[dataset["country"] == "Belgium", years]

    if france_row.empty or belgium_row.empty:
        print("Error: country not found in dataset")
        return

    population_fr = [
        parse_population(value) / 1_000_000 for value in france_row.values[0]
    ]
    population_be = [
        parse_population(value) / 1_000_000 for value in belgium_row.values[0]
    ]
    years_int = [int(year) for year in years]

    plt.plot(years_int, population_fr, label="France", color="green")
    plt.plot(years_int, population_be, label="Belgium", color="blue")

    plt.xticks(range(1800, 2051, 40), rotation=45)
    plt.yticks(range(0, int(max(population_fr + population_be)) + 20, 20))

    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
