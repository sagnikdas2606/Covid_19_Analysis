import matplotlib.pyplot as plt

def daily_new_cases(confirmed_df, countries):
    results = {}

    for country in countries:
        data = (
            confirmed_df[confirmed_df["Country/Region"] == country]
            .iloc[:,4:]
            .sum(axis=0)
            .diff()
            .fillna(0)
        )

        results[country] = data
        return results
    
    def recovery_rate_on_date(confirmed, recovered, country, date):
        confirmed_sum = confirmed[confirmed["Country/Region"] == country].iloc[:,4:].sum()
        recovered_sum = recovered[recovered["Country/Region"] == country].iloc[:,4:].sum()
        recovered_rate = recovered_sum[date]/confirmed_sum[date]
        return recovered_rate
    
    def canada_death_rates(confirmed, deaths):
        cases = confirmed[confirmed["Country/Region"] == "Canada"].iloc[:,4:].sum(axis = 1)
        death = deaths[deaths["Country/Region"] == "Canada"].iloc[:,4:].sum(axis = 1)
        return deaths/cases
