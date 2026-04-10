import matplotlib.pyplot as plt
from load_csv import load


def parse_gdp(value: str) -> float:
    """Convert values like '3.25M', '400k' or '1.2B' to absolute numbers."""
    raw = str(value).strip()
    if raw == "" or raw.lower() == "nan":
        return float("nan")
    raw = raw.replace(",", "")
    if raw.endswith("k"):
        return float(raw[:-1]) * 1_000
    if raw.endswith("M"):
        return float(raw[:-1]) * 1_000_000
    if raw.endswith("B"):
        return float(raw[:-1]) * 1_000_000_000
    try:
        return float(raw)
    except ValueError:
        return float("nan")


def main() -> None:
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if income is None:
        return
    life = load("life_expectancy_years.csv")
    if life is None:
        return

    year = "1900"

    income_1900 = income[["country", year]].rename(columns={year: "gdp"})
    life_1900 = life[["country", year]].rename(columns={year: "life"})
    merged = income_1900.merge(life_1900, on="country", how="inner")

    merged["gdp"] = merged["gdp"].apply(parse_gdp)
    merged["life"] = merged["life"].astype(float)
    merged = merged.dropna(subset=["gdp", "life"])
    merged = merged[(merged["gdp"] > 0) & (merged["life"] > 0)]
    max_gdp = merged["gdp"].max()

    plt.figure(figsize=(10, 6))
    plt.scatter(
        merged["gdp"],
        merged["life"],
        s=18,
        alpha=0.7,
        color="blue",
    )
    plt.xscale("log")
    plt.xlim(left=300, right=max(10_000, max_gdp * 1.1))
    plt.xticks([300, 1_000, 10_000], ["300", "1k", "10k"])
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.title("1900")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
