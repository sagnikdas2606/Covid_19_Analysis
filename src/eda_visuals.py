import matplotlib.pyplot as plt

# Top 3 countries - total confirmed cases over time
def plot_top_3_countries(confirmed_df):
    top_countries = confirmed_df.group_by("Country/Region").sum(numeric_only =True).nlargest(3, confirmed_df.columns[-1]).index

    for country in top_countries:
        data = confirmed_df[confirmed_df["Country/Region"] == country].iloc[:,4:].sum()
        plt.plot(data.index, data.values, label = country)
        plt.title("Total Confirmed Cases Over Time for Top 3 Countries")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Confirmed Cases")
        plt.xticks(rotation=45)
        plt.show()

# China Province wise confirmed cases
def plot_china_province(confirmed_df):
    china = confirmed_df[confirmed_df["COuntry/Region"] == "China"]
    china.set_index("Province/State").iloc[:,4:].T.plot(figsize = (10,6))
    plt.title("COVID-19 Confirmed Cases Over Time for Provinces in China")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Confirmed Cases")
    plt.xticks(rotation=45)
    plt.show()

# Daily New Caes - Germany, France, Italy
def plot_daily_new_cases(confirmed_df):
    countries = ["Germany", "France", "Italy"]
    for country in countries:
        data = confirmed_df[confirmed_df["Country/Region"] == country].iloc[:,4:].sum().diff().fillna(0)
        plt.plot(data.index, data.values, labels = country)
        plt.legend()
        plt.title("Daily New COVID-19 Cases")
        plt.xlabel("Date")
        plt.ylabel("Number of New Cases")
        plt.xticks(rotation=45)
        plt.show()

# Recovery rate comparison - Canada vs Australia
def plot_recovery_rate_comparison(confirmed_df, recovered_df):
    countries = ["Canada", "Australia"]
    recovery_rate = {}
    for country in countries:
        confirmed_sum = confirmed_df[confirmed_df["Country/Region"] == country].iloc[:,4:].sum()
        recovered_sum = recovered_df[recovered_df["Country/Region"] == country].iloc[:,4].sum()

        recovery_rate[country] =  recovered_sum["12/31/20"] / confirmed_sum["12/31/20"]

        plt.bar(recovery_rate.keys(), recovery_rate.values())
        plt.title("Recovery Rate Comparison on 2020-12-31")
        plt.ylabel("Recovery Rate")
        plt.show()

def plot_canada_death_rates(confirmed_df, deaths_df):
    cases = confirmed_df[confirmed_df["Country/Region"] == "Canada"].iloc[:,4:].sum(axis = 1)
    deaths = deaths_df[deaths_df["Country/Region"] == "Canada"].iloc[:,4:].sum(axis = 1)

    death_rates = deaths / cases

    death_rates.plot(kind="bar")
    plt.title("Death Rates by Province in Canada")
    plt.xlabel("Province Index")
    plt.ylabel("Death Rate")
    plt.show()

# Top 3 countries by average death rates
def plot_top_3_death_rates(combined_df):
    death_rates = (
        combined_df.groupby("Country/Region")["Deaths"].sum() /
        combined_df.groupby("Country/Region")["Confirmed"].sum()
    ).sort_values(ascending=False).head(3)

    death_rates.plot(kind="bar")
    plt.title("Top 3 Countries with Highest Average Death Rates")
    plt.ylabel("Death Rate")
    plt.show()

# Total Recoveries vs deaths - South Africa
def plot_south_africa_totals(combined_df):
    sa_data = combined_df[combined_df["Country/Region"] == "South Africa"]

    totals = {
        "Total Recoveries": sa_data["Recovered"].sum(),
        "Total Deaths": sa_data["Deaths"].sum()
    }

    plt.bar(totals.keys(), totals.values())
    plt.title("Total Recoveries vs Total Deaths in South Africa")
    plt.ylabel("Counts")
    plt.show()