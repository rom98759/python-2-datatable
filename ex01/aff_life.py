import matplotlib.pyplot as plt
from load_csv import load


def main() -> None:
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return

    date = dataset.columns[1:]
    life_pay = dataset.loc[dataset["country"] == "France"].values[0][1:]

    plt.plot(date, life_pay)

    #  date tous les 40 ans
    tick_idx = range(0, len(date), 40)
    plt.xticks(tick_idx, date[::40], rotation=45)

    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
