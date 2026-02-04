import matplotlib.pyplot as plt

def top_3_death_rates(combined):
    rates = (
        combined.groupby("Country/Region")["Deaths"].sum()/
        combined.groupby("Country/Region")["Confirmed"].sum()
    )
    return rates.sort_values(ascending = False).head(3)

def south_africa_totals(combined):
    sa = combined[combined["Country/Region"] == "South Africa"]
    return sa["Recovered"].sum(), sa["Deaths"].sum()

def us_monthly_recovery_ratio(combined):
    us = combined[combined["Country/Region"].isin(["US","United States"])]
    us = combined[combined["Country/Region"].isin(["US","United States"])]
    us = us.set_index("Date").resample("ME").sum()

    us = us[us["Confirmed"] > 0] 
    return us["Recovered"] / us["Confirmed"]