from src.data_loading import load_datasets, inspect_dataframes
from src.missing_values import check_missing, clean_datasets
from src.eda_visuals import(
    plot_top_3_countries,
    plot_china_provinces,
    plot_daily_new_cases,
    plot_recovery_rate_comparison,
    plot_canada_death_rates,
    plot_top_3_death_rates,
    plot_south_africa_totals
)

from src.transformation import to_long
from src.merge_data import merge_all

from src.rate_analysis import(
    daily_new_cases,
    recovery_rate_on_date,
    canada_death_rates
)

from src.advanced_analysis import (
    top_3_death_rates,
    south_africa_totals,
    us_monthly_recovery_ratio
)


def main():
    # load datasets
    confirmed, deaths, recovered = load_datasets()
    inspect_dataframes(confirmed, deaths, recovered)
    
    # check and clean missing values
    print("Confirmed missing:", check_missing(confirmed))
    print("Deaths missing:", check_missing(deaths))
    print("Recovered missing:", check_missing(recovered))

    confirmed, deaths, recovered = clean_datasets(confirmed, deaths, recovered)

    # visualization 1 and 2
    plot_top_3_countries(confirmed)
    plot_china_provinces(confirmed)

    # Visualization 3
    plot_daily_new_cases(confirmed)

    # Visualization 4
    plot_recovery_rate_comparison(confirmed, recovered)

    # Visualization 5
    plot_canada_death_rates(confirmed, deaths)

    # Prepare merged dataset for advance visualizations
    confirmed_long = to_long(confirmed, "Confirmed")
    deaths_long = to_long(deaths, "Deaths")
    recovered_long = to_long(recovered, "Recovered")

    # merging all the datsets
    combined = merge_all(
        confirmed_long,
        deaths_long,
        recovered_long
    )

    # Visualization 6 and 7
    plot_top_3_death_rates(combined)
    plot_south_africa_totals(combined)

    countries = ["Germany","France","Italy"]
    daily_cases = daily_new_cases(confirmed, countries)

    canada_rate = recovery_rate_on_date(
        confirmed, 
        recovered,
        country = "Canada",
        date = '12/31/20'
    )

    australia_rate = recovery_rate_on_date(
        confirmed,
        recovered,
        country="Australia",
        date="12/31/20"
    )

    print("Recovery Rate on 2020-12-31")
    print("Canada:", canada_rate)
    print("Australia:", australia_rate)

    death_rates_canada = canada_death_rates(confirmed, deaths)
    print(death_rates_canada)

    top3 = top_3_death_rates(combined)
    print("\nTop 3 Countries by Death Rate:")
    print(top3)

    sa_recovered, sa_deaths = south_africa_totals(combined)
    print("\nSouth Africa Totals:")
    print("Recovered:", sa_recovered)
    print("Deaths:", sa_deaths)

    us_ratio = us_monthly_recovery_ratio(combined)
    us_ratio.plot(title="US Monthly Recovery Ratio")
    us_ratio.show()


if __name__ == "__main__":
    main()